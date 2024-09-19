---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The name of the database. Values are of the form `projects//instances//databases/`, where `` is as specified in the `CREATE DATABASE` statement. This name can be passed to other API methods to identify the database. |
| <CopyableCode code="createTime" /> | `string` | Output only. If exists, the time at which the database creation started. |
| <CopyableCode code="databaseDialect" /> | `string` | Output only. The dialect of the Cloud Spanner Database. |
| <CopyableCode code="defaultLeader" /> | `string` | Output only. The read-write region which contains the database's leader replicas. This is the same as the value of default_leader database option set using DatabaseAdmin.CreateDatabase or DatabaseAdmin.UpdateDatabaseDdl. If not explicitly set, this is empty. |
| <CopyableCode code="earliestVersionTime" /> | `string` | Output only. Earliest timestamp at which older versions of the data can be read. This value is continuously updated by Cloud Spanner and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery. |
| <CopyableCode code="enableDropProtection" /> | `boolean` | Optional. Whether drop protection is enabled for this database. Defaults to false, if not set. For more details, please see how to [prevent accidental database deletion](https://cloud.google.com/spanner/docs/prevent-database-deletion). |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption configuration for a Cloud Spanner database. |
| <CopyableCode code="encryptionInfo" /> | `array` | Output only. For databases that are using customer managed encryption, this field contains the encryption information for the database, such as all Cloud KMS key versions that are in use. The `encryption_status' field inside of each `EncryptionInfo` is not populated. For databases that are using Google default or other types of encryption, this field is empty. This field is propagated lazily from the backend. There might be a delay from when a key version is being used and when it appears in this field. |
| <CopyableCode code="quorumInfo" /> | `object` | Information about the dual-region quorum. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. If true, the database is being updated. If false, there are no ongoing update operations for the database. |
| <CopyableCode code="restoreInfo" /> | `object` | Information about the database restore. |
| <CopyableCode code="state" /> | `string` | Output only. The current database state. |
| <CopyableCode code="versionRetentionPeriod" /> | `string` | Output only. The period in which Cloud Spanner retains all versions of data for the database. This is the same as the value of version_retention_period database option set using UpdateDatabaseDdl. Defaults to 1 hour, if not set. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_databases_get" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Gets the state of a Cloud Spanner database. |
| <CopyableCode code="projects_instances_databases_list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists Cloud Spanner databases. |
| <CopyableCode code="projects_instances_databases_create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId" /> | Creates a new Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format `/operations/` and can be used to track preparation of the database. The metadata field type is CreateDatabaseMetadata. The response field type is Database, if successful. |
| <CopyableCode code="projects_instances_databases_drop_database" /> | `DELETE` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Drops (aka deletes) a Cloud Spanner database. Completed backups for the database will be retained according to their `expire_time`. Note: Cloud Spanner might continue to accept requests for a few seconds after the database has been deleted. |
| <CopyableCode code="projects_instances_databases_patch" /> | `UPDATE` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Updates a Cloud Spanner database. The returned long-running operation can be used to track the progress of updating the database. If the named database does not exist, returns `NOT_FOUND`. While the operation is pending: * The database's reconciling field is set to true. * Cancelling the operation is best-effort. If the cancellation succeeds, the operation metadata's cancel_time is set, the updates are reverted, and the operation terminates with a `CANCELLED` status. * New UpdateDatabase requests will return a `FAILED_PRECONDITION` error until the pending operation is done (returns successfully or with error). * Reading the database via the API continues to give the pre-request values. Upon completion of the returned operation: * The new values are in effect and readable via the API. * The database's reconciling field becomes false. The returned long-running operation will have a name of the format `projects//instances//databases//operations/` and can be used to track the database modification. The metadata field type is UpdateDatabaseMetadata. The response field type is Database, if successful. |
| <CopyableCode code="projects_instances_databases_changequorum" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId" /> | `ChangeQuorum` is strictly restricted to databases that use dual-region instance configurations. Initiates a background operation to change the quorum of a database from dual-region mode to single-region mode or vice versa. The returned long-running operation has a name of the format `projects//instances//databases//operations/` and can be used to track execution of the `ChangeQuorum`. The metadata field type is ChangeQuorumMetadata. Authorization requires `spanner.databases.changequorum` permission on the resource database. |
| <CopyableCode code="projects_instances_databases_restore" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database long-running operation has a name of the format `projects//instances//databases//operations/`, and can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreDatabaseMetadata. The response type is Database, if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete. |

## `SELECT` examples

Lists Cloud Spanner databases.

```sql
SELECT
name,
createTime,
databaseDialect,
defaultLeader,
earliestVersionTime,
enableDropProtection,
encryptionConfig,
encryptionInfo,
quorumInfo,
reconciling,
restoreInfo,
state,
versionRetentionPeriod
FROM google.spanner.databases
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

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
INSERT INTO google.spanner.databases (
instancesId,
projectsId,
createStatement,
extraStatements,
encryptionConfig,
databaseDialect,
protoDescriptors
)
SELECT 
'{{ instancesId }}',
'{{ projectsId }}',
'{{ createStatement }}',
'{{ extraStatements }}',
'{{ encryptionConfig }}',
'{{ databaseDialect }}',
'{{ protoDescriptors }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: createStatement
      value: string
    - name: extraStatements
      value:
        - string
    - name: encryptionConfig
      value:
        - name: kmsKeyName
          value: string
        - name: kmsKeyNames
          value:
            - string
    - name: databaseDialect
      value: string
    - name: protoDescriptors
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE google.spanner.databases
SET 
name = '{{ name }}',
enableDropProtection = true|false
WHERE 
databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.databases
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
