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
| `Deployments_Get` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` | Gets a deployment. |
| `Deployments_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the deployments for a resource group. |
| `Deployments_CreateOrUpdate` | `INSERT` | `deploymentName, resourceGroupName, subscriptionId, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `Deployments_Delete` | `DELETE` | `deploymentName, resourceGroupName, subscriptionId` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `Deployments_CalculateTemplateHash` | `EXEC` |  | Calculate the hash of the given template. |
| `Deployments_Cancel` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed. |
| `Deployments_CancelAtManagementGroupScope` | `EXEC` | `deploymentName, groupId` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `Deployments_CancelAtScope` | `EXEC` | `deploymentName, scope` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `Deployments_CancelAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `Deployments_CancelAtTenantScope` | `EXEC` | `deploymentName` | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| `Deployments_CheckExistence` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` | Checks whether the deployment exists. |
| `Deployments_CheckExistenceAtManagementGroupScope` | `EXEC` | `deploymentName, groupId` | Checks whether the deployment exists. |
| `Deployments_CheckExistenceAtScope` | `EXEC` | `deploymentName, scope` | Checks whether the deployment exists. |
| `Deployments_CheckExistenceAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId` | Checks whether the deployment exists. |
| `Deployments_CheckExistenceAtTenantScope` | `EXEC` | `deploymentName` | Checks whether the deployment exists. |
| `Deployments_CreateOrUpdateAtManagementGroupScope` | `EXEC` | `deploymentName, groupId, data__location, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `Deployments_CreateOrUpdateAtScope` | `EXEC` | `deploymentName, scope, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `Deployments_CreateOrUpdateAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `Deployments_CreateOrUpdateAtTenantScope` | `EXEC` | `deploymentName, data__location, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `Deployments_DeleteAtManagementGroupScope` | `EXEC` | `deploymentName, groupId` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `Deployments_DeleteAtScope` | `EXEC` | `deploymentName, scope` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `Deployments_DeleteAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `Deployments_DeleteAtTenantScope` | `EXEC` | `deploymentName` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `Deployments_ExportTemplate` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` | Exports the template used for specified deployment. |
| `Deployments_ExportTemplateAtManagementGroupScope` | `EXEC` | `deploymentName, groupId` | Exports the template used for specified deployment. |
| `Deployments_ExportTemplateAtScope` | `EXEC` | `deploymentName, scope` | Exports the template used for specified deployment. |
| `Deployments_ExportTemplateAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId` | Exports the template used for specified deployment. |
| `Deployments_ExportTemplateAtTenantScope` | `EXEC` | `deploymentName` | Exports the template used for specified deployment. |
| `Deployments_GetAtManagementGroupScope` | `EXEC` | `deploymentName, groupId` | Gets a deployment. |
| `Deployments_GetAtScope` | `EXEC` | `deploymentName, scope` | Gets a deployment. |
| `Deployments_GetAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId` | Gets a deployment. |
| `Deployments_GetAtTenantScope` | `EXEC` | `deploymentName` | Gets a deployment. |
| `Deployments_ListAtManagementGroupScope` | `EXEC` | `groupId` | Get all the deployments for a management group. |
| `Deployments_ListAtScope` | `EXEC` | `scope` | Get all the deployments at the given scope. |
| `Deployments_ListAtSubscriptionScope` | `EXEC` | `subscriptionId` | Get all the deployments for a subscription. |
| `Deployments_ListAtTenantScope` | `EXEC` |  | Get all the deployments at the tenant scope. |
| `Deployments_Validate` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `Deployments_ValidateAtManagementGroupScope` | `EXEC` | `deploymentName, groupId, data__location, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `Deployments_ValidateAtScope` | `EXEC` | `deploymentName, scope, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `Deployments_ValidateAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `Deployments_ValidateAtTenantScope` | `EXEC` | `deploymentName, data__location, data__properties` | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| `Deployments_WhatIf` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the resource group. |
| `Deployments_WhatIfAtManagementGroupScope` | `EXEC` | `deploymentName, groupId, data__location, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the management group. |
| `Deployments_WhatIfAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the subscription. |
| `Deployments_WhatIfAtTenantScope` | `EXEC` | `deploymentName, data__location, data__properties` | Returns changes that will be made by the deployment if executed at the scope of the tenant group. |
