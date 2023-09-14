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
| `branches_url` | `string` |  |
| `comments_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `open_issues` | `integer` |  |
| `ssh_url` | `string` |  |
| `archived` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `deployments_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `topics` | `array` |  |
| `trees_url` | `string` |  |
| `forks_count` | `integer` |  |
| `teams_url` | `string` |  |
| `releases_url` | `string` |  |
| `issues_url` | `string` |  |
| `network_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `forks` | `integer` |  |
| `notifications_url` | `string` |  |
| `homepage` | `string` |  |
| `subscribers_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `contributors_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `tags_url` | `string` |  |
| `hooks_url` | `string` |  |
| `node_id` | `string` |  |
| `downloads_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `merges_url` | `string` |  |
| `clone_url` | `string` |  |
| `created_at` | `string` |  |
| `git_url` | `string` |  |
| `watchers` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `full_name` | `string` |  |
| `stargazers_url` | `string` |  |
| `compare_url` | `string` |  |
| `contents_url` | `string` |  |
| `events_url` | `string` |  |
| `keys_url` | `string` |  |
| `is_template` | `boolean` |  |
| `updated_at` | `string` |  |
| `statuses_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `visibility` | `string` |  |
| `role_name` | `string` |  |
| `commits_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `blobs_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `permissions` | `object` |  |
| `archive_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `license` | `object` |  |
| `svn_url` | `string` |  |
| `mirror_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `fork` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `labels_url` | `string` |  |
| `private` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `subscription_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `languages_url` | `string` |  |
| `forks_url` | `string` |  |
| `language` | `string` |  |
| `url` | `string` |  |
| `milestones_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `default_branch` | `string` |  |
| `has_downloads` | `boolean` |  |
| `html_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `pushed_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_watched_by_user` | `SELECT` | `username` | Lists repositories a user is watching. |
| `list_watched_repos_for_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user is watching. |
