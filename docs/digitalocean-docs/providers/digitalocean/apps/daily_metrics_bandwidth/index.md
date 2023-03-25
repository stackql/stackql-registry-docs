---
title: daily_metrics_bandwidth
hide_title: false
hide_table_of_contents: false
keywords:
  - daily_metrics_bandwidth
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>daily_metrics_bandwidth</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.daily_metrics_bandwidth</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `app_bandwidth_usage` | `array` | A list of bandwidth usage details by app. |
| `date` | `string` | The date for the metrics data. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_metrics_bandwidth_daily` | `SELECT` | `app_id` | Retrieve daily bandwidth usage metrics for a single app. |
| `list_metrics_bandwidth_daily` | `EXEC` | `data__app_ids` | Retrieve daily bandwidth usage metrics for multiple apps. |
