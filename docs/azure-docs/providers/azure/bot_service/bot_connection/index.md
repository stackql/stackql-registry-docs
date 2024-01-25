---
title: bot_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_connection
  - bot_service
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
<tr><td><b>Name</b></td><td><code>bot_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bot_service.bot_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties for a Connection Setting Item |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Get a Connection Setting registration for a Bot Service |
| `list_by_bot_service` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns all the Connection Settings registered to a particular BotService resource |
| `create` | `INSERT` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Register a new Auth Connection for a Bot Service |
| `delete` | `DELETE` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Deletes a Connection Setting registration for a Bot Service |
| `_list_by_bot_service` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns all the Connection Settings registered to a particular BotService resource |
| `update` | `EXEC` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Updates a Connection Setting registration for a Bot Service |
