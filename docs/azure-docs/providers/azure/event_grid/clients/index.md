---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
  - event_grid
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
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.clients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of client. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clientName, namespaceName, resourceGroupName, subscriptionId` | Get properties of a client. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Get all the permission bindings under a namespace. |
| `create_or_update` | `INSERT` | `clientName, namespaceName, resourceGroupName, subscriptionId` | Create or update a client with the specified parameters. |
| `delete` | `DELETE` | `clientName, namespaceName, resourceGroupName, subscriptionId` | Delete an existing client. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Get all the permission bindings under a namespace. |
