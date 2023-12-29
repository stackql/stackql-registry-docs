---
title: cost_by_orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_by_orgs
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
<tr><td><b>Name</b></td><td><code>cost_by_orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.usage_metering.cost_by_orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the response. |
| `attributes` | `object` | Cost attributes data. |
| `type` | `string` | Type of cost data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_cost_by_org` | `SELECT` | `start_month, dd_site` |
| `_get_cost_by_org` | `EXEC` | `start_month, dd_site` |
