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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: displayName
      value: string
    - name: sourceConfig
      value:
        - name: sourceConnectionProfile
          value: string
        - name: oracleSourceConfig
          value:
            - name: includeObjects
              value:
                - name: oracleSchemas
                  value:
                    - - name: schema
                        value: string
                      - name: oracleTables
                        value:
                          - - name: table
                              value: string
                            - name: oracleColumns
                              value:
                                - - name: column
                                    value: string
                                  - name: dataType
                                    value: string
                                  - name: length
                                    value: integer
                                  - name: precision
                                    value: integer
                                  - name: scale
                                    value: integer
                                  - name: encoding
                                    value: string
                                  - name: primaryKey
                                    value: boolean
                                  - name: nullable
                                    value: boolean
                                  - name: ordinalPosition
                                    value: integer
            - name: maxConcurrentCdcTasks
              value: integer
            - name: maxConcurrentBackfillTasks
              value: integer
            - name: dropLargeObjects
              value: []
            - name: streamLargeObjects
              value: []
        - name: mysqlSourceConfig
          value:
            - name: includeObjects
              value:
                - name: mysqlDatabases
                  value:
                    - - name: database
                        value: string
                      - name: mysqlTables
                        value:
                          - - name: table
                              value: string
                            - name: mysqlColumns
                              value:
                                - - name: column
                                    value: string
                                  - name: dataType
                                    value: string
                                  - name: length
                                    value: integer
                                  - name: collation
                                    value: string
                                  - name: primaryKey
                                    value: boolean
                                  - name: nullable
                                    value: boolean
                                  - name: ordinalPosition
                                    value: integer
                                  - name: precision
                                    value: integer
                                  - name: scale
                                    value: integer
            - name: maxConcurrentCdcTasks
              value: integer
            - name: maxConcurrentBackfillTasks
              value: integer
        - name: postgresqlSourceConfig
          value:
            - name: includeObjects
              value:
                - name: postgresqlSchemas
                  value:
                    - - name: schema
                        value: string
                      - name: postgresqlTables
                        value:
                          - - name: table
                              value: string
                            - name: postgresqlColumns
                              value:
                                - - name: column
                                    value: string
                                  - name: dataType
                                    value: string
                                  - name: length
                                    value: integer
                                  - name: precision
                                    value: integer
                                  - name: scale
                                    value: integer
                                  - name: primaryKey
                                    value: boolean
                                  - name: nullable
                                    value: boolean
                                  - name: ordinalPosition
                                    value: integer
            - name: replicationSlot
              value: string
            - name: publication
              value: string
            - name: maxConcurrentBackfillTasks
              value: integer
        - name: sqlServerSourceConfig
          value:
            - name: includeObjects
              value:
                - name: schemas
                  value:
                    - - name: schema
                        value: string
                      - name: tables
                        value:
                          - - name: table
                              value: string
                            - name: columns
                              value:
                                - - name: column
                                    value: string
                                  - name: dataType
                                    value: string
                                  - name: length
                                    value: integer
                                  - name: precision
                                    value: integer
                                  - name: scale
                                    value: integer
                                  - name: primaryKey
                                    value: boolean
                                  - name: nullable
                                    value: boolean
                                  - name: ordinalPosition
                                    value: integer
            - name: maxConcurrentCdcTasks
              value: integer
            - name: maxConcurrentBackfillTasks
              value: integer
            - name: transactionLogs
              value: []
            - name: changeTables
              value: []
    - name: destinationConfig
      value:
        - name: destinationConnectionProfile
          value: string
        - name: gcsDestinationConfig
          value:
            - name: path
              value: string
            - name: fileRotationMb
              value: integer
            - name: fileRotationInterval
              value: string
            - name: avroFileFormat
              value: []
            - name: jsonFileFormat
              value:
                - name: schemaFileFormat
                  value: string
                - name: compression
                  value: string
        - name: bigqueryDestinationConfig
          value:
            - name: singleTargetDataset
              value:
                - name: datasetId
                  value: string
            - name: sourceHierarchyDatasets
              value:
                - name: datasetTemplate
                  value:
                    - name: location
                      value: string
                    - name: datasetIdPrefix
                      value: string
                    - name: kmsKeyName
                      value: string
            - name: dataFreshness
              value: string
            - name: merge
              value: []
            - name: appendOnly
              value: []
    - name: state
      value: string
    - name: backfillAll
      value: []
    - name: backfillNone
      value: []
    - name: errors
      value:
        - - name: reason
            value: string
          - name: errorUuid
            value: string
          - name: message
            value: string
          - name: errorTime
            value: string
          - name: details
            value: object
    - name: customerManagedEncryptionKey
      value: string
    - name: lastRecoveryTime
      value: string

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
