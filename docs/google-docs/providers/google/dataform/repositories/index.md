---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - dataform
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
<tr><td><b>Id</b></td><td><code>google.dataform.repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `repositories` | `array` | List of repositories. |
| `unreachable` | `array` | Locations which could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId` | Fetches a single Repository. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Repositories in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Repository in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId` | Deletes a single Repository. |
| `commit` | `EXEC` | `locationsId, projectsId, repositoriesId` | Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`. |
| `compute_access_token_status` | `EXEC` | `locationsId, projectsId, repositoriesId` | Computes a Repository's Git access token status. |
| `patch` | `EXEC` | `locationsId, projectsId, repositoriesId` | Updates a single Repository. |
| `query_directory_contents` | `EXEC` | `locationsId, projectsId, repositoriesId` | Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`. |
| `read_file` | `EXEC` | `locationsId, projectsId, repositoriesId` | Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`. |
