---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - postgresql
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Information describing the identities associated with this application. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a server. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets information about a server. |
| `list` | `SELECT` | `subscriptionId` | List all the servers in a given subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `create` | `INSERT` | `resourceGroupName, serverName, subscriptionId` | Creates a new server. |
| `delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `_list` | `EXEC` | `subscriptionId` | List all the servers in a given subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `restart` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Restarts a server. |
| `start` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Starts a server. |
| `stop` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Stops a server. |
| `update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
