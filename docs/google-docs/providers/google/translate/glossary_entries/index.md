---
title: glossary_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - glossary_entries
  - translate
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
<tr><td><b>Name</b></td><td><code>glossary_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.glossary_entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the entry. Format: "projects/*/locations/*/glossaries/*/glossaryEntries/*" |
| <CopyableCode code="description" /> | `string` | Describes the glossary entry. |
| <CopyableCode code="termsPair" /> | `object` | Represents a single entry for an unidirectional glossary. |
| <CopyableCode code="termsSet" /> | `object` | Represents a single entry for an equivalent term set glossary. This is used for equivalent term sets where each term can be replaced by the other terms in the set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_glossaries_glossary_entries_get" /> | `SELECT` | <CopyableCode code="glossariesId, glossaryEntriesId, locationsId, projectsId" /> | Gets a single glossary entry by the given id. |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_list" /> | `SELECT` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | List the entries for the glossary. |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_create" /> | `INSERT` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | Creates a glossary entry. |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_delete" /> | `DELETE` | <CopyableCode code="glossariesId, glossaryEntriesId, locationsId, projectsId" /> | Deletes a single entry from the glossary |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_patch" /> | `UPDATE` | <CopyableCode code="glossariesId, glossaryEntriesId, locationsId, projectsId" /> | Updates a glossary entry. |
| <CopyableCode code="_projects_locations_glossaries_glossary_entries_list" /> | `EXEC` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | List the entries for the glossary. |
