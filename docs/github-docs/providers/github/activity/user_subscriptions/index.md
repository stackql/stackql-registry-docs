---
title: user_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_subscriptions
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
<tr><td><b>Name</b></td><td><code>user_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.user_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `has_pages` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `permissions` | `object` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `open_issues` | `integer` |  |
| `labels_url` | `string` |  |
| `watchers` | `integer` |  |
| `archive_url` | `string` |  |
| `keys_url` | `string` |  |
| `fork` | `boolean` |  |
| `topics` | `array` |  |
| `merges_url` | `string` |  |
| `blobs_url` | `string` |  |
| `archived` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `branches_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `contents_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `events_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `languages_url` | `string` |  |
| `network_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `tags_url` | `string` |  |
| `forks_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `visibility` | `string` |  |
| `git_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `releases_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `full_name` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `assignees_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `mirror_url` | `string` |  |
| `forks_url` | `string` |  |
| `created_at` | `string` |  |
| `statuses_url` | `string` |  |
| `homepage` | `string` |  |
| `pulls_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `clone_url` | `string` |  |
| `license` | `object` |  |
| `temp_clone_token` | `string` |  |
| `url` | `string` |  |
| `subscribers_url` | `string` |  |
| `trees_url` | `string` |  |
| `downloads_url` | `string` |  |
| `pushed_at` | `string` |  |
| `role_name` | `string` |  |
| `contributors_url` | `string` |  |
| `svn_url` | `string` |  |
| `language` | `string` |  |
| `notifications_url` | `string` |  |
| `private` | `boolean` |  |
| `compare_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `commits_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `updated_at` | `string` |  |
| `comments_url` | `string` |  |
| `ssh_url` | `string` |  |
| `deployments_url` | `string` |  |
| `default_branch` | `string` |  |
| `issues_url` | `string` |  |
| `teams_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `disabled` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `forks` | `integer` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_watched_repos_for_authenticated_user` | `SELECT` |  |
