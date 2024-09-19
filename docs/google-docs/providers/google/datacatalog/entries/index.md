---
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
  - datacatalog
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

Creates, updates, deletes, gets or lists a <code>entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name of an entry in URL format. Note: The entry itself and its child resources might not be stored in the location specified in its name. |
| <CopyableCode code="description" /> | `string` | Entry description that can consist of several sentences or paragraphs that describe entry contents. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). The maximum size is 2000 bytes when encoded in UTF-8. Default value is an empty string. |
| <CopyableCode code="bigqueryDateShardedSpec" /> | `object` | Specification for a group of BigQuery tables with the `[prefix]YYYYMMDD` name pattern. For more information, see [Introduction to partitioned tables] (https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding). |
| <CopyableCode code="bigqueryTableSpec" /> | `object` | Describes a BigQuery table. |
| <CopyableCode code="businessContext" /> | `object` | Business Context of the entry. |
| <CopyableCode code="cloudBigtableSystemSpec" /> | `object` | Specification that applies to all entries that are part of `CLOUD_BIGTABLE` system (user_specified_type) |
| <CopyableCode code="dataSource" /> | `object` | Physical location of an entry. |
| <CopyableCode code="dataSourceConnectionSpec" /> | `object` | Specification that applies to a data source connection. Valid only for entries with the `DATA_SOURCE_CONNECTION` type. Only one of internal specs can be set at the time, and cannot be changed later. |
| <CopyableCode code="databaseTableSpec" /> | `object` | Specification that applies to a table resource. Valid only for entries with the `TABLE` type. |
| <CopyableCode code="datasetSpec" /> | `object` | Specification that applies to a dataset. Valid only for entries with the `DATASET` type. |
| <CopyableCode code="displayName" /> | `string` | Display name of an entry. The maximum size is 500 bytes when encoded in UTF-8. Default value is an empty string. |
| <CopyableCode code="featureOnlineStoreSpec" /> | `object` | Detail description of the source information of a Vertex Feature Online Store. |
| <CopyableCode code="filesetSpec" /> | `object` | Specification that applies to a fileset. Valid only for entries with the 'FILESET' type. |
| <CopyableCode code="fullyQualifiedName" /> | `string` | [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource. Set automatically for entries representing resources from synced systems. Settable only during creation, and read-only later. Can be used for search and lookup of the entries.  |
| <CopyableCode code="gcsFilesetSpec" /> | `object` | Describes a Cloud Storage fileset entry. |
| <CopyableCode code="integratedSystem" /> | `string` | Output only. Indicates the entry's source system that Data Catalog integrates with, such as BigQuery, Pub/Sub, or Dataproc Metastore. |
| <CopyableCode code="labels" /> | `object` | Cloud labels attached to the entry. In Data Catalog, you can create and modify labels attached only to custom entries. Synced entries have unmodifiable labels that come from the source system. |
| <CopyableCode code="linkedResource" /> | `string` | The resource this metadata entry refers to. For Google Cloud Platform resources, `linked_resource` is the [Full Resource Name] (https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is: `//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}` Output only when the entry is one of the types in the `EntryType` enum. For entries with a `user_specified_type`, this field is optional and defaults to an empty string. The resource string must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), periods (.), colons (:), slashes (/), dashes (-), and hashes (#). The maximum size is 200 bytes when encoded in UTF-8. |
| <CopyableCode code="lookerSystemSpec" /> | `object` | Specification that applies to entries that are part `LOOKER` system (user_specified_type) |
| <CopyableCode code="modelSpec" /> | `object` | Specification that applies to a model. Valid only for entries with the `MODEL` type. |
| <CopyableCode code="personalDetails" /> | `object` | Entry metadata relevant only to the user and private to them. |
| <CopyableCode code="routineSpec" /> | `object` | Specification that applies to a routine. Valid only for entries with the `ROUTINE` type. |
| <CopyableCode code="schema" /> | `object` | Represents a schema, for example, a BigQuery, GoogleSQL, or Avro schema. |
| <CopyableCode code="serviceSpec" /> | `object` | Specification that applies to a Service resource. Valid only for entries with the `SERVICE` type. |
| <CopyableCode code="sourceSystemTimestamps" /> | `object` | Timestamps associated with this resource in a particular system. |
| <CopyableCode code="sqlDatabaseSystemSpec" /> | `object` | Specification that applies to entries that are part `SQL_DATABASE` system (user_specified_type) |
| <CopyableCode code="type" /> | `string` | The type of the entry. For details, see [`EntryType`](#entrytype). |
| <CopyableCode code="usageSignal" /> | `object` | The set of all usage signals that Data Catalog stores. Note: Usually, these signals are updated daily. In rare cases, an update may fail but will be performed again on the next day. |
| <CopyableCode code="userSpecifiedSystem" /> | `string` | Indicates the entry's source system that Data Catalog doesn't automatically integrate with. The `user_specified_system` string has the following limitations: * Is case insensitive. * Must begin with a letter or underscore. * Can only contain letters, numbers, and underscores. * Must be at least 1 character and at most 64 characters long. |
| <CopyableCode code="userSpecifiedType" /> | `string` | Custom entry type that doesn't match any of the values allowed for input and listed in the `EntryType` enum. When creating an entry, first check the type values in the enum. If there are no appropriate types for the new entry, provide a custom value, for example, `my_special_type`. The `user_specified_type` string has the following limitations: * Is case insensitive. * Must begin with a letter or underscore. * Can only contain letters, numbers, and underscores. * Must be at least 1 character and at most 64 characters long. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_entries_get" /> | `SELECT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Gets an entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_list" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists entries. Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use SearchCatalog. |
| <CopyableCode code="projects_locations_entry_groups_entries_create" /> | `INSERT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Creates an entry. You can create entries only with 'FILESET', 'CLUSTER', 'DATA_STREAM', or custom types. Data Catalog automatically creates entries with other types during metadata ingestion from integrated systems. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). An entry group can have a maximum of 100,000 entries. |
| <CopyableCode code="projects_locations_entry_groups_entries_delete" /> | `DELETE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Deletes an existing entry. You can delete only the entries created by the CreateEntry method. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_entry_groups_entries_patch" /> | `UPDATE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Updates an existing entry. You must enable the Data Catalog API in the project identified by the `entry.name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="entries_lookup" /> | `EXEC` | <CopyableCode code="" /> | Gets an entry by its target resource name. The resource name comes from the source Google Cloud Platform service. |
| <CopyableCode code="projects_locations_entry_groups_entries_import" /> | `EXEC` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Imports entries from a source, such as data previously dumped into a Cloud Storage bucket, into Data Catalog. Import of entries is a sync operation that reconciles the state of the third-party system with the Data Catalog. `ImportEntries` accepts source data snapshots of a third-party system. Snapshot should be delivered as a .wire or base65-encoded .txt file containing a sequence of Protocol Buffer messages of DumpItem type. `ImportEntries` returns a long-running operation resource that can be queried with Operations.GetOperation to return ImportEntriesMetadata and an ImportEntriesResponse message. |
| <CopyableCode code="projects_locations_entry_groups_entries_modify_entry_contacts" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Modifies contacts, part of the business context of an Entry. To call this method, you must have the `datacatalog.entries.updateContacts` IAM permission on the corresponding project. |
| <CopyableCode code="projects_locations_entry_groups_entries_modify_entry_overview" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Modifies entry overview, part of the business context of an Entry. To call this method, you must have the `datacatalog.entries.updateOverview` IAM permission on the corresponding project. |
| <CopyableCode code="projects_locations_entry_groups_entries_star" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Marks an Entry as starred by the current user. Starring information is private to each user. |
| <CopyableCode code="projects_locations_entry_groups_entries_unstar" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Marks an Entry as NOT starred by the current user. Starring information is private to each user. |

## `SELECT` examples

Lists entries. Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use SearchCatalog.

```sql
SELECT
name,
description,
bigqueryDateShardedSpec,
bigqueryTableSpec,
businessContext,
cloudBigtableSystemSpec,
dataSource,
dataSourceConnectionSpec,
databaseTableSpec,
datasetSpec,
displayName,
featureOnlineStoreSpec,
filesetSpec,
fullyQualifiedName,
gcsFilesetSpec,
integratedSystem,
labels,
linkedResource,
lookerSystemSpec,
modelSpec,
personalDetails,
routineSpec,
schema,
serviceSpec,
sourceSystemTimestamps,
sqlDatabaseSystemSpec,
type,
usageSignal,
userSpecifiedSystem,
userSpecifiedType
FROM google.datacatalog.entries
WHERE entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entries</code> resource.

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
INSERT INTO google.datacatalog.entries (
entryGroupsId,
locationsId,
projectsId,
linkedResource,
fullyQualifiedName,
type,
userSpecifiedType,
userSpecifiedSystem,
sqlDatabaseSystemSpec,
lookerSystemSpec,
cloudBigtableSystemSpec,
gcsFilesetSpec,
databaseTableSpec,
dataSourceConnectionSpec,
routineSpec,
datasetSpec,
filesetSpec,
serviceSpec,
modelSpec,
featureOnlineStoreSpec,
displayName,
description,
businessContext,
schema,
sourceSystemTimestamps,
usageSignal,
labels
)
SELECT 
'{{ entryGroupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ linkedResource }}',
'{{ fullyQualifiedName }}',
'{{ type }}',
'{{ userSpecifiedType }}',
'{{ userSpecifiedSystem }}',
'{{ sqlDatabaseSystemSpec }}',
'{{ lookerSystemSpec }}',
'{{ cloudBigtableSystemSpec }}',
'{{ gcsFilesetSpec }}',
'{{ databaseTableSpec }}',
'{{ dataSourceConnectionSpec }}',
'{{ routineSpec }}',
'{{ datasetSpec }}',
'{{ filesetSpec }}',
'{{ serviceSpec }}',
'{{ modelSpec }}',
'{{ featureOnlineStoreSpec }}',
'{{ displayName }}',
'{{ description }}',
'{{ businessContext }}',
'{{ schema }}',
'{{ sourceSystemTimestamps }}',
'{{ usageSignal }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: linkedResource
      value: string
    - name: fullyQualifiedName
      value: string
    - name: type
      value: string
    - name: userSpecifiedType
      value: string
    - name: integratedSystem
      value: string
    - name: userSpecifiedSystem
      value: string
    - name: sqlDatabaseSystemSpec
      value:
        - name: sqlEngine
          value: string
        - name: databaseVersion
          value: string
        - name: instanceHost
          value: string
    - name: lookerSystemSpec
      value:
        - name: parentInstanceId
          value: string
        - name: parentInstanceDisplayName
          value: string
        - name: parentModelId
          value: string
        - name: parentModelDisplayName
          value: string
        - name: parentViewId
          value: string
        - name: parentViewDisplayName
          value: string
    - name: cloudBigtableSystemSpec
      value:
        - name: instanceDisplayName
          value: string
    - name: gcsFilesetSpec
      value:
        - name: filePatterns
          value:
            - string
        - name: sampleGcsFileSpecs
          value:
            - - name: filePath
                value: string
              - name: gcsTimestamps
                value:
                  - name: createTime
                    value: string
                  - name: updateTime
                    value: string
                  - name: expireTime
                    value: string
              - name: sizeBytes
                value: string
    - name: bigqueryTableSpec
      value:
        - name: tableSourceType
          value: string
        - name: viewSpec
          value:
            - name: viewQuery
              value: string
        - name: tableSpec
          value:
            - name: groupedEntry
              value: string
    - name: bigqueryDateShardedSpec
      value:
        - name: dataset
          value: string
        - name: tablePrefix
          value: string
        - name: shardCount
          value: string
        - name: latestShardResource
          value: string
    - name: databaseTableSpec
      value:
        - name: type
          value: string
        - name: dataplexTable
          value:
            - name: externalTables
              value:
                - - name: system
                    value: string
                  - name: fullyQualifiedName
                    value: string
                  - name: googleCloudResource
                    value: string
                  - name: dataCatalogEntry
                    value: string
            - name: dataplexSpec
              value:
                - name: asset
                  value: string
                - name: dataFormat
                  value:
                    - name: avro
                      value:
                        - name: text
                          value: string
                    - name: thrift
                      value:
                        - name: text
                          value: string
                    - name: protobuf
                      value:
                        - name: text
                          value: string
                    - name: parquet
                      value: []
                    - name: orc
                      value: []
                    - name: csv
                      value: []
                - name: compressionFormat
                  value: string
                - name: projectId
                  value: string
            - name: userManaged
              value: boolean
        - name: databaseViewSpec
          value:
            - name: viewType
              value: string
            - name: baseTable
              value: string
            - name: sqlQuery
              value: string
    - name: dataSourceConnectionSpec
      value:
        - name: bigqueryConnectionSpec
          value:
            - name: connectionType
              value: string
            - name: cloudSql
              value:
                - name: instanceId
                  value: string
                - name: database
                  value: string
                - name: type
                  value: string
            - name: hasCredential
              value: boolean
    - name: routineSpec
      value:
        - name: routineType
          value: string
        - name: language
          value: string
        - name: routineArguments
          value:
            - - name: name
                value: string
              - name: mode
                value: string
              - name: type
                value: string
        - name: returnType
          value: string
        - name: definitionBody
          value: string
        - name: bigqueryRoutineSpec
          value:
            - name: importedLibraries
              value:
                - string
    - name: datasetSpec
      value:
        - name: vertexDatasetSpec
          value:
            - name: dataItemCount
              value: string
            - name: dataType
              value: string
    - name: filesetSpec
      value:
        - name: dataplexFileset
          value: []
    - name: serviceSpec
      value:
        - name: cloudBigtableInstanceSpec
          value:
            - name: cloudBigtableClusterSpecs
              value:
                - - name: displayName
                    value: string
                  - name: location
                    value: string
                  - name: type
                    value: string
                  - name: linkedResource
                    value: string
    - name: modelSpec
      value:
        - name: vertexModelSpec
          value:
            - name: versionId
              value: string
            - name: versionAliases
              value:
                - string
            - name: versionDescription
              value: string
            - name: vertexModelSourceInfo
              value:
                - name: sourceType
                  value: string
                - name: copy
                  value: boolean
            - name: containerImageUri
              value: string
    - name: featureOnlineStoreSpec
      value:
        - name: storageType
          value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: businessContext
      value:
        - name: entryOverview
          value:
            - name: overview
              value: string
        - name: contacts
          value:
            - name: people
              value:
                - - name: designation
                    value: string
                  - name: email
                    value: string
    - name: schema
      value:
        - name: columns
          value:
            - - name: column
                value: string
              - name: type
                value: string
              - name: description
                value: string
              - name: mode
                value: string
              - name: defaultValue
                value: string
              - name: ordinalPosition
                value: integer
              - name: highestIndexingType
                value: string
              - name: subcolumns
                value:
                  - - name: column
                      value: string
                    - name: type
                      value: string
                    - name: description
                      value: string
                    - name: mode
                      value: string
                    - name: defaultValue
                      value: string
                    - name: ordinalPosition
                      value: integer
                    - name: highestIndexingType
                      value: string
                    - name: subcolumns
                      value:
                        - - name: column
                            value: string
                          - name: type
                            value: string
                          - name: description
                            value: string
                          - name: mode
                            value: string
                          - name: defaultValue
                            value: string
                          - name: ordinalPosition
                            value: integer
                          - name: highestIndexingType
                            value: string
                          - name: subcolumns
                            value:
                              - - name: column
                                  value: string
                                - name: type
                                  value: string
                                - name: description
                                  value: string
                                - name: mode
                                  value: string
                                - name: defaultValue
                                  value: string
                                - name: ordinalPosition
                                  value: integer
                                - name: highestIndexingType
                                  value: string
                                - name: subcolumns
                                  value:
                                    - - name: column
                                        value: string
                                      - name: type
                                        value: string
                                      - name: description
                                        value: string
                                      - name: mode
                                        value: string
                                      - name: defaultValue
                                        value: string
                                      - name: ordinalPosition
                                        value: integer
                                      - name: highestIndexingType
                                        value: string
                                      - name: subcolumns
                                        value:
                                          - - name: column
                                              value: string
                                            - name: type
                                              value: string
                                            - name: description
                                              value: string
                                            - name: mode
                                              value: string
                                            - name: defaultValue
                                              value: string
                                            - name: ordinalPosition
                                              value: integer
                                            - name: highestIndexingType
                                              value: string
                                            - name: subcolumns
                                              value:
                                                - - name: column
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: description
                                                    value: string
                                                  - name: mode
                                                    value: string
                                                  - name: defaultValue
                                                    value: string
                                                  - name: ordinalPosition
                                                    value: integer
                                                  - name: highestIndexingType
                                                    value: string
                                                  - name: subcolumns
                                                    value:
                                                      - - name: column
                                                          value: string
                                                        - name: type
                                                          value: string
                                                        - name: description
                                                          value: string
                                                        - name: mode
                                                          value: string
                                                        - name: defaultValue
                                                          value: string
                                                        - name: ordinalPosition
                                                          value: integer
                                                        - name: highestIndexingType
                                                          value: string
                                                        - name: subcolumns
                                                          value:
                                                            - - name: column
                                                                value: string
                                                              - name: type
                                                                value: string
                                                              - name: description
                                                                value: string
                                                              - name: mode
                                                                value: string
                                                              - name: defaultValue
                                                                value: string
                                                              - name: ordinalPosition
                                                                value: integer
                                                              - name: highestIndexingType
                                                                value: string
                                                              - name: subcolumns
                                                                value:
                                                                  - []
                                                              - name: lookerColumnSpec
                                                                value: []
                                                              - name: rangeElementType
                                                                value: []
                                                              - name: gcRule
                                                                value: string
                                                        - name: gcRule
                                                          value: string
                                                  - name: gcRule
                                                    value: string
                                            - name: gcRule
                                              value: string
                                      - name: gcRule
                                        value: string
                                - name: gcRule
                                  value: string
                          - name: gcRule
                            value: string
                    - name: gcRule
                      value: string
              - name: gcRule
                value: string
    - name: usageSignal
      value:
        - name: updateTime
          value: string
        - name: usageWithinTimeRange
          value: object
        - name: commonUsageWithinTimeRange
          value: object
        - name: favoriteCount
          value: string
    - name: labels
      value: object
    - name: dataSource
      value:
        - name: service
          value: string
        - name: resource
          value: string
        - name: sourceEntry
          value: string
        - name: storageProperties
          value:
            - name: filePattern
              value:
                - string
            - name: fileType
              value: string
    - name: personalDetails
      value:
        - name: starred
          value: boolean
        - name: starTime
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>entries</code> resource.

```sql
/*+ update */
UPDATE google.datacatalog.entries
SET 
linkedResource = '{{ linkedResource }}',
fullyQualifiedName = '{{ fullyQualifiedName }}',
type = '{{ type }}',
userSpecifiedType = '{{ userSpecifiedType }}',
userSpecifiedSystem = '{{ userSpecifiedSystem }}',
sqlDatabaseSystemSpec = '{{ sqlDatabaseSystemSpec }}',
lookerSystemSpec = '{{ lookerSystemSpec }}',
cloudBigtableSystemSpec = '{{ cloudBigtableSystemSpec }}',
gcsFilesetSpec = '{{ gcsFilesetSpec }}',
databaseTableSpec = '{{ databaseTableSpec }}',
dataSourceConnectionSpec = '{{ dataSourceConnectionSpec }}',
routineSpec = '{{ routineSpec }}',
datasetSpec = '{{ datasetSpec }}',
filesetSpec = '{{ filesetSpec }}',
serviceSpec = '{{ serviceSpec }}',
modelSpec = '{{ modelSpec }}',
featureOnlineStoreSpec = '{{ featureOnlineStoreSpec }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
businessContext = '{{ businessContext }}',
schema = '{{ schema }}',
sourceSystemTimestamps = '{{ sourceSystemTimestamps }}',
usageSignal = '{{ usageSignal }}',
labels = '{{ labels }}'
WHERE 
entriesId = '{{ entriesId }}'
AND entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entries</code> resource.

```sql
/*+ delete */
DELETE FROM google.datacatalog.entries
WHERE entriesId = '{{ entriesId }}'
AND entryGroupsId = '{{ entryGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
