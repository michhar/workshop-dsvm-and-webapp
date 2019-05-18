
"""
Based upon:  https://github.com/Azure-Samples/resource-manager-python-template-deployment
"""

import os.path
from deployer import Deployer
from haikunator import Haikunator


# This script expects that the following environment vars are set:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret
# VM_USER: a VM user name to use
# AZURE_SUBSCRIPTION_ID: Azure subscription ID

my_subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')   # your Azure Subscription Id
my_resource_group = 'azure-python-deployment-sample'            # the resource group for deployment
my_admin_user = os.getenv('VM_USER', 'superwoman') # admin name
print('Take note of the admin user: ', my_admin_user)
# Create a random password with Haikunator
passwd_generator = Haikunator()
passwd = passwd_generator.haikunate() 
my_user_password = os.getenv('VM_PASSWORD', passwd)
print('Take note of the admin password: ', my_user_password)

msg = "\nInitializing the Deployer class with subscription id: {}, resource group: {}" \
    "\nand public key located at: {}...\n\n"
msg = msg.format(my_subscription_id, my_resource_group, my_admin_user, my_user_password)
print(msg)

# Initialize the deployer class
deployer = Deployer(my_subscription_id, my_resource_group, my_admin_user, my_user_password)

print("Beginning the deployment... \n\n")
# Deploy the template
my_deployment = deployer.deploy()

print("Done deploying!!\n\nYou can connect via: `ssh {}@{}.westus2.cloudapp.azure.com`".format(
    my_admin_user, deployer.dns_label_prefix))

# Destroy the resource group which contains the deployment
# deployer.destroy()