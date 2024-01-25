---
title: saved_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_searches
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>saved_searches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.saved_searches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag |
| `properties` | `object` | Value object for saved search results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Gets the specified saved search for a given workspace. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the saved searches for a given Log Analytics Workspace |
| `create_or_update` | `INSERT` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName, data__properties` | Creates or updates a saved search for a given workspace. |
| `delete` | `DELETE` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Deletes the specified saved search in a given workspace. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets the saved searches for a given Log Analytics Workspace |
