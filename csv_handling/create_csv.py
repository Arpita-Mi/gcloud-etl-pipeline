import csv

# Define CSV file name
csv_filename = "data.csv"

# Sample data
data = [
    ["id", "description", "is_active"],
    [0, "Error", True],
    [1, "Message", True],
    [2, "bool", True],
    [3, "single options", True],
    [4, "skip", True],
    [5, "location", True],
    [6, "images", True],
    [7, "multiple selection options", True],
    [8, "checklist", True],
    [9, "user_message", True],
    [10, "end_flow", True],
    [11, "skip_with_groupchat", True],
    [12, "input_project", True],
    [13, "View form detail", True],
    [14, "Reviewer Name", True],
    [15, "attendees", True],
    [16, "statistic_form", True],
    [17, "exit-button", True],
    [18, "calendar", True],
    [19, "inspection_subcategories_statistics", True],
    [20, "inspection_multiple_questions", True],
    [21, "inspection_answer_summary", True],
    [22, "leadership_questions", True],
    [23, "leadership_summary", True],
    [24, "inspection_nc_details", True],
    [25, "inspection_nc_summary", True],
]



# Create CSV file and write data
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully!")