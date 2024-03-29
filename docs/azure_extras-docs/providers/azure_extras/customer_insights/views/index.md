---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The view in Customer 360 web application. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, resourceGroupName, subscriptionId, userId, viewName` | Gets a view in the hub. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId, userId` | Gets all available views for given user in the specified hub. |
| `create_or_update` | `INSERT` | `hubName, resourceGroupName, subscriptionId, viewName` | Creates a view or updates an existing view in the hub. |
| `delete` | `DELETE` | `hubName, resourceGroupName, subscriptionId, userId, viewName` | Deletes a view in the specified hub. |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId, userId` | Gets all available views for given user in the specified hub. |
