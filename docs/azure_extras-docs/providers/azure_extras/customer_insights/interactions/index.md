---
title: interactions
hide_title: false
hide_table_of_contents: false
keywords:
  - interactions
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
<tr><td><b>Name</b></td><td><code>interactions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.interactions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The Interaction Type Definition |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, interactionName, resourceGroupName, subscriptionId` | Gets information about the specified interaction. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all interactions in the hub. |
| `create_or_update` | `INSERT` | `hubName, interactionName, resourceGroupName, subscriptionId` | Creates an interaction or updates an existing interaction within a hub. |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Gets all interactions in the hub. |
| `suggest_relationship_links` | `EXEC` | `hubName, interactionName, resourceGroupName, subscriptionId` | Suggests relationships to create relationship links. |
