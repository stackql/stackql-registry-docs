---
title: metrics_droplet_memory_available
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_droplet_memory_available
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

Creates, updates, deletes, gets or lists a <code>metrics_droplet_memory_available</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_droplet_memory_available</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_droplet_memory_available" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_droplet_memory_available_metrics" /> | `SELECT` | <CopyableCode code="end, host_id, start" /> | To retrieve available memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_available`. |

## `SELECT` examples

To retrieve available memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_available`.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_droplet_memory_available
WHERE end = '{{ end }}'
AND host_id = '{{ host_id }}'
AND start = '{{ start }}';
```