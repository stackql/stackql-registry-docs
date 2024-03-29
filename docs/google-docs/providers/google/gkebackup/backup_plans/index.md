---
title: backup_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_plans
  - gkebackup
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
<tr><td><b>Name</b></td><td><code>backup_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.backup_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the BackupPlan resource. Format: `projects/*/locations/*/backupPlans/*` |
| `description` | `string` | Optional. User specified descriptive string for this BackupPlan. |
| `retentionPolicy` | `object` | RetentionPolicy defines a Backup retention policy for a BackupPlan. |
| `backupConfig` | `object` | BackupConfig defines the configuration of Backups created via this BackupPlan. |
| `deactivated` | `boolean` | Optional. This flag indicates whether this BackupPlan has been deactivated. Setting this field to True locks the BackupPlan such that no further updates will be allowed (except deletes), including the deactivated field itself. It also prevents any new Backups from being created via this BackupPlan (including scheduled Backups). Default: False |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| `state` | `string` | Output only. State of the BackupPlan. This State field reflects the various stages a BackupPlan can be in during the Create operation. It will be set to "DEACTIVATED" if the BackupPlan is deactivated on an Update |
| `createTime` | `string` | Output only. The timestamp when this BackupPlan resource was created. |
| `backupSchedule` | `object` | Defines scheduling parameters for automatically creating Backups via this BackupPlan. |
| `cluster` | `string` | Required. Immutable. The source cluster from which Backups will be created via this BackupPlan. Valid formats: - `projects/*/locations/*/clusters/*` - `projects/*/zones/*/clusters/*` |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup plan from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform BackupPlan updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackupPlan`, and systems are expected to put that etag in the request to `UpdateBackupPlan` or `DeleteBackupPlan` to ensure that their change will be applied to the same version of the resource. |
| `labels` | `object` | Optional. A set of custom labels supplied by user. |
| `protectedPodCount` | `integer` | Output only. The number of Kubernetes Pods backed up in the last successful Backup created via this BackupPlan. |
| `stateReason` | `string` | Output only. Human-readable description of why BackupPlan is in the current `state` |
| `updateTime` | `string` | Output only. The timestamp when this BackupPlan resource was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPlansId, locationsId, projectsId` | Retrieve the details of a single BackupPlan. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists BackupPlans in a given location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new BackupPlan in a given location. |
| `delete` | `DELETE` | `backupPlansId, locationsId, projectsId` | Deletes an existing BackupPlan. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists BackupPlans in a given location. |
| `patch` | `EXEC` | `backupPlansId, locationsId, projectsId` | Update a BackupPlan. |
