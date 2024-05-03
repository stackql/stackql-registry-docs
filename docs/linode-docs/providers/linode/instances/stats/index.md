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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cpu" /> | `array` | Percentage of CPU used.<br /> |
| <CopyableCode code="io" /> | `object` | Input/Output statistics. |
| <CopyableCode code="netv4" /> | `object` | IPv4 statistics. |
| <CopyableCode code="netv6" /> | `object` | IPv6 statistics. |
| <CopyableCode code="title" /> | `string` | The title for this data set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLinodeStats" /> | `SELECT` | <CopyableCode code="linodeId" /> | Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours.<br /> |
| <CopyableCode code="getLinodeStatsByYearMonth" /> | `SELECT` | <CopyableCode code="linodeId, month, year" /> | Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days.<br /> |
| <CopyableCode code="_getLinodeStats" /> | `EXEC` | <CopyableCode code="linodeId" /> | Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours.<br /> |
| <CopyableCode code="_getLinodeStatsByYearMonth" /> | `EXEC` | <CopyableCode code="linodeId, month, year" /> | Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days.<br /> |
