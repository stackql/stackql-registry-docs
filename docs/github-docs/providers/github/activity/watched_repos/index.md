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
| `branches_url` | `string` |  |
| `svn_url` | `string` |  |
| `compare_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `downloads_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `homepage` | `string` |  |
| `deployments_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `language` | `string` |  |
| `template_repository` | `object` | A git repository |
| `has_pages` | `boolean` |  |
| `contributors_url` | `string` |  |
| `subscription_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `commits_url` | `string` |  |
| `size` | `integer` |  |
| `releases_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `owner` | `object` | Simple User |
| `teams_url` | `string` |  |
| `is_template` | `boolean` |  |
| `updated_at` | `string` |  |
| `watchers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `network_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `tags_url` | `string` |  |
| `permissions` | `object` |  |
| `archive_url` | `string` |  |
| `fork` | `boolean` |  |
| `visibility` | `string` |  |
| `assignees_url` | `string` |  |
| `comments_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `archived` | `boolean` |  |
| `notifications_url` | `string` |  |
| `forks_url` | `string` |  |
| `url` | `string` |  |
| `ssh_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `watchers` | `integer` |  |
| `languages_url` | `string` |  |
| `topics` | `array` |  |
| `node_id` | `string` |  |
| `labels_url` | `string` |  |
| `html_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `forks` | `integer` |  |
| `trees_url` | `string` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `contents_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `default_branch` | `string` |  |
| `pulls_url` | `string` |  |
| `keys_url` | `string` |  |
| `private` | `boolean` |  |
| `merges_url` | `string` |  |
| `clone_url` | `string` |  |
| `created_at` | `string` |  |
| `has_projects` | `boolean` |  |
| `full_name` | `string` |  |
| `git_refs_url` | `string` |  |
| `pushed_at` | `string` |  |
| `statuses_url` | `string` |  |
| `mirror_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `open_issues` | `integer` |  |
| `git_url` | `string` |  |
| `issues_url` | `string` |  |
| `hooks_url` | `string` |  |
| `blobs_url` | `string` |  |
| `license` | `object` |  |
| `role_name` | `string` |  |
| `disabled` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
