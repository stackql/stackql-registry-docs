---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
  - sourcerepo
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sourcerepo.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `repos` | `array` | The listed repos. |
| `nextPageToken` | `string` | If non-empty, additional repositories exist within the project. These can be retrieved by including this value in the next ListReposRequest's page_token field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, reposId` | Returns information about a repo. |
| `list` | `SELECT` | `projectsId` | Returns all repos belonging to a project. The sizes of the repos are not set by ListRepos. To get the size of a repo, use GetRepo. |
| `create` | `INSERT` | `projectsId` | Creates a repo in the given project with the given name. If the named repository already exists, `CreateRepo` returns `ALREADY_EXISTS`. |
| `delete` | `DELETE` | `projectsId, reposId` | Deletes a repo. |
| `patch` | `EXEC` | `projectsId, reposId` | Updates information about a repo. |
| `sync` | `EXEC` | `projectsId, reposId` | Synchronize a connected repo. The response contains SyncRepoMetadata in the metadata field. |
