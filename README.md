
# Azure Batch on Python Containers

A basic Python application that introduces Batch features such as pools, nodes, jobs, tasks, and interaction with Storage. Each task writes a text file to standard output.

For details and explanation, see the accompanying article [Run your first Batch job with the Python API](https://docs.microsoft.com/azure/batch/quick-run-python).

## Prerequisites

- Docker Desktop
- Python 2.7 or 3.3 or later including pip

## Resources

- [Azure Batch Explorer](https://azure.github.io/BatchExplorer/)
- [Azure Batch documentation](https://docs.microsoft.com/azure/batch/)
- [Azure Batch code samples](https://github.com/Azure/azure-batch-samples)

## Setup

First we must provision the necessary azure componenets to run the solution.  This includes creating the Azure Batch endpoint, and an Azure Container Registry to store our docker containers.

### Get the code

First clone this repo so you'll have the necessary code to complete subsequent steps.

### Provision Azure Batch

1. In the Azure Portal select "Create a Resource".
1. Type "Batch Service" in the "Search the Marketplace" dialogue.
1. Select "Batch Service" from the results, and click "Create".
1. Fill out the details for a new or existing resoruce group, and give your batch service a name.
1. Create a new storage account to associate with your batch service in the same region.
1. Finish the steps with the defaults to create the new batch service.

### Provision an Azure Container Registry

1. In the Azure Portal select "Create a Resource"
1. Type "Container Registry" in the "Search the Marketplace" dialogue.
1. Choose the Microsoft "Container Registry" result, and click "Create".
1. Select the resource group you created when provisioning Azure Batch, and give your container registry a name.
1. Finish the creation steps by accepting the defaults.
1. Once the container registry is created, navigate to the resource's "Access Keys" settings, and turn on the "Admin user".  This user will be leveraged for publishing a new container and retreiving containers by the batch service.
1. Make note of your Registry Name, Login Server, Username, and password values, you'll need these for the next step.

### Build, test, and deploy the container

1. Open a command prompt and navigate to the python-container directory of your cloned solution.
1. First lets tag and build the container image with the following command.  (Don't forget to replace the <> values from your container registry)
    ```
    docker build -t <login server>/<registry name>/is_prime:latest .
    ```
3. Now we'll test the container is working appropriately leveraging the -it command to interactively run the python script.  (Again, pay attention to the <> placeholders)
    ```
    docker run -it <login server>/<registry name>/is_prime python is_prime.py <url to file>
    ```
4. Now we need to connect to the created container registry and publish the container image.
    ```
    docker login <login server> --username <username> --password <password>
    docker push <login server>/<registry name>/is_prime
    ```

### Execute the Batch process

1. In the batch-driver folder, edit the config.py file to have the appropriate values for your Azure Batch and Azure Container Registry.
1. Exexcute the batch-driver.py python script.  (Note: this was tested using VS Code, but there are many ways to run python including the cli)
1. If you opted to install Batch Explorer, you can use it to monitor the state of your batch pool, batch job, and individual tasks.

