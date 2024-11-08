import json
import os

DAGS = "projetos"
PROJETOS = os.listdir(DAGS)
CONN_FILE = "/configs/connections.json"
VAR_FILE = "/configs/variables.json"
DEST_CONN_FILE = "utils/configs/connections_consolidated.json"
DEST_VAR_FILE = "utils/configs/variables_consolidated.json"

def consolidate_configs():
    
    connections = {}
    variables = {}

    for projeto in PROJETOS:
        conn_file = DAGS + "/" + projeto + CONN_FILE
        var_file = DAGS + "/" + projeto + VAR_FILE

        if os.path.exists(conn_file):
            with open(conn_file, "r") as f:
                conn_data = json.load(f)
                connections.update(conn_data)
        if os.path.exists(var_file):
            with open(var_file, "r") as f:
                var_data = json.load(f)
                variables.update(var_data)
        
    if os.path.exists(DEST_CONN_FILE):
        os.remove(DEST_CONN_FILE)
    if os.path.exists(DEST_VAR_FILE):
        os.remove(DEST_VAR_FILE)
    
    with open(DEST_CONN_FILE, "w") as f:
        json.dump(connections, f, indent=4)
    with open(DEST_VAR_FILE, "w") as f:
        json.dump(variables, f, indent=4)

if __name__ == "__main__":
    consolidate_configs()