---
title: backup_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_runs
  - sqladmin
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

Creates, updates, deletes, gets or lists a <code>backup_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.backup_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier for this backup run. Unique only for a specific Cloud SQL instance. |
| <CopyableCode code="description" /> | `string` | The description of this run, only applicable to on-demand backups. |
| <CopyableCode code="backupKind" /> | `string` | Specifies the kind of backup, PHYSICAL or DEFAULT_SNAPSHOT. |
| <CopyableCode code="diskEncryptionConfiguration" /> | `object` | Disk encryption configuration for an instance. |
| <CopyableCode code="diskEncryptionStatus" /> | `object` | Disk encryption status for an instance. |
| <CopyableCode code="endTime" /> | `string` | The time the backup operation completed in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="enqueuedTime" /> | `string` | The time the run was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="error" /> | `object` | Database instance operation error. |
| <CopyableCode code="instance" /> | `string` | Name of the database instance. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#backupRun`. |
| <CopyableCode code="location" /> | `string` | Location of the backups. |
| <CopyableCode code="maxChargeableBytes" /> | `string` | Output only. The maximum chargeable bytes for the backup. |
| <CopyableCode code="selfLink" /> | `string` | The URI of this resource. |
| <CopyableCode code="startTime" /> | `string` | The time the backup operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="status" /> | `string` | The status of this run. |
| <CopyableCode code="timeZone" /> | `string` | Backup time zone to prevent restores to an instance with a different time zone. Now relevant only for SQL Server. |
| <CopyableCode code="type" /> | `string` | The type of this run; can be either "AUTOMATED" or "ON_DEMAND" or "FINAL". This field defaults to "ON_DEMAND" and is ignored, when specified for insert requests. |
| <CopyableCode code="windowStartTime" /> | `string` | The start time of the backup window during which this the backup was attempted in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, instance, project" /> | Retrieves a resource containing information about a backup run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instance, project" /> | Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="instance, project" /> | Creates a new backup run on demand. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, instance, project" /> | Deletes the backup taken by a backup run. |

## `SELECT` examples

Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.

```sql
SELECT
id,
description,
backupKind,
diskEncryptionConfiguration,
diskEncryptionStatus,
endTime,
enqueuedTime,
error,
instance,
kind,
location,
maxChargeableBytes,
selfLink,
startTime,
status,
timeZone,
type,
windowStartTime
FROM google.sqladmin.backup_runs
WHERE instance = '{{ instance }}'
AND project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_runs</code> resource.

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
INSERT INTO google.sqladmin.backup_runs (
instance,
project,
status,
enqueuedTime,
startTime,
endTime,
error,
type,
description,
windowStartTime,
instance,
location,
diskEncryptionConfiguration,
diskEncryptionStatus,
backupKind,
timeZone
)
SELECT 
'{{ instance }}',
'{{ project }}',
'{{ status }}',
'{{ enqueuedTime }}',
'{{ startTime }}',
'{{ endTime }}',
'{{ error }}',
'{{ type }}',
'{{ description }}',
'{{ windowStartTime }}',
'{{ instance }}',
'{{ location }}',
'{{ diskEncryptionConfiguration }}',
'{{ diskEncryptionStatus }}',
'{{ backupKind }}',
'{{ timeZone }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: status
      value: string
    - name: enqueuedTime
      value: string
    - name: id
      value: string
    - name: startTime
      value: string
    - name: endTime
      value: string
    - name: error
      value:
        - name: kind
          value: string
        - name: code
          value: string
        - name: message
          value: string
    - name: type
      value: string
    - name: description
      value: string
    - name: windowStartTime
      value: string
    - name: instance
      value: string
    - name: selfLink
      value: string
    - name: location
      value: string
    - name: diskEncryptionConfiguration
      value:
        - name: kmsKeyName
          value: string
        - name: kind
          value: string
    - name: diskEncryptionStatus
      value:
        - name: kmsKeyVersionName
          value: string
        - name: kind
          value: string
    - name: backupKind
      value: string
    - name: timeZone
      value: string
    - name: maxChargeableBytes
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backup_runs</code> resource.

```sql
/*+ delete */
DELETE FROM google.sqladmin.backup_runs
WHERE id = '{{ id }}'
AND instance = '{{ instance }}'
AND project = '{{ project }}';
```
