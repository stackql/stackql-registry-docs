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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkebackup.backup_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the BackupPlan resource. Format: `projects/*/locations/*/backupPlans/*` |
| <CopyableCode code="description" /> | `string` | Optional. User specified descriptive string for this BackupPlan. |
| <CopyableCode code="backupConfig" /> | `object` | BackupConfig defines the configuration of Backups created via this BackupPlan. |
| <CopyableCode code="backupSchedule" /> | `object` | Defines scheduling parameters for automatically creating Backups via this BackupPlan. |
| <CopyableCode code="cluster" /> | `string` | Required. Immutable. The source cluster from which Backups will be created via this BackupPlan. Valid formats: - `projects/*/locations/*/clusters/*` - `projects/*/zones/*/clusters/*` |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when this BackupPlan resource was created. |
| <CopyableCode code="deactivated" /> | `boolean` | Optional. This flag indicates whether this BackupPlan has been deactivated. Setting this field to True locks the BackupPlan such that no further updates will be allowed (except deletes), including the deactivated field itself. It also prevents any new Backups from being created via this BackupPlan (including scheduled Backups). Default: False |
| <CopyableCode code="etag" /> | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup plan from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform BackupPlan updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackupPlan`, and systems are expected to put that etag in the request to `UpdateBackupPlan` or `DeleteBackupPlan` to ensure that their change will be applied to the same version of the resource. |
| <CopyableCode code="labels" /> | `object` | Optional. A set of custom labels supplied by user. |
| <CopyableCode code="protectedPodCount" /> | `integer` | Output only. The number of Kubernetes Pods backed up in the last successful Backup created via this BackupPlan. |
| <CopyableCode code="retentionPolicy" /> | `object` | RetentionPolicy defines a Backup retention policy for a BackupPlan. |
| <CopyableCode code="state" /> | `string` | Output only. State of the BackupPlan. This State field reflects the various stages a BackupPlan can be in during the Create operation. It will be set to "DEACTIVATED" if the BackupPlan is deactivated on an Update |
| <CopyableCode code="stateReason" /> | `string` | Output only. Human-readable description of why BackupPlan is in the current `state` |
| <CopyableCode code="uid" /> | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when this BackupPlan resource was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Retrieve the details of a single BackupPlan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists BackupPlans in a given location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new BackupPlan in a given location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Deletes an existing BackupPlan. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists BackupPlans in a given location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Update a BackupPlan. |
