---
title: repos_for_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_for_secrets
  - codespaces
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
<tr><td><b>Name</b></td><td><code>repos_for_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.repos_for_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `homepage` | `string` |  |
| `commits_url` | `string` |  |
| `size` | `integer` |  |
| `forks` | `integer` |  |
| `git_refs_url` | `string` |  |
| `hooks_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `mirror_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `fork` | `boolean` |  |
| `forks_url` | `string` |  |
| `topics` | `array` |  |
| `stargazers_count` | `integer` |  |
| `contents_url` | `string` |  |
| `notifications_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `contributors_url` | `string` |  |
| `blobs_url` | `string` |  |
| `watchers` | `integer` |  |
| `forks_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `language` | `string` |  |
| `milestones_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `archive_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `compare_url` | `string` |  |
| `teams_url` | `string` |  |
| `visibility` | `string` |  |
| `tags_url` | `string` |  |
| `permissions` | `object` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `url` | `string` |  |
| `merges_url` | `string` |  |
| `disabled` | `boolean` |  |
| `events_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `node_id` | `string` |  |
| `deployments_url` | `string` |  |
| `full_name` | `string` |  |
| `stargazers_url` | `string` |  |
| `git_url` | `string` |  |
| `owner` | `object` | Simple User |
| `open_issues` | `integer` |  |
| `pushed_at` | `string` |  |
| `svn_url` | `string` |  |
| `trees_url` | `string` |  |
| `labels_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `ssh_url` | `string` |  |
| `comments_url` | `string` |  |
| `assignees_url` | `string` |  |
| `license` | `object` |  |
| `downloads_url` | `string` |  |
| `default_branch` | `string` |  |
| `has_downloads` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `languages_url` | `string` |  |
| `updated_at` | `string` |  |
| `branches_url` | `string` |  |
| `keys_url` | `string` |  |
| `network_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `issues_url` | `string` |  |
| `private` | `boolean` |  |
| `archived` | `boolean` |  |
| `statuses_url` | `string` |  |
| `created_at` | `string` |  |
| `pulls_url` | `string` |  |
| `html_url` | `string` |  |
| `releases_url` | `string` |  |
| `clone_url` | `string` |  |
| `subscription_url` | `string` |  |
| `role_name` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repositories_for_secret_for_authenticated_user` | `SELECT` | `secret_name` | List the repositories that have been granted the ability to use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `add_repository_for_secret_for_authenticated_user` | `INSERT` | `repository_id, secret_name` | Adds a repository to the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `remove_repository_for_secret_for_authenticated_user` | `DELETE` | `repository_id, secret_name` | Removes a repository from the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `set_repositories_for_secret_for_authenticated_user` | `EXEC` | `secret_name, data__selected_repository_ids` | Select the repositories that will use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
