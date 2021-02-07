# Running_AzureML_scripts
Running python scripts in AzureML

[Edited form the official Azure docs](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-sdk-setup-local)

# imprtant commands:
- conda env create -f .azureml/lr-env.yml
> this requires having a directory .azureml that includes a file lr-env.yml which has all the needed libraries
- conda activate lr-env
- python 04-run-model.py

