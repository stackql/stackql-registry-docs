---
title: watchlists
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlists
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
<tr><td><b>Name</b></td><td><code>watchlists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.watchlists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes watchlist properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Get a watchlist, without its watchlist items. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get all watchlists, without watchlist items. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, watchlistAlias, workspaceName` | Delete a watchlist. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Get all watchlists, without watchlist items. |
