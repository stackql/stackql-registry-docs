---
title: watched_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - watched_repos
  - activity
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
<tr><td><b>Name</b></td><td><code>watched_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.watched_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `temp_clone_token` | `string` |  |
| `has_projects` | `boolean` |  |
| `languages_url` | `string` |  |
| `merges_url` | `string` |  |
| `mirror_url` | `string` |  |
| `forks` | `integer` |  |
| `commits_url` | `string` |  |
| `network_count` | `integer` |  |
| `keys_url` | `string` |  |
| `size` | `integer` |  |
| `git_commits_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `subscription_url` | `string` |  |
| `topics` | `array` |  |
| `compare_url` | `string` |  |
| `blobs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `contents_url` | `string` |  |
| `is_template` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `events_url` | `string` |  |
| `pushed_at` | `string` |  |
| `labels_url` | `string` |  |
| `trees_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `releases_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `assignees_url` | `string` |  |
| `forks_url` | `string` |  |
| `milestones_url` | `string` |  |
| `git_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `default_branch` | `string` |  |
| `archive_url` | `string` |  |
| `branches_url` | `string` |  |
| `watchers` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `disabled` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `fork` | `boolean` |  |
| `contributors_url` | `string` |  |
| `clone_url` | `string` |  |
| `language` | `string` |  |
| `has_pages` | `boolean` |  |
| `role_name` | `string` |  |
| `tags_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `url` | `string` |  |
| `downloads_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `svn_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `ssh_url` | `string` |  |
| `forks_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `full_name` | `string` |  |
| `license` | `object` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `visibility` | `string` |  |
| `deployments_url` | `string` |  |
| `comments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `html_url` | `string` |  |
| `notifications_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `permissions` | `object` |  |
| `private` | `boolean` |  |
| `homepage` | `string` |  |
| `node_id` | `string` |  |
| `teams_url` | `string` |  |
| `owner` | `object` | Simple User |
| `git_refs_url` | `string` |  |
| `open_issues` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
