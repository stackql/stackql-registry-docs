---
title: team_access_restrictions
hide_title: false
hide_table_of_contents: false
keywords:
  - team_access_restrictions
  - repos
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
<tr><td><b>Name</b></td><td><code>team_access_restrictions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.team_access_restrictions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="members_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notification_setting" /> | `string` |  |
| <CopyableCode code="parent" /> | `object` | Groups of organization members that gives permissions on specified repositories. |
| <CopyableCode code="permission" /> | `string` |  |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="privacy" /> | `string` |  |
| <CopyableCode code="repositories_url" /> | `string` |  |
| <CopyableCode code="slug" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_teams_with_access_to_protected_branch" /> | `SELECT` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists the teams who have push access to this branch. The list includes child teams. |
| <CopyableCode code="add_team_access_restrictions" /> | `INSERT` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Grants the specified teams push access for this branch. You can also give push access to child teams. |
| <CopyableCode code="remove_team_access_restrictions" /> | `DELETE` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Removes the ability of a team to push to this branch. You can also remove push access for child teams. |
| <CopyableCode code="set_team_access_restrictions" /> | `EXEC` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Replaces the list of teams that have push access to this branch. This removes all teams that previously had push access and grants push access to the new list of teams. Team restrictions include child teams. |
