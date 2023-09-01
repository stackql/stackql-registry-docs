---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - firestore
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the Database. Format: `projects/&#123;project&#125;/databases/&#123;database&#125;` |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `createTime` | `string` | Output only. The timestamp at which this database was created. Databases created before 2016 do not populate create_time. |
| `locationId` | `string` | The location of the database. Available databases are listed at https://cloud.google.com/firestore/docs/locations. |
| `deleteProtectionState` | `string` | State of delete protection for the database. |
| `pointInTimeRecoveryEnablement` | `string` | Whether to enable the PITR feature on this database. |
| `uid` | `string` | Output only. The system-generated UUID4 for this Database. |
| `concurrencyMode` | `string` | The concurrency control mode to use for this database. |
| `versionRetentionPeriod` | `string` | Output only. The period during which past versions of data are retained in the database. Any read or query can specify a `read_time` within this window, and will read the state of the database at that time. If the PITR feature is enabled, the retention period is 7 days. Otherwise, the retention period is 1 hour. |
| `earliestVersionTime` | `string` | Output only. The earliest timestamp at which older versions of the data can be read from the database. See [version_retention_period] above; this field is populated with `now - version_retention_period`. This value is continuously updated, and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery. |
| `appEngineIntegrationMode` | `string` | The App Engine integration mode to use for this database. |
| `updateTime` | `string` | Output only. The timestamp at which this database was most recently updated. Note this only includes updates to the database resource and not data contained by the database. |
| `type` | `string` | The type of the database. See https://cloud.google.com/datastore/docs/firestore-or-datastore for information about how to choose. |
| `keyPrefix` | `string` | Output only. The key_prefix for this database. This key_prefix is used, in combination with the project id ("~") to construct the application id that is returned from the Cloud Datastore APIs in Google App Engine first generation runtimes. This value may be empty in which case the appid to use for URL-encoded keys is the project_id (eg: foo instead of v~foo). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databasesId, projectsId` | Gets information about a database. |
| `list` | `SELECT` | `projectsId` | List all the databases in the project. |
| `create` | `INSERT` | `projectsId` | Create a database. |
| `delete` | `DELETE` | `databasesId, projectsId` | Deletes a database. |
| `export_documents` | `EXEC` | `databasesId, projectsId` | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. For more details on export behavior and output format, refer to: https://cloud.google.com/firestore/docs/manage-data/export-import |
| `import_documents` | `EXEC` | `databasesId, projectsId` | Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore. |
| `patch` | `EXEC` | `databasesId, projectsId` | Updates a database. |
| `restore` | `EXEC` | `projectsId` | Create a new database by restore from an existing backup. The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup. The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed. Cancelling the returned operation will stop the restore and delete the in-progress database, if the restore is still active. |
