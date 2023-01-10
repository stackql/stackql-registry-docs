---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.file.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the backup, in the format `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/backups/&#123;backup_id&#125;`. |
| `description` | `string` | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected. |
| `downloadBytes` | `string` | Output only. Amount of bytes that will be downloaded if the backup is restored. This may be different than storage bytes, since sequential backups of the same disk will share storage. |
| `capacityGb` | `string` | Output only. Capacity of the source file share when the backup was created. |
| `createTime` | `string` | Output only. The time when the backup was created. |
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `sourceFileShare` | `string` | Name of the file share in the source Filestore instance that the backup is created from. |
| `sourceInstance` | `string` | The resource name of the source Filestore instance, in the format `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/instances/&#123;instance_id&#125;`, used to create this backup. |
| `sourceInstanceTier` | `string` | Output only. The service tier of the source Filestore instance that this backup is created from. |
| `state` | `string` | Output only. The backup state. |
| `storageBytes` | `string` | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion. |
| `labels` | `object` | Resource labels to represent user provided metadata. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_backups_get` | `SELECT` | `backupsId, locationsId, projectsId` | Gets the details of a specific backup. |
| `projects_locations_backups_list` | `SELECT` | `locationsId, projectsId` | Lists all backups in a project for either a specified location or for all locations. |
| `projects_locations_backups_create` | `INSERT` | `locationsId, projectsId` | Creates a backup. |
| `projects_locations_backups_delete` | `DELETE` | `backupsId, locationsId, projectsId` | Deletes a backup. |
| `projects_locations_backups_patch` | `EXEC` | `backupsId, locationsId, projectsId` | Updates the settings of a specific backup. |
