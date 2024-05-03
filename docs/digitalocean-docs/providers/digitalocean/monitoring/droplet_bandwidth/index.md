---
title: droplet_bandwidth
hide_title: false
hide_table_of_contents: false
keywords:
  - droplet_bandwidth
  - monitoring
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
<tr><td><b>Name</b></td><td><code>droplet_bandwidth</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.droplet_bandwidth" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metric" /> | `object` | An object containing the metric labels. |
| <CopyableCode code="values" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_dropletBandwidthMetrics" /> | `SELECT` | <CopyableCode code="direction, end, host_id, interface, start" /> |
| <CopyableCode code="_get_dropletBandwidthMetrics" /> | `EXEC` | <CopyableCode code="direction, end, host_id, interface, start" /> |
