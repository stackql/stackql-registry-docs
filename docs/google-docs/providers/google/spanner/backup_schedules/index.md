---
title: backup_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedules
  - spanner
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

Creates, updates, deletes, gets or lists a <code>backup_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.backup_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Output only for the CreateBackupSchedule operation. Required for the UpdateBackupSchedule operation. A globally unique identifier for the backup schedule which cannot be changed. Values are of the form `projects//instances//databases//backupSchedules/a-z*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length. |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption configuration for the backup to create. |
| <CopyableCode code="fullBackupSpec" /> | `object` | The specification for full backups. A full backup stores the entire contents of the database at a given version time. |
| <CopyableCode code="incrementalBackupSpec" /> | `object` | The specification for incremental backup chains. An incremental backup stores the delta of changes between a previous backup and the database contents at a given version time. An incremental backup chain consists of a full backup and zero or more successive incremental backups. The first backup created for an incremental backup chain is always a full backup. |
| <CopyableCode code="retentionDuration" /> | `string` | Optional. The retention duration of a backup that must be at least 6 hours and at most 366 days. The backup is eligible to be automatically deleted once the retention period has elapsed. |
| <CopyableCode code="spec" /> | `object` | Defines specifications of the backup schedule. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp at which the schedule was last updated. If the schedule has never been updated, this field contains the timestamp when the schedule was first created. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_databases_backup_schedules_get" /> | `SELECT` | <CopyableCode code="backupSchedulesId, databasesId, instancesId, projectsId" /> | Gets backup schedule for the input schedule name. |
| <CopyableCode code="projects_instances_databases_backup_schedules_list" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Lists all the backup schedules for the database. |
| <CopyableCode code="projects_instances_databases_backup_schedules_create" /> | `INSERT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Creates a new backup schedule. |
| <CopyableCode code="projects_instances_databases_backup_schedules_delete" /> | `DELETE` | <CopyableCode code="backupSchedulesId, databasesId, instancesId, projectsId" /> | Deletes a backup schedule. |
| <CopyableCode code="projects_instances_databases_backup_schedules_patch" /> | `UPDATE` | <CopyableCode code="backupSchedulesId, databasesId, instancesId, projectsId" /> | Updates a backup schedule. |

## `SELECT` examples

Lists all the backup schedules for the database.

```sql
SELECT
name,
encryptionConfig,
fullBackupSpec,
incrementalBackupSpec,
retentionDuration,
spec,
updateTime
FROM google.spanner.backup_schedules
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_schedules</code> resource.

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
INSERT INTO google.spanner.backup_schedules (
databasesId,
instancesId,
projectsId,
name,
spec,
retentionDuration,
encryptionConfig,
fullBackupSpec,
incrementalBackupSpec
)
SELECT 
'{{ databasesId }}',
'{{ instancesId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ spec }}',
'{{ retentionDuration }}',
'{{ encryptionConfig }}',
'{{ fullBackupSpec }}',
'{{ incrementalBackupSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: spec
      value:
        - name: cronSpec
          value:
            - name: text
              value: string
            - name: timeZone
              value: string
            - name: creationWindow
              value: string
    - name: retentionDuration
      value: string
    - name: encryptionConfig
      value:
        - name: encryptionType
          value: string
        - name: kmsKeyName
          value: string
        - name: kmsKeyNames
          value:
            - string
    - name: fullBackupSpec
      value: []
    - name: incrementalBackupSpec
      value: []
    - name: updateTime
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backup_schedules</code> resource.

```sql
/*+ update */
UPDATE google.spanner.backup_schedules
SET 
name = '{{ name }}',
spec = '{{ spec }}',
retentionDuration = '{{ retentionDuration }}',
encryptionConfig = '{{ encryptionConfig }}',
fullBackupSpec = '{{ fullBackupSpec }}',
incrementalBackupSpec = '{{ incrementalBackupSpec }}'
WHERE 
backupSchedulesId = '{{ backupSchedulesId }}'
AND databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backup_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.backup_schedules
WHERE backupSchedulesId = '{{ backupSchedulesId }}'
AND databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
