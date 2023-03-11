class PPMImage:
    def __init__(self, filename):
        # Store the filename for later use
        self.filename = filename
        # Initialize the width, height, and data attributes
        self.width = 0
        self.height = 0
        self.max_value = 0
        self.data = None

        # Parse the PPM file when the object is created
        self.__parse_ppm_file()

    def __parse_ppm_file(self):
        # Open the file in binary mode so that we can read in the data as bytes
        with open(self.filename, 'rb') as f:
            # Read in the magic number at the beginning of the file
            magic_number = f.readline().strip()

            # Check if the magic number indicates a binary PPM file
            if magic_number == b'P6':
                self.__parse_binary_ppm(f)
            # Check if the magic number indicates an ASCII PPM file
            elif magic_number == b'P3':
                self.__parse_ascii_ppm(f)
            # If the magic number is not recognized, raise an exception
            else:
                raise ValueError(f'Invalid magic number {magic_number} for PPM file')

    def __parse_binary_ppm(self, f):
        # Read in the dimensions of the image (width and height)
        dimensions = f.readline().split()
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        # Read in the maximum pixel value (ignored in this implementation)
        self.max_value = int(f.readline())

        # Read in the image data as a bytearray
        self.data = bytearray(f.read())

    def __parse_ascii_ppm(self, f):
        # Read in the dimensions of the image (width and height)
        dimensions = f.readline().split()
        self.width = int(dimensions[0])
        self.height = int(dimensions[1])

        # Read in the maximum pixel value
        self.max_value = int(f.readline())

        # Read in the image data as a list of RGB tuples
        self.data = []

        # Iterate over each line in the file
        for line in f:
            # Split the line into individual RGB values
            pixels = line.split()
            # Iterate over each pixel in the line
            for i in range(0, len(pixels), 3):
                # Convert the RGB values to a tuple and append it to the data list
                r = int(pixels[i])
                g = int(pixels[i + 1])
                b = int(pixels[i + 2])
                self.data.append((r, g, b))

    def get_pixel(self, x, y):
        # Check if the requested pixel is outside the bounds of the image
        if x >= self.width or y >= self.height:
            raise ValueError('Invalid pixel coordinates')

        # If the image is binary (3 bytes per pixel), read the data as a bytearray
        if isinstance(self.data, bytearray):
            # Calculate the index of the requested pixel in the data list
            index = (x + y * self.width) * 3
            # Extract the RGB values from the data bytearray
            r = self.data[index]
            g = self.data[index + 1]
            b = self.data[index + 2]
            # Return the RGB tuple of the pixel
            return (r, g, b)
        # If the image is grayscale (1 byte per pixel), read the data

        elif isinstance(self.data, list):
            # Calculate the index of the requested pixel in the data list
            index = x + y * self.width
            # Return the RGB tuple of the pixel
            return self.data[index]


    def get_pixels(self):
        # If the image is binary (3 bytes per pixel), return the data as a bytearray
        if isinstance(self.data, bytearray):
            return self.data
        # If the image is grayscale (1 byte per pixel), convert the data to a bytearray
        elif isinstance(self.data, list):
            pixels = bytearray()
            for pixel in self.data:
                pixels.append(pixel[0])
                pixels.append(pixel[1])
                pixels.append(pixel[2])
            return pixels


    def save(self, filename):
        # Open the output file in binary mode
        with open(filename, 'wb') as f:
            # Write the magic number for binary PPM files
            f.write(b'P6\n')
            # Write the dimensions of the image
            f.write(f'{self.width} {self.height}\n'.encode())
            # Write the maximum pixel value (ignored in this implementation)
            f.write(f'{self.max_value}\n'.encode())
            # Write the pixel data to the file
            f.write(self.get_pixels())
