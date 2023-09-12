---
title: branches_protection_restrictions_users
hide_title: false
hide_table_of_contents: false
keywords:
  - branches_protection_restrictions_users
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branches_protection_restrictions_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.branches_protection_restrictions_users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `events_url` | `string` |
| `subscriptions_url` | `string` |
| `avatar_url` | `string` |
| `gravatar_id` | `string` |
| `email` | `string` |
| `starred_url` | `string` |
| `login` | `string` |
| `site_admin` | `boolean` |
| `starred_at` | `string` |
| `organizations_url` | `string` |
| `followers_url` | `string` |
| `url` | `string` |
| `following_url` | `string` |
| `gists_url` | `string` |
| `type` | `string` |
| `repos_url` | `string` |
| `node_id` | `string` |
| `received_events_url` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_users_with_access_to_protected_branch` | `SELECT` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists the people who have push access to this branch. |
| `add_user_access_restrictions` | `INSERT` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Grants the specified people push access for this branch.<br /><br />\| Type    \| Description                                                                                                                   \|<br />\| ------- \| ----------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| |
| `remove_user_access_restrictions` | `DELETE` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Removes the ability of a user to push to this branch.<br /><br />\| Type    \| Description                                                                                                                                   \|<br />\| ------- \| --------------------------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| |
| `set_user_access_restrictions` | `EXEC` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Replaces the list of people that have push access to this branch. This removes all people that previously had push access and grants push access to the new list of people.<br /><br />\| Type    \| Description                                                                                                                   \|<br />\| ------- \| ----------------------------------------------------------------------------------------------------------------------------- \|<br />\| `array` \| Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. \| |
