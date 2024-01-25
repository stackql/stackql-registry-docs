---
title: watchlist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlist_items
  - sentinel
  - azure    
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
<tr><td><b>Name</b></td><td><code>watchlist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.watchlist_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes watchlist item properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName` | Get a watchlist item. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Get all watchlist Items. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName` | Create or update a watchlist item. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName` | Delete a watchlist item. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Get all watchlist Items. |
