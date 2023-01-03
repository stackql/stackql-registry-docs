---
title: glossaries
hide_title: false
hide_table_of_contents: false
keywords:
  - glossaries
  - translate
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>glossaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.glossaries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the glossary. Glossary names have the form `projects/{project-number-or-id}/locations/{location-id}/glossaries/{glossary-id}`. |
| `languageCodesSet` | `object` | Used with equivalent term set glossaries. |
| `languagePair` | `object` | Used with unidirectional glossaries. |
| `submitTime` | `string` | Output only. When CreateGlossary was called. |
| `endTime` | `string` | Output only. When the glossary creation was finished. |
| `entryCount` | `integer` | Output only. The number of entries defined in the glossary. |
| `inputConfig` | `object` | Input configuration for glossaries. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_glossaries_get` | `SELECT` | `glossariesId, locationsId, projectsId` | Gets a glossary. Returns NOT_FOUND, if the glossary doesn't exist. |
| `projects_locations_glossaries_list` | `SELECT` | `locationsId, projectsId` | Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't exist. |
| `projects_locations_glossaries_create` | `INSERT` | `locationsId, projectsId` | Creates a glossary and returns the long-running operation. Returns NOT_FOUND, if the project doesn't exist. |
| `projects_locations_glossaries_delete` | `DELETE` | `glossariesId, locationsId, projectsId` | Deletes a glossary, or cancels glossary construction if the glossary isn't created yet. Returns NOT_FOUND, if the glossary doesn't exist. |
