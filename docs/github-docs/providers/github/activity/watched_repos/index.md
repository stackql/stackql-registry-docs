---
title: watched_repos
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
| `hooks_url` | `string` |  |
| `created_at` | `string` |  |
| `git_url` | `string` |  |
| `contributors_url` | `string` |  |
| `private` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `forks` | `integer` |  |
| `merges_url` | `string` |  |
| `trees_url` | `string` |  |
| `branches_url` | `string` |  |
| `blobs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `assignees_url` | `string` |  |
| `html_url` | `string` |  |
| `labels_url` | `string` |  |
| `network_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `releases_url` | `string` |  |
| `permissions` | `object` |  |
| `events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `tags_url` | `string` |  |
| `visibility` | `string` |  |
| `node_id` | `string` |  |
| `keys_url` | `string` |  |
| `owner` | `object` | Simple User |
| `stargazers_count` | `integer` |  |
| `languages_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `language` | `string` |  |
| `fork` | `boolean` |  |
| `ssh_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `statuses_url` | `string` |  |
| `forks_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `topics` | `array` |  |
| `full_name` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `deployments_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `teams_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `size` | `integer` |  |
| `subscribers_url` | `string` |  |
| `subscription_url` | `string` |  |
| `issues_url` | `string` |  |
| `watchers` | `integer` |  |
| `contents_url` | `string` |  |
| `forks_url` | `string` |  |
| `comments_url` | `string` |  |
| `mirror_url` | `string` |  |
| `pulls_url` | `string` |  |
| `clone_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `homepage` | `string` |  |
| `open_issues` | `integer` |  |
| `archive_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `svn_url` | `string` |  |
| `url` | `string` |  |
| `milestones_url` | `string` |  |
| `pushed_at` | `string` |  |
| `disabled` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `archived` | `boolean` |  |
| `role_name` | `string` |  |
| `commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `license` | `object` |  |
| `subscribers_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `default_branch` | `string` |  |
| `updated_at` | `string` |  |
| `compare_url` | `string` |  |
| `has_downloads` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
