---
title: spanquery
hide_title: false
hide_table_of_contents: false
keywords:
  - spanquery
  - tracing
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spanquery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.spanquery</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `createSpanQuery` | `INSERT` | `data__queryRows, data__timeRange` | Execute a span analytics query and get the id to fetch its status and results. Use the [Span Query Status](#operation/getSpanQueryStatus) endpoint to check a query status. When the query has been completed, use the [Span Query Result](#operation/getSpanQueryResult) endpoint to get the result of the asynchronous query. |
| `cancelSpanQuery` | `EXEC` | `queryId` | Cancel a currently processed span search query with the given id. |
