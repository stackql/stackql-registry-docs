
---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - backupdr
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>backup</code> resource or lists <code>backups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. Name of the resource. |
| <CopyableCode code="description" /> | `string` | Output only. The description of the Backup instance (2048 characters or less). |
| <CopyableCode code="backupApplianceBackupProperties" /> | `object` | BackupApplianceBackupProperties represents BackupDR backup appliance's properties. |
| <CopyableCode code="backupApplianceLocks" /> | `array` | Optional. The list of BackupLocks taken by the accessor Backup Appliance. |
| <CopyableCode code="backupType" /> | `string` | Output only. Type of the backup, unspecified, scheduled or ondemand. |
| <CopyableCode code="computeInstanceBackupProperties" /> | `object` | ComputeInstanceBackupProperties represents Compute Engine instance backup properties. |
| <CopyableCode code="consistencyTime" /> | `string` | Output only. The point in time when this backup was captured from the source. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="enforcedRetentionEndTime" /> | `string` | Optional. The backup can not be deleted before this time. |
| <CopyableCode code="etag" /> | `string` | Optional. Server specified ETag to prevent updates from overwriting each other. |
| <CopyableCode code="expireTime" /> | `string` | Optional. When this backup is automatically expired. |
| <CopyableCode code="gcpBackupPlanInfo" /> | `object` | GCPBackupPlanInfo captures the plan configuration details of Google Cloud resources at the time of backup. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. No labels currently defined. |
| <CopyableCode code="resourceSizeBytes" /> | `string` | Output only. source resource size in bytes at the time of the backup. |
| <CopyableCode code="serviceLocks" /> | `array` | Output only. The list of BackupLocks taken by the service to prevent the deletion of the backup. |
| <CopyableCode code="state" /> | `string` | Output only. The Backup resource instance state. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the instance was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupVaultsId, backupsId, dataSourcesId, locationsId, projectsId" /> | Gets details of a Backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Lists Backups in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupVaultsId, backupsId, dataSourcesId, locationsId, projectsId" /> | Deletes a Backup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupVaultsId, backupsId, dataSourcesId, locationsId, projectsId" /> | Updates the settings of a Backup. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="backupVaultsId, backupsId, dataSourcesId, locationsId, projectsId" /> | Restore from a Backup |

## `SELECT` examples

Lists Backups in a given project and location.

```sql
SELECT
name,
description,
backupApplianceBackupProperties,
backupApplianceLocks,
backupType,
computeInstanceBackupProperties,
consistencyTime,
createTime,
enforcedRetentionEndTime,
etag,
expireTime,
gcpBackupPlanInfo,
labels,
resourceSizeBytes,
serviceLocks,
state,
updateTime
FROM google.backupdr.backups
WHERE backupVaultsId = '{{ backupVaultsId }}'
AND dataSourcesId = '{{ dataSourcesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a backup only if the necessary resources are available.

```sql
UPDATE google.backupdr.backups
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
enforcedRetentionEndTime = '{{ enforcedRetentionEndTime }}',
expireTime = '{{ expireTime }}',
consistencyTime = '{{ consistencyTime }}',
etag = '{{ etag }}',
state = '{{ state }}',
serviceLocks = '{{ serviceLocks }}',
backupApplianceLocks = '{{ backupApplianceLocks }}',
computeInstanceBackupProperties = '{{ computeInstanceBackupProperties }}',
backupApplianceBackupProperties = '{{ backupApplianceBackupProperties }}',
backupType = '{{ backupType }}',
gcpBackupPlanInfo = '{{ gcpBackupPlanInfo }}',
resourceSizeBytes = '{{ resourceSizeBytes }}'
WHERE 
backupVaultsId = '{{ backupVaultsId }}'
AND backupsId = '{{ backupsId }}'
AND dataSourcesId = '{{ dataSourcesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified backup resource.

```sql
DELETE FROM google.backupdr.backups
WHERE backupVaultsId = '{{ backupVaultsId }}'
AND backupsId = '{{ backupsId }}'
AND dataSourcesId = '{{ dataSourcesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
