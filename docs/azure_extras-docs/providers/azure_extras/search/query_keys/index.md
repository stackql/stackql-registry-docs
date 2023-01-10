---
title: query_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - query_keys
  - search
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
<tr><td><b>Name</b></td><td><code>query_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.search.query_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `array` | The query keys for the Azure Cognitive Search service. |
| `nextLink` | `string` | Request URL that can be used to query next page of query keys. Returned when the total number of requested query keys exceed maximum page size. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `QueryKeys_ListBySearchService` | `SELECT` | `resourceGroupName, searchServiceName, subscriptionId` | Returns the list of query API keys for the given Azure Cognitive Search service. |
| `QueryKeys_Create` | `INSERT` | `name, resourceGroupName, searchServiceName, subscriptionId` | Generates a new query key for the specified search service. You can create up to 50 query keys per service. |
| `QueryKeys_Delete` | `DELETE` | `key, resourceGroupName, searchServiceName, subscriptionId` | Deletes the specified query key. Unlike admin keys, query keys are not regenerated. The process for regenerating a query key is to delete and then recreate it. |
