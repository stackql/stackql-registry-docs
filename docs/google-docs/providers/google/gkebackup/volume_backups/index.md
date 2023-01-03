---
title: volume_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_backups
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
<tr><td><b>Name</b></td><td><code>volume_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.volume_backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the VolumeBackup resource. Format: projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*. |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| `stateMessage` | `string` | Output only. A human readable message explaining why the VolumeBackup is in its current state. |
| `diskSizeBytes` | `string` | Output only. The minimum size of the disk to which this VolumeBackup can be restored. |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume backup updates in order to avoid race conditions. |
| `sourcePvc` | `object` | A reference to a namespaced resource in Kubernetes. |
| `state` | `string` | Output only. The current state of this VolumeBackup. |
| `format` | `string` | Output only. The format used for the volume backup. |
| `createTime` | `string` | Output only. The timestamp when this VolumeBackup resource was created. |
| `volumeBackupHandle` | `string` | Output only. A storage system-specific opaque handle to the underlying volume backup. |
| `completeTime` | `string` | Output only. The timestamp when the associated underlying volume backup operation completed. |
| `storageBytes` | `string` | Output only. The aggregate size of the underlying artifacts associated with this VolumeBackup in the backup storage. This may change over time when multiple backups of the same volume share the same backup storage location. In particular, this is likely to increase in size when the immediately preceding backup of the same volume is deleted. |
| `updateTime` | `string` | Output only. The timestamp when this VolumeBackup resource was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_backupPlans_backups_volumeBackups_get` | `SELECT` | `backupPlansId, backupsId, locationsId, projectsId, volumeBackupsId` | Retrieve the details of a single VolumeBackup. |
| `projects_locations_backupPlans_backups_volumeBackups_list` | `SELECT` | `backupPlansId, backupsId, locationsId, projectsId` | Lists the VolumeBackups for a given Backup. |
