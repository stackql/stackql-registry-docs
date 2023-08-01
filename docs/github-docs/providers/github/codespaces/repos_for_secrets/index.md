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
| `releases_url` | `string` |  |
| `issues_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `pushed_at` | `string` |  |
| `node_id` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `downloads_url` | `string` |  |
| `owner` | `object` | Simple User |
| `allow_forking` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `contents_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `network_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `updated_at` | `string` |  |
| `svn_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `events_url` | `string` |  |
| `git_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `archived` | `boolean` |  |
| `subscription_url` | `string` |  |
| `compare_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `size` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `keys_url` | `string` |  |
| `pulls_url` | `string` |  |
| `watchers` | `integer` |  |
| `license` | `object` |  |
| `statuses_url` | `string` |  |
| `merges_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `notifications_url` | `string` |  |
| `role_name` | `string` |  |
| `created_at` | `string` |  |
| `git_commits_url` | `string` |  |
| `trees_url` | `string` |  |
| `language` | `string` |  |
| `full_name` | `string` |  |
| `clone_url` | `string` |  |
| `milestones_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `assignees_url` | `string` |  |
| `contributors_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `archive_url` | `string` |  |
| `deployments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `collaborators_url` | `string` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `homepage` | `string` |  |
| `forks_count` | `integer` |  |
| `tags_url` | `string` |  |
| `languages_url` | `string` |  |
| `forks` | `integer` |  |
| `teams_url` | `string` |  |
| `permissions` | `object` |  |
| `private` | `boolean` |  |
| `is_template` | `boolean` |  |
| `blobs_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `commits_url` | `string` |  |
| `labels_url` | `string` |  |
| `disabled` | `boolean` |  |
| `branches_url` | `string` |  |
| `visibility` | `string` |  |
| `topics` | `array` |  |
| `default_branch` | `string` |  |
| `forks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `mirror_url` | `string` |  |
| `fork` | `boolean` |  |
| `html_url` | `string` |  |
| `ssh_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repositories_for_secret_for_authenticated_user` | `SELECT` | `secret_name` | List the repositories that have been granted the ability to use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `add_repository_for_secret_for_authenticated_user` | `INSERT` | `repository_id, secret_name` | Adds a repository to the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `remove_repository_for_secret_for_authenticated_user` | `DELETE` | `repository_id, secret_name` | Removes a repository from the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `set_repositories_for_secret_for_authenticated_user` | `EXEC` | `secret_name, data__selected_repository_ids` | Select the repositories that will use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
