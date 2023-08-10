---
title: synonym_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - synonym_sets
  - contentwarehouse
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
<tr><td><b>Name</b></td><td><code>synonym_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.synonym_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/synonymSets/&#123;context&#125;. |
| `context` | `string` | This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests. |
| `synonyms` | `array` | List of Synonyms for the context. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, synonymSetsId` | Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist |
| `list` | `SELECT` | `locationsId, projectsId` | Returns all SynonymSets (for all contexts) for the specified location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context. |
| `delete` | `DELETE` | `locationsId, projectsId, synonymSetsId` | Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found. |
| `_list` | `EXEC` | `locationsId, projectsId` | Returns all SynonymSets (for all contexts) for the specified location. |
| `patch` | `EXEC` | `locationsId, projectsId, synonymSetsId` | Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found. |
