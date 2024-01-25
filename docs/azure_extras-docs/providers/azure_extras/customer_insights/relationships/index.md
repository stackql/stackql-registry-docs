---
title: relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - relationships
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
<tr><td><b>Name</b></td><td><code>relationships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.relationships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The definition of Relationship. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, relationshipName, resourceGroupName, subscriptionId` | Gets information about the specified relationship. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all relationships in the hub. |
| `create_or_update` | `INSERT` | `hubName, relationshipName, resourceGroupName, subscriptionId` | Creates a relationship or updates an existing relationship within a hub. |
| `delete` | `DELETE` | `hubName, relationshipName, resourceGroupName, subscriptionId` | Deletes a relationship within a hub. |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Gets all relationships in the hub. |
