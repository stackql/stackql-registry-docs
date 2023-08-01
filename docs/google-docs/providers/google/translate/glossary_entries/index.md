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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>glossary_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.glossary_entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Optional. A token to retrieve a page of results. Pass this value in the [ListGLossaryEntriesRequest.page_token] field in the subsequent calls. |
| `glossaryEntries` | `array` | Optional. The Glossary Entries |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_glossaries_glossary_entries_get` | `SELECT` | `glossariesId, glossaryEntriesId, locationsId, projectsId` | Gets a single glossary entry by the given id. |
| `projects_locations_glossaries_glossary_entries_list` | `SELECT` | `glossariesId, locationsId, projectsId` | List the entries for the glossary. |
| `projects_locations_glossaries_glossary_entries_create` | `INSERT` | `glossariesId, locationsId, projectsId` | Creates a glossary entry. |
| `projects_locations_glossaries_glossary_entries_delete` | `DELETE` | `glossariesId, glossaryEntriesId, locationsId, projectsId` | Deletes a single entry from the glossary |
| `projects_locations_glossaries_glossary_entries_patch` | `EXEC` | `glossariesId, glossaryEntriesId, locationsId, projectsId` | Updates a glossary entry. |
