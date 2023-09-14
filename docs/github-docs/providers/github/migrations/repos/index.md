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
| `issue_events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `git_tags_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `labels_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `archived` | `boolean` |  |
| `svn_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_issues` | `boolean` |  |
| `homepage` | `string` |  |
| `languages_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `releases_url` | `string` |  |
| `milestones_url` | `string` |  |
| `events_url` | `string` |  |
| `default_branch` | `string` |  |
| `watchers_count` | `integer` |  |
| `role_name` | `string` |  |
| `teams_url` | `string` |  |
| `notifications_url` | `string` |  |
| `clone_url` | `string` |  |
| `open_issues` | `integer` |  |
| `topics` | `array` |  |
| `forks_count` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `subscription_url` | `string` |  |
| `keys_url` | `string` |  |
| `ssh_url` | `string` |  |
| `private` | `boolean` |  |
| `statuses_url` | `string` |  |
| `issues_url` | `string` |  |
| `full_name` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `has_wiki` | `boolean` |  |
| `updated_at` | `string` |  |
| `language` | `string` |  |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `contributors_url` | `string` |  |
| `network_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `assignees_url` | `string` |  |
| `watchers` | `integer` |  |
| `downloads_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `is_template` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `visibility` | `string` |  |
| `permissions` | `object` |  |
| `collaborators_url` | `string` |  |
| `deployments_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `archive_url` | `string` |  |
| `disabled` | `boolean` |  |
| `forks` | `integer` |  |
| `commits_url` | `string` |  |
| `pulls_url` | `string` |  |
| `node_id` | `string` |  |
| `blobs_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `security_and_analysis` | `object` |  |
| `subscribers_count` | `integer` |  |
| `contents_url` | `string` |  |
| `license` | `object` |  |
| `merges_url` | `string` |  |
| `branches_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_projects` | `boolean` |  |
| `html_url` | `string` |  |
| `trees_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `comments_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `mirror_url` | `string` |  |
| `fork` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `created_at` | `string` |  |
| `compare_url` | `string` |  |
| `tags_url` | `string` |  |
| `git_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/migrations/users#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/repos/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/repos/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
