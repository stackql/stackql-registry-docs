---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - bot_service
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.bot_service.bots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `type` | `string` | Specifies the type of the resource. |
| `properties` | `object` | The parameters to provide for the Bot. |
| `etag` | `string` | Entity Tag |
| `kind` | `string` | Indicates the type of bot service |
| `location` | `string` | Specifies the location of the resource. |
| `sku` | `object` | The SKU of the cognitive services account. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `zones` | `array` | Entity zones |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Bots_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns a BotService specified by the parameters. |
| `Bots_List` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `Bots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `Bots_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates a Bot Service. Bot Service is a resource group wide resource type. |
| `Bots_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a Bot Service from the resource group.  |
| `Bots_GetCheckNameAvailability` | `EXEC` |  | Check whether a bot name is available. |
| `Bots_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a Bot Service |
