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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datacatalog.entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of an entry in URL format. Note: The entry itself and its child resources might not be stored in the location specified in its name. |
| `description` | `string` | Entry description that can consist of several sentences or paragraphs that describe entry contents. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). The maximum size is 2000 bytes when encoded in UTF-8. Default value is an empty string. |
| `userSpecifiedType` | `string` | Custom entry type that doesn't match any of the values allowed for input and listed in the `EntryType` enum. When creating an entry, first check the type values in the enum. If there are no appropriate types for the new entry, provide a custom value, for example, `my_special_type`. The `user_specified_type` string has the following limitations: * Is case insensitive. * Must begin with a letter or underscore. * Can only contain letters, numbers, and underscores. * Must be at least 1 character and at most 64 characters long. |
| `sourceSystemTimestamps` | `object` | Timestamps associated with this resource in a particular system. |
| `cloudBigtableSystemSpec` | `object` | Specification that applies to all entries that are part of `CLOUD_BIGTABLE` system (user_specified_type) |
| `datasetSpec` | `object` | Specification that applies to a dataset. Valid only for entries with the `DATASET` type. |
| `dataSource` | `object` | Physical location of an entry. |
| `personalDetails` | `object` | Entry metadata relevant only to the user and private to them. |
| `sqlDatabaseSystemSpec` | `object` | Specification that applies to entries that are part `SQL_DATABASE` system (user_specified_type) |
| `filesetSpec` | `object` | Specification that applies to a fileset. Valid only for entries with the 'FILESET' type. |
| `gcsFilesetSpec` | `object` | Describes a Cloud Storage fileset entry. |
| `bigqueryDateShardedSpec` | `object` | Specification for a group of BigQuery tables with the `[prefix]YYYYMMDD` name pattern. For more information, see [Introduction to partitioned tables] (https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding). |
| `schema` | `object` | Represents a schema, for example, a BigQuery, GoogleSQL, or Avro schema. |
| `databaseTableSpec` | `object` | Specification that applies to a table resource. Valid only for entries with the `TABLE` type. |
| `linkedResource` | `string` | The resource this metadata entry refers to. For Google Cloud Platform resources, `linked_resource` is the [Full Resource Name] (https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is: `//bigquery.googleapis.com/projects/&#123;PROJECT_ID&#125;/datasets/&#123;DATASET_ID&#125;/tables/&#123;TABLE_ID&#125;` Output only when the entry is one of the types in the `EntryType` enum. For entries with a `user_specified_type`, this field is optional and defaults to an empty string. The resource string must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), periods (.), colons (:), slashes (/), dashes (-), and hashes (#). The maximum size is 200 bytes when encoded in UTF-8. |
| `integratedSystem` | `string` | Output only. Indicates the entry's source system that Data Catalog integrates with, such as BigQuery, Pub/Sub, or Dataproc Metastore. |
| `usageSignal` | `object` | The set of all usage signals that Data Catalog stores. Note: Usually, these signals are updated daily. In rare cases, an update may fail but will be performed again on the next day. |
| `fullyQualifiedName` | `string` | [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource. Set automatically for entries representing resources from synced systems. Settable only during creation, and read-only later. Can be used for search and lookup of the entries.  |
| `dataSourceConnectionSpec` | `object` | Specification that applies to a data source connection. Valid only for entries with the `DATA_SOURCE_CONNECTION` type. Only one of internal specs can be set at the time, and cannot be changed later. |
| `type` | `string` | The type of the entry. For details, see [`EntryType`](#entrytype). |
| `lookerSystemSpec` | `object` | Specification that applies to entries that are part `LOOKER` system (user_specified_type) |
| `displayName` | `string` | Display name of an entry. The maximum size is 500 bytes when encoded in UTF-8. Default value is an empty string. |
| `businessContext` | `object` | Business Context of the entry. |
| `serviceSpec` | `object` | Specification that applies to a Service resource. Valid only for entries with the `SERVICE` type. |
| `labels` | `object` | Cloud labels attached to the entry. In Data Catalog, you can create and modify labels attached only to custom entries. Synced entries have unmodifiable labels that come from the source system. |
| `routineSpec` | `object` | Specification that applies to a routine. Valid only for entries with the `ROUTINE` type. |
| `modelSpec` | `object` | Specification that applies to a model. Valid only for entries with the `MODEL` type. |
| `userSpecifiedSystem` | `string` | Indicates the entry's source system that Data Catalog doesn't automatically integrate with. The `user_specified_system` string has the following limitations: * Is case insensitive. * Must begin with a letter or underscore. * Can only contain letters, numbers, and underscores. * Must be at least 1 character and at most 64 characters long. |
| `bigqueryTableSpec` | `object` | Describes a BigQuery table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_entry_groups_entries_list` | `SELECT` | `entryGroupsId, locationsId, projectsId` | Lists entries. Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use SearchCatalog. |
| `projects_locations_entry_groups_entries_create` | `INSERT` | `entryGroupsId, locationsId, projectsId` | Creates an entry. You can create entries only with 'FILESET', 'CLUSTER', 'DATA_STREAM', or custom types. Data Catalog automatically creates entries with other types during metadata ingestion from integrated systems. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). An entry group can have a maximum of 100,000 entries. |
| `projects_locations_entry_groups_entries_delete` | `DELETE` | `entriesId, entryGroupsId, locationsId, projectsId` | Deletes an existing entry. You can delete only the entries created by the CreateEntry method. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| `_projects_locations_entry_groups_entries_list` | `EXEC` | `entryGroupsId, locationsId, projectsId` | Lists entries. Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use SearchCatalog. |
| `entries_lookup` | `EXEC` |  | Gets an entry by its target resource name. The resource name comes from the source Google Cloud Platform service. |
| `projects_locations_entry_groups_entries_get` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Gets an entry. |
| `projects_locations_entry_groups_entries_import` | `EXEC` | `entryGroupsId, locationsId, projectsId` | Imports entries from a source, such as data previously dumped into a Cloud Storage bucket, into Data Catalog. Import of entries is a sync operation that reconciles the state of the third-party system with the Data Catalog. `ImportEntries` accepts source data snapshots of a third-party system. Snapshot should be delivered as a .wire or base65-encoded .txt file containing a sequence of Protocol Buffer messages of DumpItem type. `ImportEntries` returns a long-running operation resource that can be queried with Operations.GetOperation to return ImportEntriesMetadata and an ImportEntriesResponse message. |
| `projects_locations_entry_groups_entries_modify_entry_contacts` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Modifies contacts, part of the business context of an Entry. To call this method, you must have the `datacatalog.entries.updateContacts` IAM permission on the corresponding project. |
| `projects_locations_entry_groups_entries_modify_entry_overview` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Modifies entry overview, part of the business context of an Entry. To call this method, you must have the `datacatalog.entries.updateOverview` IAM permission on the corresponding project. |
| `projects_locations_entry_groups_entries_patch` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Updates an existing entry. You must enable the Data Catalog API in the project identified by the `entry.name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| `projects_locations_entry_groups_entries_star` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Marks an Entry as starred by the current user. Starring information is private to each user. |
| `projects_locations_entry_groups_entries_unstar` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Marks an Entry as NOT starred by the current user. Starring information is private to each user. |
