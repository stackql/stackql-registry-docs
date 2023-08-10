---
title: restore_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_plans
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
<tr><td><b>Name</b></td><td><code>restore_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.restore_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the RestorePlan resource. Format: `projects/*/locations/*/restorePlans/*`. |
| `description` | `string` | Optional. User specified descriptive string for this RestorePlan. |
| `updateTime` | `string` | Output only. The timestamp when this RestorePlan resource was last updated. |
| `stateReason` | `string` | Output only. Human-readable description of why RestorePlan is in the current `state` |
| `backupPlan` | `string` | Required. Immutable. A reference to the BackupPlan from which Backups may be used as the source for Restores created via this RestorePlan. Format: `projects/*/locations/*/backupPlans/*`. |
| `createTime` | `string` | Output only. The timestamp when this RestorePlan resource was created. |
| `restoreConfig` | `object` | Configuration of a restore. Next id: 12 |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| `cluster` | `string` | Required. Immutable. The target cluster into which Restores created via this RestorePlan will restore data. NOTE: the cluster's region must be the same as the RestorePlan. Valid formats: - `projects/*/locations/*/clusters/*` - `projects/*/zones/*/clusters/*` |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestorePlan`, and systems are expected to put that etag in the request to `UpdateRestorePlan` or `DeleteRestorePlan` to ensure that their change will be applied to the same version of the resource. |
| `labels` | `object` | Optional. A set of custom labels supplied by user. |
| `state` | `string` | Output only. State of the RestorePlan. This State field reflects the various stages a RestorePlan can be in during the Create operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, restorePlansId` | Retrieve the details of a single RestorePlan. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists RestorePlans in a given location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new RestorePlan in a given location. |
| `delete` | `DELETE` | `locationsId, projectsId, restorePlansId` | Deletes an existing RestorePlan. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists RestorePlans in a given location. |
| `patch` | `EXEC` | `locationsId, projectsId, restorePlansId` | Update a RestorePlan. |
