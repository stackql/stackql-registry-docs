---
title: metrics_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_searches
  - metrics_searches
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
<tr><td><b>Name</b></td><td><code>metrics_searches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.metrics_searches.metrics_searches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the metrics search. |
| `description` | `string` | Item description in the content library. |
| `timeRange` | `object` |  |
| `desiredQuantizationInSecs` | `integer` | Desired quantization in seconds. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `title` | `string` | Item title in the content library. |
| `metricsQueries` | `array` | Metrics queries, up to the maximum of six. |
| `properties` | `string` | Chart properties, like line width, color palette, and the fill missing data method. Leave this field empty to use the defaults.<br />This property contains JSON object encoded as a string.<br /> |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `logQuery` | `string` | Log query used to add an overlay to the chart. |
| `parentId` | `string` | Identifier of the parent element in the content library, such as folder. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getMetricsSearch` | `SELECT` | `id, region` | Returns a metrics search with the specified identifier. |
| `createMetricsSearch` | `INSERT` | `region` | Saves a metrics search in the content library. Metrics search consists of one or more queries, a time range, a quantization period and a set of chart properties like line width. |
| `deleteMetricsSearch` | `DELETE` | `id, region` | Deletes a metrics search from the content library. |
| `updateMetricsSearch` | `EXEC` | `id, data__description, data__metricsQueries, data__timeRange, data__title, region` | Updates a metrics search with the specified identifier. Partial updates are not supported, you must provide values for all fields. |
