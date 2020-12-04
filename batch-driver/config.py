# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "

_BATCH_ACCOUNT_NAME = '<batch account>'  # Your batch account name
_BATCH_ACCOUNT_KEY = '<batch key>'  # Your batch account key
_BATCH_ACCOUNT_URL = '<batch url>'  # Your batch account URL
_STORAGE_CONNSTR = '<storage connection string>'  # Your storage connection string
_STORAGE_KEY = '<storage key>'
_POOL_ID = 'PrimeNumberPool'  # Your Pool ID
_POOL_NODE_COUNT = 2  # Pool node count
_POOL_VM_SIZE = 'STANDARD_A2'  # VM Type/Size
_JOB_ID = 'PrimeNumberJob'  # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file

_REGISTRY_USER_NAME = '<username>'
_REGISTRY_PASSWORD = '<password>'
_REGISTRY_SERVER = '<login server>'
_DOCKER_IMAGE = '<login server>/<registry name>/is_prime:latest'
