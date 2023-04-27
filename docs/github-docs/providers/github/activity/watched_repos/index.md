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
| `svn_url` | `string` |  |
| `branches_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `deployments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `is_template` | `boolean` |  |
| `visibility` | `string` |  |
| `keys_url` | `string` |  |
| `git_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `open_issues` | `integer` |  |
| `compare_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `downloads_url` | `string` |  |
| `trees_url` | `string` |  |
| `license` | `object` |  |
| `notifications_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `url` | `string` |  |
| `subscribers_url` | `string` |  |
| `size` | `integer` |  |
| `blobs_url` | `string` |  |
| `teams_url` | `string` |  |
| `forks_count` | `integer` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `languages_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `forks` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `merges_url` | `string` |  |
| `permissions` | `object` |  |
| `contributors_url` | `string` |  |
| `private` | `boolean` |  |
| `issues_url` | `string` |  |
| `releases_url` | `string` |  |
| `html_url` | `string` |  |
| `default_branch` | `string` |  |
| `subscription_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `assignees_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `homepage` | `string` |  |
| `statuses_url` | `string` |  |
| `archived` | `boolean` |  |
| `pulls_url` | `string` |  |
| `topics` | `array` |  |
| `contents_url` | `string` |  |
| `tags_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `labels_url` | `string` |  |
| `clone_url` | `string` |  |
| `mirror_url` | `string` |  |
| `events_url` | `string` |  |
| `network_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `subscribers_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `owner` | `object` | Simple User |
| `ssh_url` | `string` |  |
| `hooks_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `language` | `string` |  |
| `role_name` | `string` |  |
| `milestones_url` | `string` |  |
| `comments_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `fork` | `boolean` |  |
| `watchers` | `integer` |  |
| `created_at` | `string` |  |
| `commits_url` | `string` |  |
| `archive_url` | `string` |  |
| `updated_at` | `string` |  |
| `full_name` | `string` |  |
| `git_refs_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
