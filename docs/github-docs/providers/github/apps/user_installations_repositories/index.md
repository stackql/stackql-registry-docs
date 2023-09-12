---
title: user_installations_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - user_installations_repositories
  - apps
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_installations_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.user_installations_repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `repository_selection` | `string` |
| `total_count` | `integer` |
| `repositories` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_installation_repos_for_authenticated_user` | `SELECT` | `installation_id` | List repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access for an installation.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.<br /><br />You must use a [user access token](https://docs.github.com/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app), created for a user who has authorized your GitHub App, to access this endpoint.<br /><br />The access the user has to each repository is included in the hash under the `permissions` key. |
| `remove_repo_from_installation_for_authenticated_user` | `DELETE` | `installation_id, repository_id` | Remove a single repository from an installation. The authenticated user must have admin access to the repository. The installation must have the `repository_selection` of `selected`.<br /><br />You must use a personal access token (which you can create via the [command line](https://docs.github.com/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint. |
| `add_repo_to_installation_for_authenticated_user` | `EXEC` | `installation_id, repository_id` | Add a single repository to an installation. The authenticated user must have admin access to the repository.<br /><br />You must use a personal access token (which you can create via the [command line](https://docs.github.com/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint. |
