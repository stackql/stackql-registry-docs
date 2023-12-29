---
title: hourly_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - hourly_usages
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
<tr><td><b>Name</b></td><td><code>hourly_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.usage_metering.hourly_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the response. |
| `attributes` | `object` | Attributes of hourly usage for a product family for an org for a time period. |
| `type` | `string` | Type of usage data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_hourly_usage` | `SELECT` | `filter[product_families], filter[timestamp][start], dd_site` |
| `_get_hourly_usage` | `EXEC` | `filter[product_families], filter[timestamp][start], dd_site` |
