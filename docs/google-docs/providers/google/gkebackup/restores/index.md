---
title: restores
hide_title: false
hide_table_of_contents: false
keywords:
  - restores
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
<tr><td><b>Name</b></td><td><code>restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.restores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the Restore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*` |
| `description` | `string` | User specified descriptive string for this Restore. |
| `state` | `string` | Output only. The current state of the Restore. |
| `labels` | `object` | A set of custom labels supplied by user. |
| `stateReason` | `string` | Output only. Human-readable description of why the Restore is in its current state. |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestore`, and systems are expected to put that etag in the request to `UpdateRestore` or `DeleteRestore` to ensure that their change will be applied to the same version of the resource. |
| `createTime` | `string` | Output only. The timestamp when this Restore resource was created. |
| `completeTime` | `string` | Output only. Timestamp of when the restore operation completed. |
| `restoreConfig` | `object` | Configuration of a restore. Next id: 12 |
| `updateTime` | `string` | Output only. The timestamp when this Restore resource was last updated. |
| `volumesRestoredCount` | `integer` | Output only. Number of volumes restored during the restore execution. |
| `cluster` | `string` | Output only. The target cluster into which this Restore will restore data. Valid formats: - `projects/*/locations/*/clusters/*` - `projects/*/zones/*/clusters/*` Inherited from parent RestorePlan's cluster value. |
| `resourcesRestoredCount` | `integer` | Output only. Number of resources restored during the restore execution. |
| `resourcesExcludedCount` | `integer` | Output only. Number of resources excluded during the restore execution. |
| `backup` | `string` | Required. Immutable. A reference to the Backup used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's backup_plan. Format: `projects/*/locations/*/backupPlans/*/backups/*`. |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| `resourcesFailedCount` | `integer` | Output only. Number of resources that failed to be restored during the restore execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, restorePlansId, restoresId` | Retrieves the details of a single Restore. |
| `list` | `SELECT` | `locationsId, projectsId, restorePlansId` | Lists the Restores for a given RestorePlan. |
| `create` | `INSERT` | `locationsId, projectsId, restorePlansId` | Creates a new Restore for the given RestorePlan. |
| `delete` | `DELETE` | `locationsId, projectsId, restorePlansId, restoresId` | Deletes an existing Restore. |
| `_list` | `EXEC` | `locationsId, projectsId, restorePlansId` | Lists the Restores for a given RestorePlan. |
| `patch` | `EXEC` | `locationsId, projectsId, restorePlansId, restoresId` | Update a Restore. |
