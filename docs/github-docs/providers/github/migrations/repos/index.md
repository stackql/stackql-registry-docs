---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `merges_url` | `string` |  |
| `pulls_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `has_pages` | `boolean` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `archived` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `ssh_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `mirror_url` | `string` |  |
| `svn_url` | `string` |  |
| `visibility` | `string` |  |
| `is_template` | `boolean` |  |
| `homepage` | `string` |  |
| `has_downloads` | `boolean` |  |
| `notifications_url` | `string` |  |
| `full_name` | `string` |  |
| `fork` | `boolean` |  |
| `pushed_at` | `string` |  |
| `has_projects` | `boolean` |  |
| `watchers` | `integer` |  |
| `disabled` | `boolean` |  |
| `forks` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `deployments_url` | `string` |  |
| `blobs_url` | `string` |  |
| `language` | `string` |  |
| `compare_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `assignees_url` | `string` |  |
| `private` | `boolean` |  |
| `branches_url` | `string` |  |
| `topics` | `array` |  |
| `keys_url` | `string` |  |
| `hooks_url` | `string` |  |
| `forks_count` | `integer` |  |
| `labels_url` | `string` |  |
| `forks_url` | `string` |  |
| `downloads_url` | `string` |  |
| `contents_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `archive_url` | `string` |  |
| `clone_url` | `string` |  |
| `contributors_url` | `string` |  |
| `updated_at` | `string` |  |
| `stargazers_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `role_name` | `string` |  |
| `permissions` | `object` |  |
| `git_refs_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `milestones_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `trees_url` | `string` |  |
| `size` | `integer` |  |
| `releases_url` | `string` |  |
| `license` | `object` |  |
| `network_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `events_url` | `string` |  |
| `languages_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `owner` | `object` | Simple User |
| `issues_url` | `string` |  |
| `url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `subscription_url` | `string` |  |
| `commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `default_branch` | `string` |  |
| `node_id` | `string` |  |
| `teams_url` | `string` |  |
| `open_issues` | `integer` |  |
| `tags_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` | Lists all the repositories for this user migration. |
| `list_repos_for_org` | `SELECT` | `migration_id, org` | List all the repositories for this organization migration. |
| `unlock_repo_for_authenticated_user` | `EXEC` | `migration_id, repo_name` | Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/reference/migrations#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/reference/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked. |
| `unlock_repo_for_org` | `EXEC` | `migration_id, org, repo_name` | Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/reference/repos#delete-a-repository) when the migration is complete and you no longer need the source data. |
