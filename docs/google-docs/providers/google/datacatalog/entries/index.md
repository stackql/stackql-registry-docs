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
| `entries` | `array` | Entry details. |
| `nextPageToken` | `string` | Pagination token of the next results page. Empty if there are no more items in results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_entry_groups_entries_list` | `SELECT` | `entryGroupsId, locationsId, projectsId` | Lists entries. Note: Currently, this method can list only custom entries. To get a list of both custom and automatically created entries, use SearchCatalog. |
| `projects_locations_entry_groups_entries_create` | `INSERT` | `entryGroupsId, locationsId, projectsId` | Creates an entry. You can create entries only with 'FILESET', 'CLUSTER', 'DATA_STREAM', or custom types. Data Catalog automatically creates entries with other types during metadata ingestion from integrated systems. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). An entry group can have a maximum of 100,000 entries. |
| `projects_locations_entry_groups_entries_delete` | `DELETE` | `entriesId, entryGroupsId, locationsId, projectsId` | Deletes an existing entry. You can delete only the entries created by the CreateEntry method. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| `entries_lookup` | `EXEC` |  | Gets an entry by its target resource name. The resource name comes from the source Google Cloud Platform service. |
| `projects_locations_entry_groups_entries_get` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Gets an entry. |
| `projects_locations_entry_groups_entries_import` | `EXEC` | `entryGroupsId, locationsId, projectsId` | Imports entries from a source, such as data previously dumped into a Cloud Storage bucket, into Data Catalog. Import of entries is a sync operation that reconciles the state of the third-party system with the Data Catalog. `ImportEntries` accepts source data snapshots of a third-party system. Snapshot should be delivered as a .wire or base65-encoded .txt file containing a sequence of Protocol Buffer messages of DumpItem type. `ImportEntries` returns a long-running operation resource that can be queried with Operations.GetOperation to return ImportEntriesMetadata and an ImportEntriesResponse message. |
| `projects_locations_entry_groups_entries_modify_entry_contacts` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Modifies contacts, part of the business context of an Entry. To call this method, you must have the `datacatalog.entries.updateContacts` IAM permission on the corresponding project. |
| `projects_locations_entry_groups_entries_modify_entry_overview` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Modifies entry overview, part of the business context of an Entry. To call this method, you must have the `datacatalog.entries.updateOverview` IAM permission on the corresponding project. |
| `projects_locations_entry_groups_entries_patch` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Updates an existing entry. You must enable the Data Catalog API in the project identified by the `entry.name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| `projects_locations_entry_groups_entries_star` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Marks an Entry as starred by the current user. Starring information is private to each user. |
| `projects_locations_entry_groups_entries_unstar` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | Marks an Entry as NOT starred by the current user. Starring information is private to each user. |
