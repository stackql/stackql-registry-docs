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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datacatalog.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the tag in URL format where tag ID is a system-generated identifier. Note: The tag itself might not be stored in the location specified in its name. |
| <CopyableCode code="column" /> | `string` | Resources like entry can have schemas associated with them. This scope allows you to attach tags to an individual column based on that schema. To attach a tag to a nested column, separate column names with a dot (`.`). Example: `column.nested_column`. |
| <CopyableCode code="fields" /> | `object` | Required. Maps the ID of a tag field to its value and additional information about that field. Tag template defines valid field IDs. A tag must have at least 1 field and at most 500 fields. |
| <CopyableCode code="template" /> | `string` | Required. The resource name of the tag template this tag uses. Example: `projects/&#123;PROJECT_ID&#125;/locations/&#123;LOCATION&#125;/tagTemplates/&#123;TAG_TEMPLATE_ID&#125;` This field cannot be modified after creation. |
| <CopyableCode code="templateDisplayName" /> | `string` | Output only. The display name of the tag template. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_entries_tags_list" /> | `SELECT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| <CopyableCode code="projects_locations_entry_groups_tags_list" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_create" /> | `INSERT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Creates a tag and assigns it to: * An Entry if the method name is `projects.locations.entryGroups.entries.tags.create`. * Or EntryGroupif the method name is `projects.locations.entryGroups.tags.create`. Note: The project identified by the `parent` parameter for the [tag] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be in the same organization. |
| <CopyableCode code="projects_locations_entry_groups_tags_create" /> | `INSERT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Creates a tag and assigns it to: * An Entry if the method name is `projects.locations.entryGroups.entries.tags.create`. * Or EntryGroupif the method name is `projects.locations.entryGroups.tags.create`. Note: The project identified by the `parent` parameter for the [tag] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template] (https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be in the same organization. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_delete" /> | `DELETE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId, tagsId" /> | Deletes a tag. |
| <CopyableCode code="projects_locations_entry_groups_tags_delete" /> | `DELETE` | <CopyableCode code="entryGroupsId, locationsId, projectsId, tagsId" /> | Deletes a tag. |
| <CopyableCode code="_projects_locations_entry_groups_entries_tags_list" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| <CopyableCode code="_projects_locations_entry_groups_tags_list" /> | `EXEC` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists tags assigned to an Entry. The columns in the response are lowercased. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_patch" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId, tagsId" /> | Updates an existing tag. |
| <CopyableCode code="projects_locations_entry_groups_entries_tags_reconcile" /> | `EXEC` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | `ReconcileTags` creates or updates a list of tags on the entry. If the ReconcileTagsRequest.force_delete_missing parameter is set, the operation deletes tags not included in the input tag list. `ReconcileTags` returns a long-running operation resource that can be queried with Operations.GetOperation to return ReconcileTagsMetadata and a ReconcileTagsResponse message. |
| <CopyableCode code="projects_locations_entry_groups_tags_patch" /> | `EXEC` | <CopyableCode code="entryGroupsId, locationsId, projectsId, tagsId" /> | Updates an existing tag. |
