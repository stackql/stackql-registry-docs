---
title: compute
hide_title: false
hide_table_of_contents: false
keywords:
  - compute
  - ml_services
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
<tr><td><b>Id</b></td><td><code>azure.ml_services.compute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` | Machine Learning compute object. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Gets compute definition by its name. Any secrets (storage keys, service credentials, etc) are not returned - use 'keys' nested resource to get them. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets computes in specified workspace. |
| `create_or_update` | `INSERT` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. If your intent is to create a new compute, do a GET first to verify that it does not exist yet. |
| `delete` | `DELETE` | `computeName, resourceGroupName, subscriptionId, underlyingResourceAction, workspaceName` | Deletes specified Machine Learning compute. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets computes in specified workspace. |
| `resize` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Updates the size of a Compute Instance. |
| `restart` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Posts a restart action to a compute instance |
| `start` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Posts a start action to a compute instance |
| `stop` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Posts a stop action to a compute instance |
| `update` | `EXEC` | `computeName, resourceGroupName, subscriptionId, workspaceName` | Updates properties of a compute. This call will overwrite a compute if it exists. This is a nonrecoverable operation. |
