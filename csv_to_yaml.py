import csv, yaml

# Convert the exported CSV file to a YAML file that can be used to populate the database
def csv_to_yaml(csv_file, yaml_file):
    # Open the CSV file and read the data
    with open(csv_file, "r") as file:
        csv_file = csv.reader(file)
        data = list(csv_file)

    yaml_data = []
    # Extract the column names and the data from the CSV file
    columns = data.pop(0)

    # Create a dictionary for each row in the CSV file
    for i in range(len(data[1:])):

        row = {}

        row["model"] = "api.movies"
        row["pk"] = i + 1
        row["fields"] = dict(zip(columns, data[i]))

        yaml_data.append(row)

    with open(yaml_file, "w") as file:
        yaml.dump(yaml_data, file)


csv_to_yaml("movies.csv", "movies.yaml")
