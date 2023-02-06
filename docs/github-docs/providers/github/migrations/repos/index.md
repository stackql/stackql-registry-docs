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
| `statuses_url` | `string` |  |
| `labels_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `comments_url` | `string` |  |
| `notifications_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `private` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `milestones_url` | `string` |  |
| `fork` | `boolean` |  |
| `blobs_url` | `string` |  |
| `subscription_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `keys_url` | `string` |  |
| `role_name` | `string` |  |
| `downloads_url` | `string` |  |
| `created_at` | `string` |  |
| `network_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `open_issues` | `integer` |  |
| `hooks_url` | `string` |  |
| `is_template` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `assignees_url` | `string` |  |
| `forks_url` | `string` |  |
| `full_name` | `string` |  |
| `visibility` | `string` |  |
| `stargazers_count` | `integer` |  |
| `teams_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `owner` | `object` | Simple User |
| `branches_url` | `string` |  |
| `languages_url` | `string` |  |
| `html_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `size` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `events_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `updated_at` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `pulls_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `permissions` | `object` |  |
| `has_wiki` | `boolean` |  |
| `disabled` | `boolean` |  |
| `compare_url` | `string` |  |
| `clone_url` | `string` |  |
| `homepage` | `string` |  |
| `node_id` | `string` |  |
| `contributors_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `archive_url` | `string` |  |
| `merges_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `forks_count` | `integer` |  |
| `default_branch` | `string` |  |
| `svn_url` | `string` |  |
| `deployments_url` | `string` |  |
| `watchers` | `integer` |  |
| `pushed_at` | `string` |  |
| `ssh_url` | `string` |  |
| `forks` | `integer` |  |
| `releases_url` | `string` |  |
| `license` | `object` |  |
| `has_projects` | `boolean` |  |
| `commits_url` | `string` |  |
| `language` | `string` |  |
| `url` | `string` |  |
| `git_url` | `string` |  |
| `topics` | `array` |  |
| `trees_url` | `string` |  |
| `contents_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
