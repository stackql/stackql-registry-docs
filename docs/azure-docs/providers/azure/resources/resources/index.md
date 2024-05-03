---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
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
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the resource. |
| <CopyableCode code="managedBy" /> | `string` | ID of the resource that manages this resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | The resource properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Gets a resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the resources in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the resources for a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Creates a resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Deletes a resource. |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="api-version, resourceId" /> | Deletes a resource by ID. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get all the resources in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the resources for a resource group. |
| <CopyableCode code="check_existence" /> | `EXEC` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Checks whether a resource exists. |
| <CopyableCode code="check_existence_by_id" /> | `EXEC` | <CopyableCode code="api-version, resourceId" /> | Checks by ID whether a resource exists. This API currently works only for a limited set of Resource providers. In the event that a Resource provider does not implement this API, ARM will respond with a 405. The alternative then is to use the GET API to check for the existence of the resource. |
| <CopyableCode code="create_or_update_by_id" /> | `EXEC` | <CopyableCode code="api-version, resourceId" /> | Create a resource by ID. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="api-version, resourceId" /> | Gets a resource by ID. |
| <CopyableCode code="move_resources" /> | `EXEC` | <CopyableCode code="sourceResourceGroupName, subscriptionId" /> | The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes.  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Updates a resource. |
| <CopyableCode code="update_by_id" /> | `EXEC` | <CopyableCode code="api-version, resourceId" /> | Updates a resource by ID. |
| <CopyableCode code="validate_move_resources" /> | `EXEC` | <CopyableCode code="sourceResourceGroupName, subscriptionId" /> | This operation checks whether the specified resources can be moved to the target. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation. |
