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
| `fork` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `html_url` | `string` |  |
| `assignees_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `teams_url` | `string` |  |
| `comments_url` | `string` |  |
| `url` | `string` |  |
| `merges_url` | `string` |  |
| `downloads_url` | `string` |  |
| `language` | `string` |  |
| `forks_count` | `integer` |  |
| `size` | `integer` |  |
| `ssh_url` | `string` |  |
| `permissions` | `object` |  |
| `has_pages` | `boolean` |  |
| `forks` | `integer` |  |
| `created_at` | `string` |  |
| `default_branch` | `string` |  |
| `topics` | `array` |  |
| `tags_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `compare_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `archive_url` | `string` |  |
| `open_issues` | `integer` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `mirror_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `visibility` | `string` |  |
| `branches_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `svn_url` | `string` |  |
| `releases_url` | `string` |  |
| `notifications_url` | `string` |  |
| `statuses_url` | `string` |  |
| `forks_url` | `string` |  |
| `clone_url` | `string` |  |
| `owner` | `object` | Simple User |
| `milestones_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `subscription_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `is_template` | `boolean` |  |
| `license` | `object` |  |
| `private` | `boolean` |  |
| `blobs_url` | `string` |  |
| `full_name` | `string` |  |
| `archived` | `boolean` |  |
| `contributors_url` | `string` |  |
| `languages_url` | `string` |  |
| `commits_url` | `string` |  |
| `labels_url` | `string` |  |
| `watchers` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `deployments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `pulls_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `has_wiki` | `boolean` |  |
| `homepage` | `string` |  |
| `events_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `contents_url` | `string` |  |
| `disabled` | `boolean` |  |
| `keys_url` | `string` |  |
| `git_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `issues_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `network_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
