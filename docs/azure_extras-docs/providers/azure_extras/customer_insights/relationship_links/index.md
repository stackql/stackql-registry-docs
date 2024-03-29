---
title: relationship_links
hide_title: false
hide_table_of_contents: false
keywords:
  - relationship_links
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
<tr><td><b>Name</b></td><td><code>relationship_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.relationship_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The definition of relationship link. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, relationshipLinkName, resourceGroupName, subscriptionId` | Gets information about the specified relationship Link. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all relationship links in the hub. |
| `create_or_update` | `INSERT` | `hubName, relationshipLinkName, resourceGroupName, subscriptionId` | Creates a relationship link or updates an existing relationship link within a hub. |
| `delete` | `DELETE` | `hubName, relationshipLinkName, resourceGroupName, subscriptionId` | Deletes a relationship link within a hub. |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Gets all relationship links in the hub. |
