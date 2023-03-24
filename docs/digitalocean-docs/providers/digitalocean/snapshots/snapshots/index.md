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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.snapshots.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier for the snapshot. |
| `name` | `string` | A human-readable name for the snapshot. |
| `regions` | `array` | An array of the regions that the snapshot is available in. The regions are represented by their identifying slug values. |
| `min_disk_size` | `integer` | The minimum size in GB required for a volume or Droplet to use this snapshot. |
| `resource_type` | `string` | The type of resource that the snapshot originated from. |
| `tags` | `array` | An array of Tags the snapshot has been tagged with. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the snapshot was created. |
| `resource_id` | `string` | The unique identifier for the resource that the snapshot originated from. |
| `size_gigabytes` | `number` | The billable size of the snapshot in gigabytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `snapshot_id` | To retrieve information about a snapshot, send a GET request to<br />`/v2/snapshots/$SNAPSHOT_ID`.<br /><br />The response will be a JSON object with a key called `snapshot`. The value of<br />this will be an snapshot object containing the standard snapshot attributes.<br /> |
| `list` | `SELECT` |  | To list all of the snapshots available on your account, send a GET request to<br />`/v2/snapshots`.<br /><br />The response will be a JSON object with a key called `snapshots`. This will be<br />set to an array of `snapshot` objects, each of which will contain the standard<br />snapshot attributes.<br /><br />### Filtering Results by Resource Type<br /><br />It's possible to request filtered results by including certain query parameters.<br /><br />#### List Droplet Snapshots<br /><br />To retrieve only snapshots based on Droplets, include the `resource_type`<br />query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.<br /><br />#### List Volume Snapshots<br /><br />To retrieve only snapshots based on volumes, include the `resource_type`<br />query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.<br /> |
| `delete` | `DELETE` | `snapshot_id` | Both Droplet and volume snapshots are managed through the `/v2/snapshots/`<br />endpoint. To delete a snapshot, send a DELETE request to<br />`/v2/snapshots/$SNAPSHOT_ID`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /> |
| `_list` | `EXEC` |  | To list all of the snapshots available on your account, send a GET request to<br />`/v2/snapshots`.<br /><br />The response will be a JSON object with a key called `snapshots`. This will be<br />set to an array of `snapshot` objects, each of which will contain the standard<br />snapshot attributes.<br /><br />### Filtering Results by Resource Type<br /><br />It's possible to request filtered results by including certain query parameters.<br /><br />#### List Droplet Snapshots<br /><br />To retrieve only snapshots based on Droplets, include the `resource_type`<br />query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.<br /><br />#### List Volume Snapshots<br /><br />To retrieve only snapshots based on volumes, include the `resource_type`<br />query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.<br /> |
