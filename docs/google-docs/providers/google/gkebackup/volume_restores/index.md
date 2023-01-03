---
title: volume_restores
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_restores
  - gkebackup
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.volume_restores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Full name of the VolumeRestore resource. Format: projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*. |
| `volumeHandle` | `string` | Output only. A storage system-specific opaque handler to the underlying volume created for the target PVC from the volume backup. |
| `createTime` | `string` | Output only. The timestamp when this VolumeRestore resource was created. |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume restore updates in order to avoid race conditions. |
| `stateMessage` | `string` | Output only. A human readable message explaining why the VolumeRestore is in its current state. |
| `targetPvc` | `object` | A reference to a namespaced resource in Kubernetes. |
| `volumeType` | `string` | Output only. The type of volume provisioned |
| `updateTime` | `string` | Output only. The timestamp when this VolumeRestore resource was last updated. |
| `state` | `string` | Output only. The current state of this VolumeRestore. |
| `volumeBackup` | `string` | Output only. The full name of the VolumeBackup from which the volume will be restored. Format: projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*. |
| `completeTime` | `string` | Output only. The timestamp when the associated underlying volume restoration completed. |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_restorePlans_restores_volumeRestores_get` | `SELECT` | `locationsId, projectsId, restorePlansId, restoresId, volumeRestoresId` | Retrieve the details of a single VolumeRestore. |
| `projects_locations_restorePlans_restores_volumeRestores_list` | `SELECT` | `locationsId, projectsId, restorePlansId, restoresId` | Lists the VolumeRestores for a given Restore. |
