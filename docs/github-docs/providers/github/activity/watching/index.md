---
title: watching
hide_title: false
hide_table_of_contents: false
keywords:
  - watching
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
<tr><td><b>Name</b></td><td><code>watching</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.watching</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `svn_url` | `string` |  |
| `topics` | `array` |  |
| `license` | `object` |  |
| `html_url` | `string` |  |
| `downloads_url` | `string` |  |
| `homepage` | `string` |  |
| `language` | `string` |  |
| `labels_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `default_branch` | `string` |  |
| `issue_comment_url` | `string` |  |
| `open_issues` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `is_template` | `boolean` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `created_at` | `string` |  |
| `has_downloads` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `notifications_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `forks_url` | `string` |  |
| `git_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `statuses_url` | `string` |  |
| `archived` | `boolean` |  |
| `mirror_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `full_name` | `string` |  |
| `subscribers_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `permissions` | `object` |  |
| `updated_at` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `teams_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `releases_url` | `string` |  |
| `private` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `tags_url` | `string` |  |
| `languages_url` | `string` |  |
| `archive_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `disabled` | `boolean` |  |
| `issues_url` | `string` |  |
| `fork` | `boolean` |  |
| `events_url` | `string` |  |
| `deployments_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `keys_url` | `string` |  |
| `forks` | `integer` |  |
| `commits_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `merges_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `pushed_at` | `string` |  |
| `hooks_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `node_id` | `string` |  |
| `compare_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `contributors_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `forks_count` | `integer` |  |
| `url` | `string` |  |
| `network_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `visibility` | `string` |  |
| `clone_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `branches_url` | `string` |  |
| `comments_url` | `string` |  |
| `watchers` | `integer` |  |
| `subscription_url` | `string` |  |
| `contents_url` | `string` |  |
| `ssh_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
