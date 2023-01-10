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
| `mirror_url` | `string` |  |
| `forks` | `integer` |  |
| `contributors_url` | `string` |  |
| `svn_url` | `string` |  |
| `private` | `boolean` |  |
| `branches_url` | `string` |  |
| `contents_url` | `string` |  |
| `role_name` | `string` |  |
| `updated_at` | `string` |  |
| `homepage` | `string` |  |
| `pulls_url` | `string` |  |
| `watchers` | `integer` |  |
| `downloads_url` | `string` |  |
| `git_url` | `string` |  |
| `assignees_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `forks_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `pushed_at` | `string` |  |
| `events_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `full_name` | `string` |  |
| `notifications_url` | `string` |  |
| `ssh_url` | `string` |  |
| `archive_url` | `string` |  |
| `deployments_url` | `string` |  |
| `trees_url` | `string` |  |
| `html_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `milestones_url` | `string` |  |
| `permissions` | `object` |  |
| `has_pages` | `boolean` |  |
| `license` | `object` |  |
| `url` | `string` |  |
| `subscription_url` | `string` |  |
| `default_branch` | `string` |  |
| `forks_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `network_count` | `integer` |  |
| `issues_url` | `string` |  |
| `node_id` | `string` |  |
| `subscribers_url` | `string` |  |
| `commits_url` | `string` |  |
| `is_template` | `boolean` |  |
| `releases_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `visibility` | `string` |  |
| `size` | `integer` |  |
| `blobs_url` | `string` |  |
| `labels_url` | `string` |  |
| `disabled` | `boolean` |  |
| `comments_url` | `string` |  |
| `languages_url` | `string` |  |
| `archived` | `boolean` |  |
| `teams_url` | `string` |  |
| `tags_url` | `string` |  |
| `open_issues` | `integer` |  |
| `owner` | `object` | Simple User |
| `topics` | `array` |  |
| `issue_events_url` | `string` |  |
| `hooks_url` | `string` |  |
| `compare_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `statuses_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `open_issues_count` | `integer` |  |
| `keys_url` | `string` |  |
| `created_at` | `string` |  |
| `has_downloads` | `boolean` |  |
| `language` | `string` |  |
| `temp_clone_token` | `string` |  |
| `git_tags_url` | `string` |  |
| `merges_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `clone_url` | `string` |  |
| `fork` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
