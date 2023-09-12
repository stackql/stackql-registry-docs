---
title: users_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - users_subscriptions
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
<tr><td><b>Name</b></td><td><code>users_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.users_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `contributors_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `updated_at` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `is_template` | `boolean` |  |
| `languages_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `deployments_url` | `string` |  |
| `watchers` | `integer` |  |
| `visibility` | `string` |  |
| `compare_url` | `string` |  |
| `events_url` | `string` |  |
| `forks` | `integer` |  |
| `watchers_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `notifications_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `node_id` | `string` |  |
| `issue_comment_url` | `string` |  |
| `archive_url` | `string` |  |
| `private` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `keys_url` | `string` |  |
| `comments_url` | `string` |  |
| `clone_url` | `string` |  |
| `html_url` | `string` |  |
| `labels_url` | `string` |  |
| `merges_url` | `string` |  |
| `assignees_url` | `string` |  |
| `milestones_url` | `string` |  |
| `homepage` | `string` |  |
| `blobs_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `full_name` | `string` |  |
| `commits_url` | `string` |  |
| `url` | `string` |  |
| `subscription_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `open_issues` | `integer` |  |
| `role_name` | `string` |  |
| `language` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `trees_url` | `string` |  |
| `forks_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `ssh_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `branches_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `created_at` | `string` |  |
| `has_projects` | `boolean` |  |
| `topics` | `array` |  |
| `downloads_url` | `string` |  |
| `forks_url` | `string` |  |
| `permissions` | `object` |  |
| `temp_clone_token` | `string` |  |
| `has_issues` | `boolean` |  |
| `has_discussions` | `boolean` |  |
| `tags_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `pulls_url` | `string` |  |
| `license` | `object` |  |
| `has_downloads` | `boolean` |  |
| `releases_url` | `string` |  |
| `disabled` | `boolean` |  |
| `archived` | `boolean` |  |
| `fork` | `boolean` |  |
| `issues_url` | `string` |  |
| `teams_url` | `string` |  |
| `svn_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `pushed_at` | `string` |  |
| `allow_forking` | `boolean` |  |
| `network_count` | `integer` |  |
| `contents_url` | `string` |  |
| `default_branch` | `string` |  |
| `stargazers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_repos_watched_by_user` | `SELECT` | `username` |
