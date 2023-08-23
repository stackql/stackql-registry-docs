---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - file
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.file.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the snapshot, in the format `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/instances/&#123;instance_id&#125;/snapshots/&#123;snapshot_id&#125;`. |
| `description` | `string` | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected. |
| `createTime` | `string` | Output only. The time when the snapshot was created. |
| `filesystemUsedBytes` | `string` | Output only. The amount of bytes needed to allocate a full copy of the snapshot content |
| `labels` | `object` | Resource labels to represent user provided metadata. |
| `state` | `string` | Output only. The snapshot state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId, snapshotsId` | Gets the details of a specific snapshot. |
| `list` | `SELECT` | `instancesId, locationsId, projectsId` | Lists all snapshots in a project for either a specified location or for all locations. |
| `create` | `INSERT` | `instancesId, locationsId, projectsId` | Creates a snapshot. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId, snapshotsId` | Deletes a snapshot. |
| `_list` | `EXEC` | `instancesId, locationsId, projectsId` | Lists all snapshots in a project for either a specified location or for all locations. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId, snapshotsId` | Updates the settings of a specific snapshot. |
