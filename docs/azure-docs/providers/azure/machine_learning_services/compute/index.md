---
title: compute
hide_title: false
hide_table_of_contents: false
keywords:
  - compute
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>compute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.compute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | Machine Learning compute object. |
| `location` | `string` | Specifies the location of the resource. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `sku` | `object` | The resource model definition representing SKU |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Compute_Get` | `SELECT` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use 'keys' nested resource to get them. |
| `Compute_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets computes in specified workspace. |
| `Compute_CreateOrUpdate` | `INSERT` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet. |
| `Compute_Delete` | `DELETE` | `computeName, resourceGroupName, subscriptionId, underlyingResourceAction, workspaceName` | Deletes specified Machine Learning compute. |
| `Compute_ListKeys` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Gets secrets related to Machine Learning compute (storage keys, service credentials, etc). |
| `Compute_ListNodes` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Get the details (e.g IP address, port etc) of all the compute nodes in the compute. |
| `Compute_Restart` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Posts a restart action to a compute instance |
| `Compute_Start` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Posts a start action to a compute instance |
| `Compute_Stop` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Posts a stop action to a compute instance |
| `Compute_Update` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. |
| `Compute_UpdateCustomServices` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Updates the custom services list. The list of custom services provided shall be overwritten |
| `Compute_UpdateIdleShutdownSetting` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Updates the idle shutdown setting of a compute instance. |
