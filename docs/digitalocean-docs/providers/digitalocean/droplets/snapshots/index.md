---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - droplets
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique identifier for the snapshot or backup. |
| <CopyableCode code="name" /> | `string` | A human-readable name for the snapshot. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the snapshot was created. |
| <CopyableCode code="min_disk_size" /> | `integer` | The minimum size in GB required for a volume or Droplet to use this snapshot. |
| <CopyableCode code="regions" /> | `array` | An array of the regions that the snapshot is available in. The regions are represented by their identifying slug values. |
| <CopyableCode code="size_gigabytes" /> | `number` | The billable size of the snapshot in gigabytes. |
| <CopyableCode code="type" /> | `string` | Describes the kind of image. It may be one of `snapshot` or `backup`. This specifies whether an image is a user-generated Droplet snapshot or automatically created Droplet backup. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_snapshots" /> | `SELECT` | <CopyableCode code="droplet_id" /> |
| <CopyableCode code="_list_snapshots" /> | `EXEC` | <CopyableCode code="droplet_id" /> |
