---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - artifactregistry
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
<tr><td><b>Id</b></td><td><code>google.artifactregistry.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to retrieve the next page of tags, or empty if there are no more tags to return. |
| `tags` | `array` | The tags returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId, tagsId` | Gets a tag. |
| `list` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId` | Lists tags. |
| `create` | `INSERT` | `locationsId, packagesId, projectsId, repositoriesId` | Creates a tag. |
| `delete` | `DELETE` | `locationsId, packagesId, projectsId, repositoriesId, tagsId` | Deletes a tag. |
| `patch` | `EXEC` | `locationsId, packagesId, projectsId, repositoriesId, tagsId` | Updates a tag. |
