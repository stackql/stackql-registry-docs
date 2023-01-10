---
title: bot_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_connection
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
<tr><td><b>Name</b></td><td><code>bot_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.bot_service.bot_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `zones` | `array` | Entity zones |
| `etag` | `string` | Entity Tag |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `properties` | `object` | Properties for a Connection Setting Item |
| `type` | `string` | Specifies the type of the resource. |
| `kind` | `string` | Indicates the type of bot service |
| `location` | `string` | Specifies the location of the resource. |
| `sku` | `object` | The SKU of the cognitive services account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BotConnection_Get` | `SELECT` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Get a Connection Setting registration for a Bot Service |
| `BotConnection_ListByBotService` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns all the Connection Settings registered to a particular BotService resource |
| `BotConnection_Create` | `INSERT` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Register a new Auth Connection for a Bot Service |
| `BotConnection_Delete` | `DELETE` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Deletes a Connection Setting registration for a Bot Service |
| `BotConnection_ListServiceProviders` | `EXEC` | `subscriptionId` | Lists the available Service Providers for creating Connection Settings |
| `BotConnection_ListWithSecrets` | `EXEC` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Get a Connection Setting registration for a Bot Service |
| `BotConnection_Update` | `EXEC` | `connectionName, resourceGroupName, resourceName, subscriptionId` | Updates a Connection Setting registration for a Bot Service |
