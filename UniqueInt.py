import os


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


def main():
    while True:
        # Prompt user for input filename
        input_filename = input("Enter the input filename (with extension): ")

        # Define the directories
        input_directory = r'C:\Users\user\Desktop\ALU-intranet projecta\DSA-HW01-UniqueInt\sampleInputs'
        output_directory = r'C:\Users\user\Desktop\ALU-intranet projecta\DSA-HW01-UniqueInt\sampleResults'

        # Build full input path
        input_filepath = os.path.join(input_directory, input_filename)

        # Check if the file exists in the input directory
        if os.path.exists(input_filepath):
            print(f"Input file '{input_filename}' exists.")

            # Create the output filename by appending 'result.txt'
            output_filename = input_filename.replace('.txt', '') + 'result.txt'
            output_filepath = os.path.join(output_directory, output_filename)

            # Process the file using the UniqueInt class
            UniqueInt.processFile(input_filepath, output_filepath)
            print(f"Output file '{output_filename}' created in {output_directory}.")

            # Optionally print the sorted unique integers to the console
            with open(output_filepath, 'r') as result_file:
                print("\nSorted unique integers from the output file:")
                for line in result_file:
                    print(line.strip())

        else:
            print(f"Input file '{input_filename}' doesn't exist.")

        # Ask user if they want to continue or exit
        continue_choice = input("\nDo you want to process another file? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
