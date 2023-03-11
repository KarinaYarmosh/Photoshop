class PBMImage:
    def __init__(self, filename):
        # Store the filename for later use
        self.filename = filename
        # Initialize the width, height, and data attributes
        self.width = 0
        self.height = 0
        self.data = None

        # Parse the PBM file when the object is created
        self.__parse_pbm_file()

    def __parse_pbm_file(self):
        # Open the file in binary mode so that we can read in the data as bytes
        with open(self.filename, 'rb') as f:
            # Read in the magic number at the beginning of the file
            magic_number = f.readline().strip()

            # Check if the magic number indicates a binary PBM file
            if magic_number == b'P4':
                self.__parse_binary_pbm(f)
            # Check if the magic number indicates an ASCII PBM file
            elif magic_number == b'P1':
                self.__parse_ascii_pbm(f)
            # If the magic number is not recognized, raise an exception
            else:
                raise ValueError(f'Invalid magic number {magic_number} for PBM file')

    def __parse_binary_pbm(self, f):
        # Read in the dimensions of the image (width and height)
        dimensions = f.readline().split()
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        # Read in the image data as a bytearray
        self.data = bytearray(f.read())

    def __parse_ascii_pbm(self, f):
        # Read in the dimensions of the image (width and height)
        dimensions = f.readline().split()
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        # Read in the image data as a list of integers
        self.data = []

        # Iterate over each line in the file
        for line in f:
            #remove whitechars
            new_line = line.strip()
            # Split the line into individual numbers
            for c in new_line:

                if c == '0':
                    self.data.append(0)
                elif c == '1':
                    self.data.append(1)
                else:
                    raise ValueError(f'Invalid pixel value {c} for PBM file')

    def get_pixel(self, x, y):
        # Check if the requested pixel is outside the bounds of the image
        if x >= self.width or y >= self.height:
            raise ValueError('Invalid pixel coordinates')

        # If the image is binary (1 bit per pixel), read the data as a bytearray
        if isinstance(self.data, bytearray):
            # Calculate the byte index and bit offset for the requested pixel
            byte_index = x // 8 + y * (self.width // 8)
            bit_offset = 7 - (x % 8)
            # Read the bit value from the appropriate byte
            byte_value = self.data[byte_index]
            return (byte_value >> bit_offset) & 1
        # If the image is grayscale (8 bits per pixel), read the data as a list of integers
        else:
            # Calculate the index of the requested pixel in the data list
            index = x + y * self.width
            # Return the integer value of the pixel
            return self.data[index]