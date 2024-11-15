---
title: metrics_load_balancer_frontend_http_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_load_balancer_frontend_http_responses
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

Creates, updates, deletes, gets or lists a <code>metrics_load_balancer_frontend_http_responses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_load_balancer_frontend_http_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_load_balancer_frontend_http_responses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_lb_frontend_http_responses" /> | `SELECT` | <CopyableCode code="end, lb_id, start" /> | To retrieve frontend HTTP rate of response code for a given load balancer, send a GET request to `/v2/monitoring/metrics/load_balancer/frontend_http_responses`. |

## `SELECT` examples

To retrieve frontend HTTP rate of response code for a given load balancer, send a GET request to `/v2/monitoring/metrics/load_balancer/frontend_http_responses`.


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_load_balancer_frontend_http_responses
WHERE end = '{{ end }}'
AND lb_id = '{{ lb_id }}'
AND start = '{{ start }}';
```