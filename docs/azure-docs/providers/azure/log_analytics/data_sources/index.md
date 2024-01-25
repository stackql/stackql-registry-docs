---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
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
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.data_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag of the data source. |
| `kind` | `string` | The kind of the DataSource. |
| `properties` | `object` | JSON object |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataSourceName, resourceGroupName, subscriptionId, workspaceName` | Gets a datasource instance. |
| `list_by_workspace` | `SELECT` | `$filter, resourceGroupName, subscriptionId, workspaceName` | Gets the first page of data source instances in a workspace with the link to the next page. |
| `create_or_update` | `INSERT` | `dataSourceName, resourceGroupName, subscriptionId, workspaceName, data__kind, data__properties` | Create or update a data source. |
| `delete` | `DELETE` | `dataSourceName, resourceGroupName, subscriptionId, workspaceName` | Deletes a data source instance. |
| `_list_by_workspace` | `EXEC` | `$filter, resourceGroupName, subscriptionId, workspaceName` | Gets the first page of data source instances in a workspace with the link to the next page. |
