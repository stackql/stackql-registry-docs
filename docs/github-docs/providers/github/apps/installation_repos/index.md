---
title: installation_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - installation_repos
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>installation_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.apps.installation_repos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="repositories" /> | `array` |
| <CopyableCode code="repository_selection" /> | `string` |
| <CopyableCode code="total_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_installation_repos_for_authenticated_user" /> | `SELECT` | <CopyableCode code="installation_id" /> | List repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access for an installation.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.<br /><br />You must use a [user access token](https://docs.github.com/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app), created for a user who has authorized your GitHub App, to access this endpoint.<br /><br />The access the user has to each repository is included in the hash under the `permissions` key. |
| <CopyableCode code="list_repos_accessible_to_installation" /> | `SELECT` |  | List repositories that an app installation can access.<br /><br />You must use an [installation access token](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint. |
| <CopyableCode code="remove_repo_from_installation_for_authenticated_user" /> | `DELETE` | <CopyableCode code="installation_id, repository_id" /> | Remove a single repository from an installation. The authenticated user must have admin access to the repository. The installation must have the `repository_selection` of `selected`.<br /><br />You must use a personal access token (which you can create via the [command line](https://docs.github.com/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint. |
| <CopyableCode code="add_repo_to_installation_for_authenticated_user" /> | `EXEC` | <CopyableCode code="installation_id, repository_id" /> | Add a single repository to an installation. The authenticated user must have admin access to the repository.<br /><br />You must use a personal access token (which you can create via the [command line](https://docs.github.com/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint. |
