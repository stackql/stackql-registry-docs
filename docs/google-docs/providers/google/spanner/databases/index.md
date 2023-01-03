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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The name of the database. Values are of the form `projects//instances//databases/`, where `` is as specified in the `CREATE DATABASE` statement. This name can be passed to other API methods to identify the database. |
| `encryptionInfo` | `array` | Output only. For databases that are using customer managed encryption, this field contains the encryption information for the database, such as encryption state and the Cloud KMS key versions that are in use. For databases that are using Google default or other types of encryption, this field is empty. This field is propagated lazily from the backend. There might be a delay from when a key version is being used and when it appears in this field. |
| `restoreInfo` | `object` | Information about the database restore. |
| `earliestVersionTime` | `string` | Output only. Earliest timestamp at which older versions of the data can be read. This value is continuously updated by Cloud Spanner and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery. |
| `state` | `string` | Output only. The current database state. |
| `versionRetentionPeriod` | `string` | Output only. The period in which Cloud Spanner retains all versions of data for the database. This is the same as the value of version_retention_period database option set using UpdateDatabaseDdl. Defaults to 1 hour, if not set. |
| `createTime` | `string` | Output only. If exists, the time at which the database creation started. |
| `encryptionConfig` | `object` | Encryption configuration for a Cloud Spanner database. |
| `databaseDialect` | `string` | Output only. The dialect of the Cloud Spanner Database. |
| `defaultLeader` | `string` | Output only. The read-write region which contains the database's leader replicas. This is the same as the value of default_leader database option set using DatabaseAdmin.CreateDatabase or DatabaseAdmin.UpdateDatabaseDdl. If not explicitly set, this is empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instances_databases_get` | `SELECT` | `databasesId, instancesId, projectsId` | Gets the state of a Cloud Spanner database. |
| `projects_instances_databases_list` | `SELECT` | `instancesId, projectsId` | Lists Cloud Spanner databases. |
| `projects_instances_databases_create` | `INSERT` | `instancesId, projectsId` | Creates a new Cloud Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format `/operations/` and can be used to track preparation of the database. The metadata field type is CreateDatabaseMetadata. The response field type is Database, if successful. |
| `projects_instances_databases_dropDatabase` | `DELETE` | `databasesId, instancesId, projectsId` | Drops (aka deletes) a Cloud Spanner database. Completed backups for the database will be retained according to their `expire_time`. Note: Cloud Spanner might continue to accept requests for a few seconds after the database has been deleted. |
| `projects_instances_databases_restore` | `EXEC` | `instancesId, projectsId` | Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database long-running operation has a name of the format `projects//instances//databases//operations/`, and can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreDatabaseMetadata. The response type is Database, if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete. |
| `projects_instances_databases_updateDdl` | `EXEC` | `databasesId, instancesId, projectsId` | Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned long-running operation will have a name of the format `/operations/` and can be used to track execution of the schema change(s). The metadata field type is UpdateDatabaseDdlMetadata. The operation has no response. |
