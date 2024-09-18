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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.firestore.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the Database. Format: `projects/{project}/databases/{database}` |
| <CopyableCode code="appEngineIntegrationMode" /> | `string` | The App Engine integration mode to use for this database. |
| <CopyableCode code="cmekConfig" /> | `object` | The CMEK (Customer Managed Encryption Key) configuration for a Firestore database. If not present, the database is secured by the default Google encryption key. |
| <CopyableCode code="concurrencyMode" /> | `string` | The concurrency control mode to use for this database. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp at which this database was created. Databases created before 2016 do not populate create_time. |
| <CopyableCode code="deleteProtectionState" /> | `string` | State of delete protection for the database. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The timestamp at which this database was deleted. Only set if the database has been deleted. |
| <CopyableCode code="earliestVersionTime" /> | `string` | Output only. The earliest timestamp at which older versions of the data can be read from the database. See [version_retention_period] above; this field is populated with `now - version_retention_period`. This value is continuously updated, and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="keyPrefix" /> | `string` | Output only. The key_prefix for this database. This key_prefix is used, in combination with the project ID ("~") to construct the application ID that is returned from the Cloud Datastore APIs in Google App Engine first generation runtimes. This value may be empty in which case the appid to use for URL-encoded keys is the project_id (eg: foo instead of v~foo). |
| <CopyableCode code="locationId" /> | `string` | The location of the database. Available locations are listed at https://cloud.google.com/firestore/docs/locations. |
| <CopyableCode code="pointInTimeRecoveryEnablement" /> | `string` | Whether to enable the PITR feature on this database. |
| <CopyableCode code="previousId" /> | `string` | Output only. The database resource's prior database ID. This field is only populated for deleted databases. |
| <CopyableCode code="sourceInfo" /> | `object` | Information about the provenance of this database. |
| <CopyableCode code="type" /> | `string` | The type of the database. See https://cloud.google.com/datastore/docs/firestore-or-datastore for information about how to choose. |
| <CopyableCode code="uid" /> | `string` | Output only. The system-generated UUID4 for this Database. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp at which this database was most recently updated. Note this only includes updates to the database resource and not data contained by the database. |
| <CopyableCode code="versionRetentionPeriod" /> | `string` | Output only. The period during which past versions of data are retained in the database. Any read or query can specify a `read_time` within this window, and will read the state of the database at that time. If the PITR feature is enabled, the retention period is 7 days. Otherwise, the retention period is 1 hour. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databasesId, projectsId" /> | Gets information about a database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | List all the databases in the project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Create a database. |
| <CopyableCode code="bulk_delete_documents" /> | `DELETE` | <CopyableCode code="databasesId, projectsId" /> | Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created. For more details on bulk delete behavior, refer to: https://cloud.google.com/firestore/docs/manage-data/bulk-delete |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databasesId, projectsId" /> | Deletes a database. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="databasesId, projectsId" /> | Updates a database. |
| <CopyableCode code="export_documents" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. For more details on export behavior and output format, refer to: https://cloud.google.com/firestore/docs/manage-data/export-import |
| <CopyableCode code="import_documents" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="projectsId" /> | Creates a new database by restoring from an existing backup. The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup. The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed. |

## `SELECT` examples

List all the databases in the project.

```sql
SELECT
name,
appEngineIntegrationMode,
cmekConfig,
concurrencyMode,
createTime,
deleteProtectionState,
deleteTime,
earliestVersionTime,
etag,
keyPrefix,
locationId,
pointInTimeRecoveryEnablement,
previousId,
sourceInfo,
type,
uid,
updateTime,
versionRetentionPeriod
FROM google.firestore.databases
WHERE projectsId = '{{ projectsId }}'; 
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
INSERT INTO google.firestore.databases (
projectsId,
name,
locationId,
type,
concurrencyMode,
pointInTimeRecoveryEnablement,
appEngineIntegrationMode,
deleteProtectionState,
cmekConfig,
etag
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ locationId }}',
'{{ type }}',
'{{ concurrencyMode }}',
'{{ pointInTimeRecoveryEnablement }}',
'{{ appEngineIntegrationMode }}',
'{{ deleteProtectionState }}',
'{{ cmekConfig }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
uid: string
createTime: string
updateTime: string
deleteTime: string
locationId: string
type: string
concurrencyMode: string
versionRetentionPeriod: string
earliestVersionTime: string
pointInTimeRecoveryEnablement: string
appEngineIntegrationMode: string
keyPrefix: string
deleteProtectionState: string
cmekConfig:
  kmsKeyName: string
  activeKeyVersion:
    - type: string
previousId: string
sourceInfo:
  backup:
    backup: string
  operation: string
etag: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE google.firestore.databases
SET 
name = '{{ name }}',
locationId = '{{ locationId }}',
type = '{{ type }}',
concurrencyMode = '{{ concurrencyMode }}',
pointInTimeRecoveryEnablement = '{{ pointInTimeRecoveryEnablement }}',
appEngineIntegrationMode = '{{ appEngineIntegrationMode }}',
deleteProtectionState = '{{ deleteProtectionState }}',
cmekConfig = '{{ cmekConfig }}',
etag = '{{ etag }}'
WHERE 
databasesId = '{{ databasesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM google.firestore.databases
WHERE databasesId = '{{ databasesId }}'
AND projectsId = '{{ projectsId }}';
```
