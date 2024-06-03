---
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
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
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The relative resource name of the Entry, of the form: projects/&#123;project&#125;/locations/&#123;location&#125;/entryGroups/&#123;entry_group&#125;/entries/&#123;entry&#125;. |
| <CopyableCode code="aspects" /> | `object` | Optional. The Aspects attached to the Entry. The format for the key can be one of the following: 1. &#123;projectId&#125;.&#123;locationId&#125;.&#123;aspectTypeId&#125; (if the aspect is attached directly to the entry) 2. &#123;projectId&#125;.&#123;locationId&#125;.&#123;aspectTypeId&#125;@&#123;path&#125; (if the aspect is attached to an entry's path) |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the Entry was created. |
| <CopyableCode code="entrySource" /> | `object` | EntrySource contains source system related information for the entry. |
| <CopyableCode code="entryType" /> | `string` | Required. Immutable. The resource name of the EntryType used to create this Entry. |
| <CopyableCode code="fullyQualifiedName" /> | `string` | Optional. A name for the entry that can reference it in an external system. The maximum size of the field is 4000 characters. |
| <CopyableCode code="parentEntry" /> | `string` | Optional. Immutable. The resource name of the parent entry. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the Entry was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_entry_groups_entries_get" /> | `SELECT` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Gets a single entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_list" /> | `SELECT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists entries within an entry group. |
| <CopyableCode code="projects_locations_entry_groups_entries_create" /> | `INSERT` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Creates an Entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_delete" /> | `DELETE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Deletes an Entry. |
| <CopyableCode code="projects_locations_entry_groups_entries_patch" /> | `UPDATE` | <CopyableCode code="entriesId, entryGroupsId, locationsId, projectsId" /> | Updates an Entry. |
| <CopyableCode code="_projects_locations_entry_groups_entries_list" /> | `EXEC` | <CopyableCode code="entryGroupsId, locationsId, projectsId" /> | Lists entries within an entry group. |
