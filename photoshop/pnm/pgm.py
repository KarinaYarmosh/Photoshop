class PGMImage:
    def __init__(self, filename):
        # Store the filename for later use
        self.filename = filename
        # Initialize the width, height, and data attributes
        self.width = 0
        self.height = 0
        self.max_value = 0
        self.data = None

        # Parse the PGM file when the object is created
        self.__parse_pgm_file()

    def __parse_pgm_file(self):
        # Open the file in binary mode so that we can read in the data as bytes
        with open(self.filename, 'rb') as f:
            # Read in the magic number at the beginning of the file
            magic_number = f.readline().strip()

            # Check if the magic number indicates a binary PGM file
            if magic_number == b'P5':
                self.__parse_binary_pgm(f)
            # Check if the magic number indicates an ASCII PGM file
            elif magic_number == b'P2':
                self.__parse_ascii_pgm(f)
            # If the magic number is not recognized, raise an exception
            else:
                raise ValueError(f'Invalid magic number {magic_number} for PGM file')

    def __parse_binary_pgm(self, f):
        # Read in the dimensions of the image (width and height)
        dimensions = f.readline().split()
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        # Read in the maximum pixel value (ignored in this implementation)
        self.max_value = int(f.readline())

        # Read in the image data as a bytearray
        self.data = bytearray(f.read())

    def __parse_ascii_pgm(self, f):
        # Read in the dimensions of the image (width and height)
        dimensions = f.readline().split()
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        # Read in the maximum pixel value
        self.max_value = int(f.readline())

        # Read in the image data as a list of integers
        self.data = []

        # Iterate over each line in the file
        for line in f:
            # Split the line into individual numbers
            for c in line.split():
                # Convert the number to an integer and append it to the data list
                self.data.append(int(c))

    def get_pixel(self, x, y):
        # Check if the requested pixel is outside the bounds of the image
        if x >= self.width or y >= self.height:
            raise ValueError('Invalid pixel coordinates')

        # If the image is binary (1 byte per pixel), read the data as a bytearray
        if isinstance(self.data, bytearray):
            # Calculate the index of the requested pixel in the data list
            index = x + y * self.width
            # Return the byte value of the pixel
            return self.data[index]
        # If the image is grayscale (1 byte per pixel), read the data as a list of integers
        else:
            # Calculate the index of the requested pixel in the data list
            index = x + y * self.width
            # Return the integer value of the pixel
            return self.data[index]

    def get_pixels(self):
        if isinstance(self.data, bytearray):
            return self.data
        elif isinstance(self.data, list):
            pixels = bytearray()
            for pixel in self.data:
                pixels.append(pixel)
            return pixels
