
# Automated ID Card Generator from Excel Data

The Automated ID Card Generator is a Python script that automates the process of creating personalized ID cards for students or trainees based on their information stored in an Excel spreadsheet. The script leverages various Python libraries, including NumPy, Pandas, PIL (Python Imaging Library), and regular expressions, to efficiently process student data and generate customized ID cards.

## Features

- **Data Processing**: The script reads student information from the specified Excel file, including name, trade name, start date, end date, location, and photo path. It formats and validates the data to ensure accuracy.

- **ID Card Template**: The project includes a pre-designed ID card template (template.jpg) that serves as the background for the generated ID cards. The student's photo is resized to fit the designated space on the template.

- **Custom Fonts**: To enhance the visual appeal of the ID cards, the script uses custom fonts for text rendering. It applies formatting and positioning for the student's name, trade name, start date, end date, and location.

- **Output Directory**: The generated ID cards are saved in an "output" directory, automatically created if it doesn't exist. Each ID card file is uniquely named based on the student's name to avoid naming conflicts.

## Usage

1. **Install Dependencies**: Before running the script, ensure you have Python installed along with the required libraries: NumPy, Pandas, PIL, and re.

2. **Data Preparation**: Create an Excel spreadsheet with student information. Use columns named "Name," "Passport Size Photo," "Trade Name," "Starting Date," "Ending Date," and "Coordinate Location name."

3. **Template Image**: Provide a suitable ID card template (template.jpg) with space for the student's photo and information.

4. **Custom Fonts**: Ensure the custom fonts (slavefont.ttf, GOUDOSB.ttf, and GOUDOS.ttf) are available in the specified paths.

5. **Run the Script**: Modify the range of rows (start_row and end_row variables) to generate ID cards for desired students. Execute the script to generate the ID cards.

6. **Output**: The generated ID cards are saved in the "output" directory, each with a unique filename based on the student's name.

## Contributions

Contributions to this project are welcome! If you encounter any issues or have ideas for improvements, please feel free to create an issue or submit a pull request.

### Contributor

- [Anurag Devoor](https://github.com/anuragdevoor)
  - Software Engineer - Java Full Stack

## Example

```python
# Modify start_row and end_row as needed
start_row = 1
end_row = 2

# Load Excel data and generate ID cards
# ...



