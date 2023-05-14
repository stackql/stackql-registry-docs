---
title: stats
hide_title: false
hide_table_of_contents: false
keywords:
  - stats
  - instances
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.stats</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `title` | `string` | The title for this data set. |
| `cpu` | `array` | Percentage of CPU used.<br /> |
| `io` | `object` | Input/Output statistics. |
| `netv4` | `object` | IPv4 statistics. |
| `netv6` | `object` | IPv6 statistics. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLinodeStats` | `SELECT` | `linodeId` | Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours.<br /> |
| `getLinodeStatsByYearMonth` | `SELECT` | `linodeId, month, year` | Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days.<br /> |
| `_getLinodeStats` | `EXEC` | `linodeId` | Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours.<br /> |
| `_getLinodeStatsByYearMonth` | `EXEC` | `linodeId, month, year` | Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days.<br /> |
