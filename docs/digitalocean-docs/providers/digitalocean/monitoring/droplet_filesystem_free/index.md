---
title: droplet_filesystem_free
hide_title: false
hide_table_of_contents: false
keywords:
  - droplet_filesystem_free
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
<tr><td><b>Name</b></td><td><code>droplet_filesystem_free</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.droplet_filesystem_free" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metric" /> | `object` | An object containing the metric labels. |
| <CopyableCode code="values" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_dropletFilesystemFreeMetrics" /> | `SELECT` | <CopyableCode code="end, host_id, start" /> |
| <CopyableCode code="_get_dropletFilesystemFreeMetrics" /> | `EXEC` | <CopyableCode code="end, host_id, start" /> |
