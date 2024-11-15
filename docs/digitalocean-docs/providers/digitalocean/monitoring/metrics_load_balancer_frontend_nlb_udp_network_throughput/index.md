---
title: metrics_load_balancer_frontend_nlb_udp_network_throughput
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_load_balancer_frontend_nlb_udp_network_throughput
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

Creates, updates, deletes, gets or lists a <code>metrics_load_balancer_frontend_nlb_udp_network_throughput</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_load_balancer_frontend_nlb_udp_network_throughput</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_load_balancer_frontend_nlb_udp_network_throughput" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_lb_frontend_nlb_udp_network_throughput" /> | `SELECT` | <CopyableCode code="end, lb_id, start" /> | To retrieve frontend UDP throughput in bytes per second for a given load balancer, send a GET request to `/v2/monitoring/metrics/load_balancer/frontend_nlb_udp_network_throughput`. |

## `SELECT` examples

To retrieve frontend UDP throughput in bytes per second for a given load balancer, send a GET request to `/v2/monitoring/metrics/load_balancer/frontend_nlb_udp_network_throughput`.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_load_balancer_frontend_nlb_udp_network_throughput
WHERE end = '{{ end }}'
AND lb_id = '{{ lb_id }}'
AND start = '{{ start }}';
```