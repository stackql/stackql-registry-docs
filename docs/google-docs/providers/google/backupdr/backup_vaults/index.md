---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
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

Creates, updates, deletes, gets or lists a <code>backup_vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.backup_vaults" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name. |
| <CopyableCode code="description" /> | `string` | Optional. The description of the BackupVault instance (2048 characters or less). |
| <CopyableCode code="annotations" /> | `object` | Optional. User annotations. See https://google.aip.dev/128#annotations Stores small amounts of arbitrary data. |
| <CopyableCode code="backupCount" /> | `string` | Output only. The number of backups in this backup vault. |
| <CopyableCode code="backupMinimumEnforcedRetentionDuration" /> | `string` | Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="deletable" /> | `boolean` | Output only. Set to true when there are no backups nested under this resource. |
| <CopyableCode code="effectiveTime" /> | `string` | Optional. Time after which the BackupVault resource is locked. |
| <CopyableCode code="etag" /> | `string` | Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. No labels currently defined: |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there. |
| <CopyableCode code="state" /> | `string` | Output only. The BackupVault resource instance state. |
| <CopyableCode code="totalStoredBytes" /> | `string` | Output only. Total size of the storage used by all backup resources. |
| <CopyableCode code="uid" /> | `string` | Output only. Output only Immutable after resource creation until resource deletion. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the instance was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupVaultsId, locationsId, projectsId" /> | Gets details of a BackupVault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists BackupVaults in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupVaultsId, locationsId, projectsId" /> | Deletes a BackupVault. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupVaultsId, locationsId, projectsId" /> | Updates the settings of a BackupVault. |

## `SELECT` examples

Lists BackupVaults in a given project and location.

```sql
SELECT
name,
description,
annotations,
backupCount,
backupMinimumEnforcedRetentionDuration,
createTime,
deletable,
effectiveTime,
etag,
labels,
serviceAccount,
state,
totalStoredBytes,
uid,
updateTime
FROM google.backupdr.backup_vaults
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_vaults</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.backupdr.backup_vaults (
locationsId,
projectsId,
description,
labels,
backupMinimumEnforcedRetentionDuration,
etag,
effectiveTime,
annotations
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ labels }}',
'{{ backupMinimumEnforcedRetentionDuration }}',
'{{ etag }}',
'{{ effectiveTime }}',
'{{ annotations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
labels: object
createTime: string
updateTime: string
backupMinimumEnforcedRetentionDuration: string
deletable: boolean
etag: string
state: string
effectiveTime: string
backupCount: string
serviceAccount: string
totalStoredBytes: string
uid: string
annotations: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backup_vaults</code> resource.

```sql
/*+ update */
UPDATE google.backupdr.backup_vaults
SET 
description = '{{ description }}',
labels = '{{ labels }}',
backupMinimumEnforcedRetentionDuration = '{{ backupMinimumEnforcedRetentionDuration }}',
etag = '{{ etag }}',
effectiveTime = '{{ effectiveTime }}',
annotations = '{{ annotations }}'
WHERE 
backupVaultsId = '{{ backupVaultsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backup_vaults</code> resource.

```sql
/*+ delete */
DELETE FROM google.backupdr.backup_vaults
WHERE backupVaultsId = '{{ backupVaultsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
