---
title: entry_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - entry_groups
  - dataplex
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
<tr><td><b>Name</b></td><td><code>entry_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.entry_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the EntryGroup, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/entryGroups/&#123;entry_group_id&#125;. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the EntryGroup. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the EntryGroup was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the EntryGroup. |
| <CopyableCode code="transferStatus" /> | `string` | Output only. Denotes the transfer status of the Entry Group. It is unspecified for Entry Group created from Dataplex API. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the EntryGroup. This ID will be different if the EntryGroup is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the EntryGroup was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_get" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Retrieves a EntryGroup resource. |
| <CopyableCode code="projects_locations_entry_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists EntryGroup resources in a project and location. |
| <CopyableCode code="projects_locations_entry_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an EntryGroup |
| <CopyableCode code="projects_locations_entry_groups_delete" /> | `DELETE` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Deletes a EntryGroup resource. |
| <CopyableCode code="projects_locations_entry_groups_patch" /> | `UPDATE` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Updates a EntryGroup resource. |
| <CopyableCode code="_projects_locations_entry_groups_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists EntryGroup resources in a project and location. |
