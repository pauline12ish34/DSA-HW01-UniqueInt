class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        """
        Reads a list of integers from an input file, identifies unique integers,
        and generates an output file with sorted unique integers.

        Args:
            inputFilePath (str): Path to the input file.
            outputFilePath (str): Path to the output file.
        """
        unique_integers = set()

        # Read input file
        with open(inputFilePath, 'r') as infile:
            for line in infile:
                try:
                    integer = int(line.strip())  # Remove leading/trailing spaces
                    unique_integers.add(integer)
                except ValueError:
                    # Skip the non-integer lines
                    pass

        # Sort unique integers
        sorted_unique_integers = sorted(unique_integers)

        # Write to output file
        with open(outputFilePath, 'w') as outfile:
            for integer in sorted_unique_integers:
                outfile.write(f"{integer}\n")

if __name__ == "__main__":
    input_file_path =r"C:\Users\user\Desktop\ALU-intranet projecta\DSA-HW01-UniqueInt\sampleInputs\small_sample_input_02.txt"
    output_file_path = r"C:\Users\user\Desktop\ALU-intranet projecta\DSA-HW01-UniqueInt\sampleResults\small_sample_input_02.txt"

    UniqueInt.processFile(input_file_path, output_file_path)
    # Print the sorted unique integers to the console
    with open(output_file_path, 'r') as result_file:
        for line in result_file:
            print(line.strip())
