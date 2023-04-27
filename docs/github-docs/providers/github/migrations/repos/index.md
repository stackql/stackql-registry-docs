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
| `pushed_at` | `string` |  |
| `assignees_url` | `string` |  |
| `events_url` | `string` |  |
| `full_name` | `string` |  |
| `has_downloads` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `open_issues` | `integer` |  |
| `hooks_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `disabled` | `boolean` |  |
| `archived` | `boolean` |  |
| `watchers` | `integer` |  |
| `git_refs_url` | `string` |  |
| `svn_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `git_url` | `string` |  |
| `archive_url` | `string` |  |
| `trees_url` | `string` |  |
| `clone_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `license` | `object` |  |
| `stargazers_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `permissions` | `object` |  |
| `default_branch` | `string` |  |
| `comments_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `is_template` | `boolean` |  |
| `deployments_url` | `string` |  |
| `labels_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `owner` | `object` | Simple User |
| `releases_url` | `string` |  |
| `ssh_url` | `string` |  |
| `keys_url` | `string` |  |
| `notifications_url` | `string` |  |
| `language` | `string` |  |
| `fork` | `boolean` |  |
| `compare_url` | `string` |  |
| `html_url` | `string` |  |
| `network_count` | `integer` |  |
| `languages_url` | `string` |  |
| `forks_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `forks` | `integer` |  |
| `watchers_count` | `integer` |  |
| `node_id` | `string` |  |
| `contents_url` | `string` |  |
| `downloads_url` | `string` |  |
| `created_at` | `string` |  |
| `issues_url` | `string` |  |
| `blobs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `visibility` | `string` |  |
| `pulls_url` | `string` |  |
| `tags_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `commits_url` | `string` |  |
| `mirror_url` | `string` |  |
| `branches_url` | `string` |  |
| `teams_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `contributors_url` | `string` |  |
| `subscription_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `private` | `boolean` |  |
| `size` | `integer` |  |
| `homepage` | `string` |  |
| `topics` | `array` |  |
| `has_issues` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `merges_url` | `string` |  |
| `role_name` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
