---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - snapshots
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
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.snapshots.snapshots" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="snapshot_id" /> | To retrieve information about a snapshot, send a GET request to<br />`/v2/snapshots/$SNAPSHOT_ID`.<br /><br />The response will be a JSON object with a key called `snapshot`. The value of<br />this will be an snapshot object containing the standard snapshot attributes.<br /> |
| <CopyableCode code="list" /> | `SELECT` |  | To list all of the snapshots available on your account, send a GET request to<br />`/v2/snapshots`.<br /><br />The response will be a JSON object with a key called `snapshots`. This will be<br />set to an array of `snapshot` objects, each of which will contain the standard<br />snapshot attributes.<br /><br />### Filtering Results by Resource Type<br /><br />It's possible to request filtered results by including certain query parameters.<br /><br />#### List Droplet Snapshots<br /><br />To retrieve only snapshots based on Droplets, include the `resource_type`<br />query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.<br /><br />#### List Volume Snapshots<br /><br />To retrieve only snapshots based on volumes, include the `resource_type`<br />query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.<br /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="snapshot_id" /> | Both Droplet and volume snapshots are managed through the `/v2/snapshots/`<br />endpoint. To delete a snapshot, send a DELETE request to<br />`/v2/snapshots/$SNAPSHOT_ID`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /> |
| <CopyableCode code="_list" /> | `EXEC` |  | To list all of the snapshots available on your account, send a GET request to<br />`/v2/snapshots`.<br /><br />The response will be a JSON object with a key called `snapshots`. This will be<br />set to an array of `snapshot` objects, each of which will contain the standard<br />snapshot attributes.<br /><br />### Filtering Results by Resource Type<br /><br />It's possible to request filtered results by including certain query parameters.<br /><br />#### List Droplet Snapshots<br /><br />To retrieve only snapshots based on Droplets, include the `resource_type`<br />query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.<br /><br />#### List Volume Snapshots<br /><br />To retrieve only snapshots based on volumes, include the `resource_type`<br />query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.<br /> |
