---
title: metrics_droplet_load_1s
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_droplet_load_1s
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

Creates, updates, deletes, gets or lists a <code>metrics_droplet_load_1s</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_droplet_load_1s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_droplet_load_1s" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_droplet_load1metrics" /> | `SELECT` | <CopyableCode code="end, host_id, start" /> | To retrieve 1 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_1`. |

## `SELECT` examples

To retrieve 1 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_1`.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_droplet_load_1s
WHERE end = '{{ end }}'
AND host_id = '{{ host_id }}'
AND start = '{{ start }}';
```