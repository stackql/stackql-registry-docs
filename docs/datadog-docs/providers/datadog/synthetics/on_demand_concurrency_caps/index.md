---
title: on_demand_concurrency_caps
hide_title: false
hide_table_of_contents: false
keywords:
  - on_demand_concurrency_caps
  - synthetics
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
<tr><td><b>Name</b></td><td><code>on_demand_concurrency_caps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.synthetics.on_demand_concurrency_caps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `attributes` | `object` | On-demand concurrency cap attributes. |
| `type` | `string` | On-demand concurrency cap type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_on_demand_concurrency_cap` | `SELECT` | `dd_site` | Get the on-demand concurrency cap. |
| `_get_on_demand_concurrency_cap` | `EXEC` | `dd_site` | Get the on-demand concurrency cap. |
| `set_on_demand_concurrency_cap` | `EXEC` | `dd_site` | Save new value for on-demand concurrency cap. |
