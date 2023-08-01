---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datacatalog.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Pagination token of the next results page. Empty if there are no more items in results. |
| `tags` | `array` | Tag details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_entry_groups_entries_tags_list` | `SELECT` | `entriesId, entryGroupsId, locationsId, projectsId` | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| `projects_locations_entry_groups_tags_list` | `SELECT` | `entryGroupsId, locationsId, projectsId` | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| `projects_locations_entry_groups_entries_tags_create` | `INSERT` | `entriesId, entryGroupsId, locationsId, projectsId` | Creates a tag and assigns it to: * An Entry if the method name is `projects.locations.entryGroups.entries.tags.create`. * Or EntryGroupif the method name is `projects.locations.entryGroups.tags.create`. Note: The project identified by the `parent` parameter for the [tag] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be in the same organization. |
| `projects_locations_entry_groups_tags_create` | `INSERT` | `entryGroupsId, locationsId, projectsId` | Creates a tag and assigns it to: * An Entry if the method name is `projects.locations.entryGroups.entries.tags.create`. * Or EntryGroupif the method name is `projects.locations.entryGroups.tags.create`. Note: The project identified by the `parent` parameter for the [tag] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be in the same organization. |
| `projects_locations_entry_groups_entries_tags_delete` | `DELETE` | `entriesId, entryGroupsId, locationsId, projectsId, tagsId` | Deletes a tag. |
| `projects_locations_entry_groups_tags_delete` | `DELETE` | `entryGroupsId, locationsId, projectsId, tagsId` | Deletes a tag. |
| `projects_locations_entry_groups_entries_tags_patch` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId, tagsId` | Updates an existing tag. |
| `projects_locations_entry_groups_entries_tags_reconcile` | `EXEC` | `entriesId, entryGroupsId, locationsId, projectsId` | `ReconcileTags` creates or updates a list of tags on the entry. If the ReconcileTagsRequest.force_delete_missing parameter is set, the operation deletes tags not included in the input tag list. `ReconcileTags` returns a long-running operation resource that can be queried with Operations.GetOperation to return ReconcileTagsMetadata and a ReconcileTagsResponse message. |
| `projects_locations_entry_groups_tags_patch` | `EXEC` | `entryGroupsId, locationsId, projectsId, tagsId` | Updates an existing tag. |
