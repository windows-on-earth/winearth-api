import csv, yaml


# Convert the exported CSV file to a YAML file that can be used to populate the database
def csv_to_yaml(csv_file, inital_file, yaml_file):

    # Open the existing YAML file and read the data
    with open(inital_file, "r") as f:
        inital_data = yaml.load(f, Loader=yaml.SafeLoader)

    pk = 1
    inital_movies = []
    # Create a new list to store the data
    yaml_data = inital_data

    # Loop through the old data to get the last pk and a list of movies
    for i in range(len(inital_data)):
        # Get the last pk
        if int(inital_data[i]["pk"]) > pk:
            pk = int(inital_data[i]["pk"])

        # Append the movie to the list
        inital_movies.append(inital_data[i]["fields"]["movie"])

    # Open the CSV file and read the data
    with open(csv_file, "r") as file:
        csv_file = csv.reader(file)
        data = list(csv_file)

    # Extract the column names and the data from the CSV file
    columns = data.pop(0)

    # Create a dictionary for each row in the CSV file
    for i in range(len(data[1:])):

        # Skip the row if the movie is already in the initial.yaml
        if data[i][0] in inital_movies:
            print(f"Skipping {data[i][0]}")
            continue

        row = {}

        # Increment the pk
        pk = pk + 1

        row["model"] = "api.movies"
        row["pk"] = pk
        row["fields"] = dict(zip(columns, data[i]))

        yaml_data.append(row)

    with open(yaml_file, "w") as file:
        yaml.dump(yaml_data, file)


csv_to_yaml("movies.csv", "initial.yaml", "movies.yaml")
