---
title: entity_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_queries
  - security_insights
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
<tr><td><b>Name</b></td><td><code>entity_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.entity_queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the entity query |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EntityQueries_Get` | `SELECT` | `entityQueryId, resourceGroupName, subscriptionId, workspaceName` | Gets an entity query. |
| `EntityQueries_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all entity queries. |
| `EntityQueries_CreateOrUpdate` | `INSERT` | `entityQueryId, resourceGroupName, subscriptionId, workspaceName, data__kind` | Creates or updates the entity query. |
| `EntityQueries_Delete` | `DELETE` | `entityQueryId, resourceGroupName, subscriptionId, workspaceName` | Delete the entity query. |
