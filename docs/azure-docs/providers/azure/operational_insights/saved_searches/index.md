---
title: saved_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_searches
  - operational_insights
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
<tr><td><b>Id</b></td><td><code>azure.operational_insights.saved_searches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag |
| `properties` | `object` | Value object for saved search results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SavedSearches_Get` | `SELECT` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Gets the specified saved search for a given workspace. |
| `SavedSearches_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the saved searches for a given Log Analytics Workspace |
| `SavedSearches_CreateOrUpdate` | `INSERT` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName, data__properties` | Creates or updates a saved search for a given workspace. |
| `SavedSearches_Delete` | `DELETE` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Deletes the specified saved search in a given workspace. |
