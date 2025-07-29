
def generate(data, filename='report.txt'):
    with open(filename, 'w') as f:
        for key, value in data.items():
            f.write(f"--- {key.upper()} ---\n")
            if isinstance(value, dict):
                for k, v in value.items():
                    f.write(f"{k}: {v}\n")
            elif isinstance(value, list):
                for item in value:
                    f.write(f"{item}\n")
            else:
                f.write(f"{value}\n")
            f.write("\n")
