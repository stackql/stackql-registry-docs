---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
  - migrations
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `homepage` | `string` |  |
| `has_issues` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `teams_url` | `string` |  |
| `commits_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `private` | `boolean` |  |
| `archived` | `boolean` |  |
| `issues_url` | `string` |  |
| `assignees_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `size` | `integer` |  |
| `notifications_url` | `string` |  |
| `releases_url` | `string` |  |
| `pulls_url` | `string` |  |
| `svn_url` | `string` |  |
| `subscription_url` | `string` |  |
| `watchers` | `integer` |  |
| `created_at` | `string` |  |
| `has_pages` | `boolean` |  |
| `license` | `object` |  |
| `statuses_url` | `string` |  |
| `forks_count` | `integer` |  |
| `contents_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `default_branch` | `string` |  |
| `permissions` | `object` |  |
| `issue_events_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `forks_url` | `string` |  |
| `keys_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `disabled` | `boolean` |  |
| `updated_at` | `string` |  |
| `subscribers_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `visibility` | `string` |  |
| `issue_comment_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `compare_url` | `string` |  |
| `hooks_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `full_name` | `string` |  |
| `deployments_url` | `string` |  |
| `clone_url` | `string` |  |
| `git_url` | `string` |  |
| `node_id` | `string` |  |
| `milestones_url` | `string` |  |
| `branches_url` | `string` |  |
| `language` | `string` |  |
| `is_template` | `boolean` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `tags_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `blobs_url` | `string` |  |
| `labels_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `mirror_url` | `string` |  |
| `fork` | `boolean` |  |
| `forks` | `integer` |  |
| `topics` | `array` |  |
| `role_name` | `string` |  |
| `git_commits_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `languages_url` | `string` |  |
| `html_url` | `string` |  |
| `comments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `events_url` | `string` |  |
| `archive_url` | `string` |  |
| `owner` | `object` | Simple User |
| `merges_url` | `string` |  |
| `trees_url` | `string` |  |
| `network_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `stargazers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
