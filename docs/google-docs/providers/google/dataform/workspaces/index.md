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
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId, workspacesId` | Fetches a single Workspace. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists Workspaces in a given Repository. |
| `create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new Workspace in a given Repository. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId, workspacesId` | Deletes a single Workspace. |
| `_list` | `EXEC` | `locationsId, projectsId, repositoriesId` | Lists Workspaces in a given Repository. |
| `commit` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Applies a Git commit for uncommitted files in a Workspace. |
| `install_npm_packages` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Installs dependency NPM packages (inside a Workspace). |
| `make_directory` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Creates a directory inside a Workspace. |
| `move_directory` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Moves a directory (inside a Workspace), and all of its contents, to a new location. |
| `move_file` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Moves a file (inside a Workspace) to a new location. |
| `pull` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Pulls Git commits from the Repository's remote into a Workspace. |
| `push` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Pushes Git commits from a Workspace to the Repository's remote. |
| `query_directory_contents` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Returns the contents of a given Workspace directory. |
| `read_file` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Returns the contents of a file (inside a Workspace). |
| `reset` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Performs a Git reset for uncommitted files in a Workspace. |
| `write_file` | `EXEC` | `locationsId, projectsId, repositoriesId, workspacesId` | Writes to a file (inside a Workspace). |
