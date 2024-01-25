---
title: bookmarks
hide_title: false
hide_table_of_contents: false
keywords:
  - bookmarks
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
<tr><td><b>Name</b></td><td><code>bookmarks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.bookmarks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes bookmark properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Gets a bookmark. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all bookmarks. |
| `create_or_update` | `INSERT` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the bookmark. |
| `delete` | `DELETE` | `bookmarkId, resourceGroupName, subscriptionId, workspaceName` | Delete the bookmark. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all bookmarks. |
