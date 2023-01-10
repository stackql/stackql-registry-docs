---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.bot_service.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `sku` | `object` | The SKU of the cognitive services account. |
| `zones` | `array` | Entity zones |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `kind` | `string` | Indicates the type of bot service |
| `etag` | `string` | Entity Tag |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` | Channel definition |
| `type` | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Channels_Get` | `SELECT` | `channelName, resourceGroupName, resourceName, subscriptionId` | Returns a BotService Channel registration specified by the parameters. |
| `Channels_ListByResourceGroup` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns all the Channel registrations of a particular BotService resource |
| `Channels_Create` | `INSERT` | `channelName, resourceGroupName, resourceName, subscriptionId` | Creates a Channel registration for a Bot Service |
| `Channels_Delete` | `DELETE` | `channelName, resourceGroupName, resourceName, subscriptionId` | Deletes a Channel registration from a Bot Service |
| `Channels_ListWithKeys` | `EXEC` | `channelName, resourceGroupName, resourceName, subscriptionId` | Lists a Channel registration for a Bot Service including secrets |
| `Channels_Update` | `EXEC` | `channelName, resourceGroupName, resourceName, subscriptionId` | Updates a Channel registration for a Bot Service |
