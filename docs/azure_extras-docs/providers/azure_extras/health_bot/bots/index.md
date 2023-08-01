---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - health_bot
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
<tr><td><b>Id</b></td><td><code>azure_extras.health_bot.bots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a Azure Health Bot. The Health Bot Service is a cloud platform that empowers developers in Healthcare organizations to build and deploy their compliant, AI-powered virtual health assistants and health bots, that help them improve processes and reduce costs. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Bots_Get` | `SELECT` | `botName, resourceGroupName, subscriptionId` | Get a HealthBot. |
| `Bots_List` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `Bots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `Bots_Create` | `INSERT` | `botName, resourceGroupName, subscriptionId, data__sku` | Create a new Azure Health Bot. |
| `Bots_Delete` | `DELETE` | `botName, resourceGroupName, subscriptionId` | Delete a HealthBot. |
| `Bots_Update` | `EXEC` | `botName, resourceGroupName, subscriptionId` | Patch a HealthBot. |
