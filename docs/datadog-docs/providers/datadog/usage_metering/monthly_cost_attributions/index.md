---
title: monthly_cost_attributions
hide_title: false
hide_table_of_contents: false
keywords:
  - monthly_cost_attributions
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
<tr><td><b>Name</b></td><td><code>monthly_cost_attributions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.usage_metering.monthly_cost_attributions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the response. |
| `attributes` | `object` | Cost Attribution by Tag for a given organization. |
| `type` | `string` | Type of cost attribution data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_monthly_cost_attribution` | `SELECT` | `end_month, fields, start_month, dd_site` |
| `_get_monthly_cost_attribution` | `EXEC` | `end_month, fields, start_month, dd_site` |
