def modify_content(content):

    return content.upper()

def main():
    filename = input("python3 prac: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    modified_content = modify_content(content)

    new_filename = filename.rsplit('.', 1)
    if len(new_filename) == 2:
        output_filename = f"{new_filename[0]}_modified.{new_filename[1]}"
    else:
        output_filename = f"{filename}_modified"

    try:
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        print(f"Modified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    main()
