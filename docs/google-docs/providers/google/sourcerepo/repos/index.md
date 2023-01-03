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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash` |
| `size` | `string` | The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo. |
| `url` | `string` | URL to clone the repository from Google Cloud Source Repositories. Read-only field. |
| `mirrorConfig` | `object` | Configuration to automatically mirror a repository from another hosting service, for example GitHub or Bitbucket. |
| `pubsubConfigs` | `object` | How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_repos_get` | `SELECT` | `projectsId, reposId` | Returns information about a repo. |
| `projects_repos_list` | `SELECT` | `projectsId` | Returns all repos belonging to a project. The sizes of the repos are not set by ListRepos. To get the size of a repo, use GetRepo. |
| `projects_repos_create` | `INSERT` | `projectsId` | Creates a repo in the given project with the given name. If the named repository already exists, `CreateRepo` returns `ALREADY_EXISTS`. |
| `projects_repos_delete` | `DELETE` | `projectsId, reposId` | Deletes a repo. |
| `projects_repos_patch` | `EXEC` | `projectsId, reposId` | Updates information about a repo. |
| `projects_repos_sync` | `EXEC` | `projectsId, reposId` | Synchronize a connected repo. The response contains SyncRepoMetadata in the metadata field. |
