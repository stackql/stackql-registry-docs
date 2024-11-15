---
title: metrics_load_balancer_frontend_firewall_dropped_packets
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_load_balancer_frontend_firewall_dropped_packets
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

Creates, updates, deletes, gets or lists a <code>metrics_load_balancer_frontend_firewall_dropped_packets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_load_balancer_frontend_firewall_dropped_packets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_load_balancer_frontend_firewall_dropped_packets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_lb_frontend_firewall_dropped_packets" /> | `SELECT` | <CopyableCode code="end, lb_id, start" /> | To retrieve firewall dropped packets per second for a given load balancer, send a GET request to `/v2/monitoring/metrics/load_balancer/frontend_firewall_dropped_packets`. This is currently only supported for network load balancers. |

## `SELECT` examples

To retrieve firewall dropped packets per second for a given load balancer, send a GET request to `/v2/monitoring/metrics/load_balancer/frontend_firewall_dropped_packets`. This is currently only supported for network load balancers.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_load_balancer_frontend_firewall_dropped_packets
WHERE end = '{{ end }}'
AND lb_id = '{{ lb_id }}'
AND start = '{{ start }}';
```