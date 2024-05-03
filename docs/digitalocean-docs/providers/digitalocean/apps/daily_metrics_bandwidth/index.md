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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>daily_metrics_bandwidth</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.daily_metrics_bandwidth" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_bandwidth_usage" /> | `array` | A list of bandwidth usage details by app. |
| <CopyableCode code="date" /> | `string` | The date for the metrics data. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_metrics_bandwidth_daily" /> | `SELECT` | <CopyableCode code="app_id" /> | Retrieve daily bandwidth usage metrics for a single app. |
| <CopyableCode code="list_metrics_bandwidth_daily" /> | `EXEC` | <CopyableCode code="data__app_ids" /> | Retrieve daily bandwidth usage metrics for multiple apps. |
