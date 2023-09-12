---
title: user_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - user_repositories
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
<tr><td><b>Name</b></td><td><code>user_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.user_repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `stargazers_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `git_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `labels_url` | `string` |  |
| `issues_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `html_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `notifications_url` | `string` |  |
| `disabled` | `boolean` |  |
| `teams_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `created_at` | `string` |  |
| `events_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `archived` | `boolean` |  |
| `subscription_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `releases_url` | `string` |  |
| `watchers` | `integer` |  |
| `archive_url` | `string` |  |
| `deployments_url` | `string` |  |
| `assignees_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `commits_url` | `string` |  |
| `full_name` | `string` |  |
| `is_template` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `forks_count` | `integer` |  |
| `node_id` | `string` |  |
| `private` | `boolean` |  |
| `languages_url` | `string` |  |
| `homepage` | `string` |  |
| `has_pages` | `boolean` |  |
| `default_branch` | `string` |  |
| `statuses_url` | `string` |  |
| `language` | `string` |  |
| `compare_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `forks` | `integer` |  |
| `permissions` | `object` |  |
| `role_name` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `keys_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `branches_url` | `string` |  |
| `open_issues` | `integer` |  |
| `trees_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `git_commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `topics` | `array` |  |
| `network_count` | `integer` |  |
| `fork` | `boolean` |  |
| `merges_url` | `string` |  |
| `clone_url` | `string` |  |
| `url` | `string` |  |
| `ssh_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `license` | `object` |  |
| `tags_url` | `string` |  |
| `forks_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `blobs_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `visibility` | `string` |  |
| `contents_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `contributors_url` | `string` |  |
| `downloads_url` | `string` |  |
| `pulls_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `hooks_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `updated_at` | `string` |  |
| `milestones_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `comments_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_repos_for_authenticated_user` | `SELECT` | `migration_id` |
