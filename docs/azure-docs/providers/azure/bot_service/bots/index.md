---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
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
<tr><td><b>Name</b></td><td><code>bots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bot_service.bots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The parameters to provide for the Bot. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns a BotService specified by the parameters. |
| `list` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates a Bot Service. Bot Service is a resource group wide resource type. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a Bot Service from the resource group.  |
| `_list` | `EXEC` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a Bot Service |
