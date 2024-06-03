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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.file.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the snapshot, in the format `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/instances/&#123;instance_id&#125;/snapshots/&#123;snapshot_id&#125;`. |
| <CopyableCode code="description" /> | `string` | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the snapshot was created. |
| <CopyableCode code="filesystemUsedBytes" /> | `string` | Output only. The amount of bytes needed to allocate a full copy of the snapshot content |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user provided metadata. |
| <CopyableCode code="state" /> | `string` | Output only. The snapshot state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId, snapshotsId" /> | Gets the details of a specific snapshot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Lists all snapshots in a project for either a specified location or for all locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Creates a snapshot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId, snapshotsId" /> | Deletes a snapshot. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId, snapshotsId" /> | Updates the settings of a specific snapshot. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Lists all snapshots in a project for either a specified location or for all locations. |
