---
title: links
hide_title: false
hide_table_of_contents: false
keywords:
  - links
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
<tr><td><b>Name</b></td><td><code>links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The definition of Link. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, linkName, resourceGroupName, subscriptionId` | Gets a link in the hub. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all the links in the specified hub. |
| `create_or_update` | `INSERT` | `hubName, linkName, resourceGroupName, subscriptionId` | Creates a link or updates an existing link in the hub. |
| `delete` | `DELETE` | `hubName, linkName, resourceGroupName, subscriptionId` | Deletes a link in the hub. |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Gets all the links in the specified hub. |
