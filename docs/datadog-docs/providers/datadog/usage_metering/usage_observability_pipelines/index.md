---
title: usage_observability_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_observability_pipelines
  - usage_metering
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
<tr><td><b>Name</b></td><td><code>usage_observability_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.usage_metering.usage_observability_pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the response. |
| `attributes` | `object` | Usage attributes data. |
| `type` | `string` | Type of usage data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_usage_observability_pipelines` | `SELECT` | `start_hr, dd_site` |
| `_get_usage_observability_pipelines` | `EXEC` | `start_hr, dd_site` |
