---
title: scalar_data
hide_title: false
hide_table_of_contents: false
keywords:
  - scalar_data
  - metrics
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalar_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.metrics.scalar_data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `data` | `object` | A message containing the response to a scalar query. |
| `errors` | `string` | An error generated when processing a request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `query_scalar_data` | `SELECT` | `data__data, dd_site` |
