---
title: metrics_droplet_filesystem_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_droplet_filesystem_sizes
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

Creates, updates, deletes, gets or lists a <code>metrics_droplet_filesystem_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_droplet_filesystem_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_droplet_filesystem_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_droplet_filesystem_size_metrics" /> | `SELECT` | <CopyableCode code="end, host_id, start" /> | To retrieve filesystem size metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_size`. |

## `SELECT` examples

To retrieve filesystem size metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_size`.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_droplet_filesystem_sizes
WHERE end = '{{ end }}'
AND host_id = '{{ host_id }}'
AND start = '{{ start }}';
```