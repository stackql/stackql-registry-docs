---
title: workspaces__git_ahead_behind
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces__git_ahead_behind
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
<tr><td><b>Name</b></td><td><code>workspaces__git_ahead_behind</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.workspaces__git_ahead_behind</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `commitsAhead` | `integer` | The number of commits in the remote branch that are not in the workspace. |
| `commitsBehind` | `integer` | The number of commits in the workspace that are not in the remote branch. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_repositories_workspaces_fetchGitAheadBehind` | `SELECT` | `locationsId, projectsId, repositoriesId, workspacesId` |
