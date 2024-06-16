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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the deployment. |
| <CopyableCode code="name" /> | `string` | The name of the deployment. |
| <CopyableCode code="location" /> | `string` | the location of the deployment. |
| <CopyableCode code="properties" /> | `object` | Deployment properties with additional details. |
| <CopyableCode code="tags" /> | `object` | Deployment tags |
| <CopyableCode code="type" /> | `string` | The type of the deployment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | Gets a deployment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the deployments for a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId, data__properties" /> | You can provide the template and parameters directly in the request or link to JSON files. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. Deleting a template deployment does not affect the state of the resource group. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| <CopyableCode code="calculate_template_hash" /> | `EXEC` |  | Calculate the hash of the given template. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resource group partially deployed. |
| <CopyableCode code="cancel_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="cancel_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="cancel_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="cancel_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName" /> | You can cancel a deployment only if the provisioningState is Accepted or Running. After the deployment is canceled, the provisioningState is set to Canceled. Canceling a template deployment stops the currently running template deployment and leaves the resources partially deployed. |
| <CopyableCode code="export_template" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId" /> | Exports the template used for specified deployment. |
| <CopyableCode code="export_template_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName" /> | Exports the template used for specified deployment. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId, data__location, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_scope" /> | `EXEC` | <CopyableCode code="deploymentName, scope, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="validate_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName, data__location, data__properties" /> | Validates whether the specified template is syntactically correct and will be accepted by Azure Resource Manager.. |
| <CopyableCode code="what_if" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the resource group. |
| <CopyableCode code="what_if_at_management_group_scope" /> | `EXEC` | <CopyableCode code="deploymentName, groupId, data__location, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the management group. |
| <CopyableCode code="what_if_at_subscription_scope" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the subscription. |
| <CopyableCode code="what_if_at_tenant_scope" /> | `EXEC` | <CopyableCode code="deploymentName, data__location, data__properties" /> | Returns changes that will be made by the deployment if executed at the scope of the tenant group. |
