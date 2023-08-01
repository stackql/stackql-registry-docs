---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
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
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to retrieve the next page of repositories, or empty if there are no more repositories to return. |
| `repositories` | `array` | The repositories returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId` | Gets a repository. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists repositories. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId` | Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response. |
| `patch` | `EXEC` | `locationsId, projectsId, repositoriesId` | Updates a repository. |
