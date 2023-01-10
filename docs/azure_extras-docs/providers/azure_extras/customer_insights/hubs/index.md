---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of hub. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Hubs_Get` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets information about the specified hub. |
| `Hubs_List` | `SELECT` | `subscriptionId` | Gets all hubs in the specified subscription. |
| `Hubs_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the hubs in a resource group. |
| `Hubs_CreateOrUpdate` | `INSERT` | `hubName, resourceGroupName, subscriptionId` | Creates a hub, or updates an existing hub. |
| `Hubs_Delete` | `DELETE` | `hubName, resourceGroupName, subscriptionId` | Deletes the specified hub. |
| `Hubs_Update` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Updates a Hub. |
