---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.workspaces</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_workspaces_get` | `SELECT` | `locationsId, projectsId, repositoriesId, workspacesId` | Fetches a single Workspace. |
| `projects_locations_repositories_workspaces_list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists Workspaces in a given Repository. |
| `projects_locations_repositories_workspaces_create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new Workspace in a given Repository. |
| `projects_locations_repositories_workspaces_delete` | `DELETE` | `locationsId, projectsId, repositoriesId, workspacesId` | Deletes a single Workspace. |
| `projects_locations_repositories_workspaces_commit` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Applies a Git commit for uncommitted files in a Workspace. |
| `projects_locations_repositories_workspaces_installNpmPackages` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Installs dependency NPM packages (inside a Workspace). |
| `projects_locations_repositories_workspaces_makeDirectory` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Creates a directory inside a Workspace. |
| `projects_locations_repositories_workspaces_moveDirectory` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Moves a directory (inside a Workspace), and all of its contents, to a new location. |
| `projects_locations_repositories_workspaces_moveFile` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Moves a file (inside a Workspace) to a new location. |
| `projects_locations_repositories_workspaces_pull` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Pulls Git commits from the Repository's remote into a Workspace. |
| `projects_locations_repositories_workspaces_push` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Pushes Git commits from a Workspace to the Repository's remote. |
| `projects_locations_repositories_workspaces_queryDirectoryContents` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Returns the contents of a given Workspace directory. |
| `projects_locations_repositories_workspaces_readFile` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Returns the contents of a file (inside a Workspace). |
| `projects_locations_repositories_workspaces_reset` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Performs a Git reset for uncommitted files in a Workspace. |
| `projects_locations_repositories_workspaces_writeFile` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Writes to a file (inside a Workspace). |
