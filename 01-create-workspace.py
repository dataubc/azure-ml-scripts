from azureml.core import Workspace


ws = Workspace.from_config()

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')
