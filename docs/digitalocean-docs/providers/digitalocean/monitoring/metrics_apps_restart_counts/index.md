---
title: metrics_apps_restart_counts
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_apps_restart_counts
  - monitoring
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

Creates, updates, deletes, gets or lists a <code>metrics_apps_restart_counts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_apps_restart_counts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_apps_restart_counts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_app_restart_count_metrics_yml" /> | `SELECT` | <CopyableCode code="app_id, end, start" /> | To retrieve restart count metrics for a given app, send a GET request to `/v2/monitoring/metrics/apps/restart_count`. |

## `SELECT` examples

To retrieve restart count metrics for a given app, send a GET request to `/v2/monitoring/metrics/apps/restart_count`.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_apps_restart_counts
WHERE app_id = '{{ app_id }}'
AND end = '{{ end }}'
AND start = '{{ start }}';
```