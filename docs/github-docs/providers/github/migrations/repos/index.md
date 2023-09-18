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
| `url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `language` | `string` |  |
| `has_issues` | `boolean` |  |
| `deployments_url` | `string` |  |
| `releases_url` | `string` |  |
| `license` | `object` |  |
| `forks` | `integer` |  |
| `is_template` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `statuses_url` | `string` |  |
| `issues_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `pulls_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `contents_url` | `string` |  |
| `downloads_url` | `string` |  |
| `forks_count` | `integer` |  |
| `full_name` | `string` |  |
| `keys_url` | `string` |  |
| `fork` | `boolean` |  |
| `svn_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `clone_url` | `string` |  |
| `tags_url` | `string` |  |
| `assignees_url` | `string` |  |
| `teams_url` | `string` |  |
| `private` | `boolean` |  |
| `archived` | `boolean` |  |
| `updated_at` | `string` |  |
| `has_wiki` | `boolean` |  |
| `blobs_url` | `string` |  |
| `milestones_url` | `string` |  |
| `merges_url` | `string` |  |
| `disabled` | `boolean` |  |
| `notifications_url` | `string` |  |
| `node_id` | `string` |  |
| `allow_forking` | `boolean` |  |
| `events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `visibility` | `string` |  |
| `comments_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `default_branch` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `watchers` | `integer` |  |
| `homepage` | `string` |  |
| `issue_events_url` | `string` |  |
| `ssh_url` | `string` |  |
| `trees_url` | `string` |  |
| `permissions` | `object` |  |
| `open_issues` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `branches_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `created_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `commits_url` | `string` |  |
| `contributors_url` | `string` |  |
| `languages_url` | `string` |  |
| `archive_url` | `string` |  |
| `labels_url` | `string` |  |
| `forks_url` | `string` |  |
| `compare_url` | `string` |  |
| `role_name` | `string` |  |
| `git_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `mirror_url` | `string` |  |
| `pushed_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `topics` | `array` |  |
| `network_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `git_commits_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/migrations/users#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/repos/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/repos/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
