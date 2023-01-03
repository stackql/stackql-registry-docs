---
title: installations_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>installations_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.installations_repos</code></td></tr>
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
| `list_installation_repos_for_authenticated_user` | `SELECT` | `installation_id` | List repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access for an installation.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.<br /><br />You must use a [user-to-server OAuth access token](https://docs.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.<br /><br />The access the user has to each repository is included in the hash under the `permissions` key. |
| `list_repos_accessible_to_installation` | `SELECT` |  | List repositories that an app installation can access.<br /><br />You must use an [installation access token](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint. |
| `add_repo_to_installation_for_authenticated_user` | `INSERT` | `installation_id, repository_id` | Add a single repository to an installation. The authenticated user must have admin access to the repository.<br /><br />You must use a personal access token (which you can create via the [command line](https://docs.github.com/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint. |
| `remove_repo_from_installation_for_authenticated_user` | `DELETE` | `installation_id, repository_id` | Remove a single repository from an installation. The authenticated user must have admin access to the repository.<br /><br />You must use a personal access token (which you can create via the [command line](https://docs.github.com/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint. |
| `revoke_installation_access_token` | `EXEC` |  | Revokes the installation token you're using to authenticate as an installation and access this endpoint.<br /><br />Once an installation token is revoked, the token is invalidated and cannot be used. Other endpoints that require the revoked installation token must have a new installation token to work. You can create a new token using the "[Create an installation access token for an app](https://docs.github.com/rest/reference/apps#create-an-installation-access-token-for-an-app)" endpoint.<br /><br />You must use an [installation access token](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint. |
