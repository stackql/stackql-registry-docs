---
title: volume_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_snapshots
  - block_storage
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
<tr><td><b>Name</b></td><td><code>volume_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.block_storage.volume_snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier for the snapshot. |
| <CopyableCode code="name" /> | `string` | A human-readable name for the snapshot. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the snapshot was created. |
| <CopyableCode code="min_disk_size" /> | `integer` | The minimum size in GB required for a volume or Droplet to use this snapshot. |
| <CopyableCode code="regions" /> | `array` | An array of the regions that the snapshot is available in. The regions are represented by their identifying slug values. |
| <CopyableCode code="resource_id" /> | `string` | The unique identifier for the resource that the snapshot originated from. |
| <CopyableCode code="resource_type" /> | `string` | The type of resource that the snapshot originated from. |
| <CopyableCode code="size_gigabytes" /> | `number` | The billable size of the snapshot in gigabytes. |
| <CopyableCode code="tags" /> | `array` | An array of Tags the snapshot has been tagged with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="volumeSnapshots_get_byId" /> | `SELECT` | <CopyableCode code="snapshot_id" /> | To retrieve the details of a snapshot that has been created from a volume, send a GET request to `/v2/volumes/snapshots/$SNAPSHOT_ID`.<br /><br /> |
| <CopyableCode code="volumeSnapshots_list" /> | `SELECT` | <CopyableCode code="volume_id" /> | To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`.<br /><br /> |
| <CopyableCode code="volumeSnapshots_create" /> | `INSERT` | <CopyableCode code="volume_id, data__name" /> | To create a snapshot from a volume, sent a POST request to `/v2/volumes/$VOLUME_ID/snapshots`. |
| <CopyableCode code="volumeSnapshots_delete_byId" /> | `DELETE` | <CopyableCode code="snapshot_id" /> | To delete a volume snapshot, send a DELETE request to<br />`/v2/snapshots/$SNAPSHOT_ID`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /> |
| <CopyableCode code="_volumeSnapshots_get_byId" /> | `EXEC` | <CopyableCode code="snapshot_id" /> | To retrieve the details of a snapshot that has been created from a volume, send a GET request to `/v2/volumes/snapshots/$SNAPSHOT_ID`.<br /><br /> |
| <CopyableCode code="_volumeSnapshots_list" /> | `EXEC` | <CopyableCode code="volume_id" /> | To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`.<br /><br /> |
