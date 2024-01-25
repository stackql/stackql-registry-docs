---
title: query_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - query_keys
  - search
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
<tr><td><b>Name</b></td><td><code>query_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.search.query_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Request URL that can be used to query next page of query keys. Returned when the total number of requested query keys exceed maximum page size. |
| `value` | `array` | The query keys for the search service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_search_service` | `SELECT` | `resourceGroupName, searchServiceName, subscriptionId` | Returns the list of query API keys for the given search service. |
| `create` | `INSERT` | `name, resourceGroupName, searchServiceName, subscriptionId` | Generates a new query key for the specified search service. You can create up to 50 query keys per service. |
| `delete` | `DELETE` | `key, resourceGroupName, searchServiceName, subscriptionId` | Deletes the specified query key. Unlike admin keys, query keys are not regenerated. The process for regenerating a query key is to delete and then recreate it. |
