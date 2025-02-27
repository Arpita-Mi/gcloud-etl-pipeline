import subprocess

command = [
    "python csv_handling/create_csv.py",
    "python storage/upload_to_gcs.py",
    "python dataflow/dataflow_pipleline.py"
]

def run_command():
    for cmd in command:
        process = subprocess.run(cmd, shell=True)
        if process.returncode != 0:
            print(f"Error in Executing {cmd}")
            return
    print(f"succesfully executed")

if __name__ == "__main__":
    run_command()