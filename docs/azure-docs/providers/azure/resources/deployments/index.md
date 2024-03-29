---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - resources
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the deployment. |
| `name` | `string` | The name of the deployment. |
| `location` | `string` | the location of the deployment. |
| `properties` | `object` | Deployment properties with additional details. |
| `tags` | `object` | Deployment tags |
| `type` | `string` | The type of the deployment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` | Gets a deployment. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the deployments for a resource group. |
| `create_or_update` | `INSERT` | `deploymentName, resourceGroupName, subscriptionId, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `delete` | `DELETE` | `deploymentName, resourceGroupName, subscriptionId` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the deployments for a resource group. |
| `calculate_template_hash` | `EXEC` |  | Calculate the hash of the given template. |
| `cancel` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed. |
| `cancel_at_management_group_scope` | `EXEC` | `deploymentName, groupId` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `cancel_at_scope` | `EXEC` | `deploymentName, scope` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `cancel_at_subscription_scope` | `EXEC` | `deploymentName, subscriptionId` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `cancel_at_tenant_scope` | `EXEC` | `deploymentName` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `check_existence` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` | Checks whether the deployment exists. |
| `check_existence_at_management_group_scope` | `EXEC` | `deploymentName, groupId` | Checks whether the deployment exists. |
| `check_existence_at_scope` | `EXEC` | `deploymentName, scope` | Checks whether the deployment exists. |
| `check_existence_at_subscription_scope` | `EXEC` | `deploymentName, subscriptionId` | Checks whether the deployment exists. |
| `check_existence_at_tenant_scope` | `EXEC` | `deploymentName` | Checks whether the deployment exists. |
| `export_template` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` | Exports the template used for specified deployment. |
| `export_template_at_management_group_scope` | `EXEC` | `deploymentName, groupId` | Exports the template used for specified deployment. |
| `export_template_at_scope` | `EXEC` | `deploymentName, scope` | Exports the template used for specified deployment. |
| `export_template_at_subscription_scope` | `EXEC` | `deploymentName, subscriptionId` | Exports the template used for specified deployment. |
| `export_template_at_tenant_scope` | `EXEC` | `deploymentName` | Exports the template used for specified deployment. |
| `validate` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `validate_at_management_group_scope` | `EXEC` | `deploymentName, groupId, data__location, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `validate_at_scope` | `EXEC` | `deploymentName, scope, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `validate_at_subscription_scope` | `EXEC` | `deploymentName, subscriptionId, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `validate_at_tenant_scope` | `EXEC` | `deploymentName, data__location, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `what_if` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the resource group. |
| `what_if_at_management_group_scope` | `EXEC` | `deploymentName, groupId, data__location, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the management group. |
| `what_if_at_subscription_scope` | `EXEC` | `deploymentName, subscriptionId, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the subscription. |
| `what_if_at_tenant_scope` | `EXEC` | `deploymentName, data__location, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the tenant group. |
