---
title: daily_metrics_bandwidths
hide_title: false
hide_table_of_contents: false
keywords:
  - daily_metrics_bandwidths
  - apps
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>daily_metrics_bandwidths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>daily_metrics_bandwidths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.daily_metrics_bandwidths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_bandwidth_usage" /> | `array` | A list of bandwidth usage details by app. |
| <CopyableCode code="date" /> | `string` | The date for the metrics data. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apps_get_metrics_bandwidth_daily" /> | `SELECT` | <CopyableCode code="app_id" /> | Retrieve daily bandwidth usage metrics for a single app. |
| <CopyableCode code="apps_list_metrics_bandwidth_daily" /> | `SELECT` | <CopyableCode code="data__app_ids" /> | Retrieve daily bandwidth usage metrics for multiple apps. |

## `SELECT` examples

Retrieve daily bandwidth usage metrics for a single app.


```sql
SELECT
app_bandwidth_usage,
date
FROM digitalocean.apps.daily_metrics_bandwidths
WHERE app_id = '{{ app_id }}';
```