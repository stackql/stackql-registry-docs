---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - datastream
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

Creates, updates, deletes, gets or lists a <code>streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.streams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The stream's name. |
| <CopyableCode code="backfillAll" /> | `object` | Backfill strategy to automatically backfill the Stream's objects. Specific objects can be excluded. |
| <CopyableCode code="backfillNone" /> | `object` | Backfill strategy to disable automatic backfill for the Stream's objects. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the stream. |
| <CopyableCode code="customerManagedEncryptionKey" /> | `string` | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. |
| <CopyableCode code="destinationConfig" /> | `object` | The configuration of the stream destination. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="errors" /> | `array` | Output only. Errors on the Stream. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="lastRecoveryTime" /> | `string` | Output only. If the stream was recovered, the time of the last recovery. Note: This field is currently experimental. |
| <CopyableCode code="sourceConfig" /> | `object` | The configuration of the stream source. |
| <CopyableCode code="state" /> | `string` | The state of the stream. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update time of the stream. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to get details about a stream. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list streams in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to create a stream. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to delete a stream. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to update the configuration of a stream. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to start, resume or recover a stream with a non default CDC strategy. |

## `SELECT` examples

Use this method to list streams in a project and location.

```sql
SELECT
name,
backfillAll,
backfillNone,
createTime,
customerManagedEncryptionKey,
destinationConfig,
displayName,
errors,
labels,
lastRecoveryTime,
sourceConfig,
state,
updateTime
FROM google.datastream.streams
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streams</code> resource.

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
INSERT INTO google.datastream.streams (
locationsId,
projectsId,
labels,
displayName,
sourceConfig,
destinationConfig,
state,
backfillAll,
backfillNone,
customerManagedEncryptionKey
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ displayName }}',
'{{ sourceConfig }}',
'{{ destinationConfig }}',
'{{ state }}',
'{{ backfillAll }}',
'{{ backfillNone }}',
'{{ customerManagedEncryptionKey }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
labels: object
displayName: string
sourceConfig:
  sourceConnectionProfile: string
  oracleSourceConfig:
    includeObjects:
      oracleSchemas:
        - schema: string
          oracleTables:
            - table: string
              oracleColumns:
                - column: string
                  dataType: string
                  length: integer
                  precision: integer
                  scale: integer
                  encoding: string
                  primaryKey: boolean
                  nullable: boolean
                  ordinalPosition: integer
    maxConcurrentCdcTasks: integer
    maxConcurrentBackfillTasks: integer
    dropLargeObjects: {}
    streamLargeObjects: {}
  mysqlSourceConfig:
    includeObjects:
      mysqlDatabases:
        - database: string
          mysqlTables:
            - table: string
              mysqlColumns:
                - column: string
                  dataType: string
                  length: integer
                  collation: string
                  primaryKey: boolean
                  nullable: boolean
                  ordinalPosition: integer
                  precision: integer
                  scale: integer
    maxConcurrentCdcTasks: integer
    maxConcurrentBackfillTasks: integer
  postgresqlSourceConfig:
    includeObjects:
      postgresqlSchemas:
        - schema: string
          postgresqlTables:
            - table: string
              postgresqlColumns:
                - column: string
                  dataType: string
                  length: integer
                  precision: integer
                  scale: integer
                  primaryKey: boolean
                  nullable: boolean
                  ordinalPosition: integer
    replicationSlot: string
    publication: string
    maxConcurrentBackfillTasks: integer
  sqlServerSourceConfig:
    includeObjects:
      schemas:
        - schema: string
          tables:
            - table: string
              columns:
                - column: string
                  dataType: string
                  length: integer
                  precision: integer
                  scale: integer
                  primaryKey: boolean
                  nullable: boolean
                  ordinalPosition: integer
    maxConcurrentCdcTasks: integer
    maxConcurrentBackfillTasks: integer
    transactionLogs: {}
    changeTables: {}
destinationConfig:
  destinationConnectionProfile: string
  gcsDestinationConfig:
    path: string
    fileRotationMb: integer
    fileRotationInterval: string
    avroFileFormat: {}
    jsonFileFormat:
      schemaFileFormat: string
      compression: string
  bigqueryDestinationConfig:
    singleTargetDataset:
      datasetId: string
    sourceHierarchyDatasets:
      datasetTemplate:
        location: string
        datasetIdPrefix: string
        kmsKeyName: string
    dataFreshness: string
    merge: {}
    appendOnly: {}
state: string
backfillAll: {}
backfillNone: {}
errors:
  - reason: string
    errorUuid: string
    message: string
    errorTime: string
    details: object
customerManagedEncryptionKey: string
lastRecoveryTime: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>streams</code> resource.

```sql
/*+ update */
UPDATE google.datastream.streams
SET 
labels = '{{ labels }}',
displayName = '{{ displayName }}',
sourceConfig = '{{ sourceConfig }}',
destinationConfig = '{{ destinationConfig }}',
state = '{{ state }}',
backfillAll = '{{ backfillAll }}',
backfillNone = '{{ backfillNone }}',
customerManagedEncryptionKey = '{{ customerManagedEncryptionKey }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND streamsId = '{{ streamsId }}';
```

## `DELETE` example

Deletes the specified <code>streams</code> resource.

```sql
/*+ delete */
DELETE FROM google.datastream.streams
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND streamsId = '{{ streamsId }}';
```
