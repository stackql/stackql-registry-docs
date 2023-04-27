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
| `has_downloads` | `boolean` |  |
| `mirror_url` | `string` |  |
| `pulls_url` | `string` |  |
| `commits_url` | `string` |  |
| `network_count` | `integer` |  |
| `git_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `trees_url` | `string` |  |
| `deployments_url` | `string` |  |
| `permissions` | `object` |  |
| `archive_url` | `string` |  |
| `teams_url` | `string` |  |
| `ssh_url` | `string` |  |
| `language` | `string` |  |
| `subscribers_url` | `string` |  |
| `license` | `object` |  |
| `archived` | `boolean` |  |
| `forks` | `integer` |  |
| `git_tags_url` | `string` |  |
| `open_issues` | `integer` |  |
| `role_name` | `string` |  |
| `homepage` | `string` |  |
| `collaborators_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `html_url` | `string` |  |
| `clone_url` | `string` |  |
| `releases_url` | `string` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `events_url` | `string` |  |
| `compare_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `languages_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `full_name` | `string` |  |
| `owner` | `object` | Simple User |
| `stargazers_url` | `string` |  |
| `topics` | `array` |  |
| `branches_url` | `string` |  |
| `visibility` | `string` |  |
| `contents_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `hooks_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `comments_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `disabled` | `boolean` |  |
| `created_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `issues_url` | `string` |  |
| `blobs_url` | `string` |  |
| `private` | `boolean` |  |
| `assignees_url` | `string` |  |
| `url` | `string` |  |
| `pushed_at` | `string` |  |
| `default_branch` | `string` |  |
| `labels_url` | `string` |  |
| `statuses_url` | `string` |  |
| `tags_url` | `string` |  |
| `size` | `integer` |  |
| `contributors_url` | `string` |  |
| `updated_at` | `string` |  |
| `svn_url` | `string` |  |
| `forks_count` | `integer` |  |
| `watchers` | `integer` |  |
| `has_projects` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `downloads_url` | `string` |  |
| `subscription_url` | `string` |  |
| `milestones_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `merges_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `keys_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repositories_for_secret_for_authenticated_user` | `SELECT` | `secret_name` | List the repositories that have been granted the ability to use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `add_repository_for_secret_for_authenticated_user` | `INSERT` | `repository_id, secret_name` | Adds a repository to the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `remove_repository_for_secret_for_authenticated_user` | `DELETE` | `repository_id, secret_name` | Removes a repository from the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `set_repositories_for_secret_for_authenticated_user` | `EXEC` | `secret_name, data__selected_repository_ids` | Select the repositories that will use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
