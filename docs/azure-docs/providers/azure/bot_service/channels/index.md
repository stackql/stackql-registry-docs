---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bot_service.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Channel definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `channelName, resourceGroupName, resourceName, subscriptionId` | Returns a BotService Channel registration specified by the parameters. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns all the Channel registrations of a particular BotService resource |
| `create` | `INSERT` | `channelName, resourceGroupName, resourceName, subscriptionId` | Creates a Channel registration for a Bot Service |
| `delete` | `DELETE` | `channelName, resourceGroupName, resourceName, subscriptionId` | Deletes a Channel registration from a Bot Service |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns all the Channel registrations of a particular BotService resource |
| `update` | `EXEC` | `channelName, resourceGroupName, resourceName, subscriptionId` | Updates a Channel registration for a Bot Service |
