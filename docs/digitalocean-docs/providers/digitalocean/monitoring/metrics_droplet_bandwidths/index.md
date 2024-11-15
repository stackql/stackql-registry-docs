---
title: metrics_droplet_bandwidths
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_droplet_bandwidths
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

Creates, updates, deletes, gets or lists a <code>metrics_droplet_bandwidths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_droplet_bandwidths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.metrics_droplet_bandwidths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` |  |
| <CopyableCode code="status" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_droplet_bandwidth_metrics" /> | `SELECT` | <CopyableCode code="direction, end, host_id, interface, start" /> | To retrieve bandwidth metrics for a given Droplet, send a GET request to `/v2/monitoring/metrics/droplet/bandwidth`. Use the `interface` query parameter to specify if the results should be for the `private` or `public` interface. Use the `direction` query parameter to specify if the results should be for `inbound` or `outbound` traffic. The metrics in the response body are in megabits per second (Mbps). |

## `SELECT` examples

To retrieve bandwidth metrics for a given Droplet, send a GET request to `/v2/monitoring/metrics/droplet/bandwidth`. Use the `interface` query parameter to specify if the results should be for the `private` or `public` interface. Use the `direction` query parameter to specify if the results should be for `inbound` or `outbound` traffic. The metrics in the response body are in megabits per second (Mbps).


```sql
SELECT
data,
status
FROM digitalocean.monitoring.metrics_droplet_bandwidths
WHERE direction = '{{ direction }}'
AND end = '{{ end }}'
AND host_id = '{{ host_id }}'
AND interface = '{{ interface }}'
AND start = '{{ start }}';
```