import sys
import json

def update_model_weights(endpoint_name, parameter_value):
    with open("model_weights_config.json") as f:
        config = json.load(f)

    config[endpoint_name]["model_weights_file"] = parameter_value

    with open("model_weights_config.json", "w") as f:
        json.dump(config, f)
    


if __name__ == "__main__":
    args = sys.argv
    endpoint_name = args[1]
    parameter_value = args[2]

    update_model_weights(endpoint_name, parameter_value)



