---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - repos
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `contents_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `notifications_url` | `string` |  |
| `disabled` | `boolean` |  |
| `ssh_url` | `string` |  |
| `topics` | `array` |  |
| `issues_url` | `string` |  |
| `branches_url` | `string` |  |
| `comments_url` | `string` |  |
| `default_branch` | `string` |  |
| `security_and_analysis` | `object` |  |
| `releases_url` | `string` |  |
| `permissions` | `object` |  |
| `subscription_url` | `string` |  |
| `network_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `compare_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `full_name` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `forks_url` | `string` |  |
| `pushed_at` | `string` |  |
| `stargazers_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `fork` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `merges_url` | `string` |  |
| `labels_url` | `string` |  |
| `homepage` | `string` |  |
| `forks_count` | `integer` |  |
| `owner` | `object` | A GitHub user. |
| `git_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `node_id` | `string` |  |
| `languages_url` | `string` |  |
| `url` | `string` |  |
| `issue_events_url` | `string` |  |
| `html_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `contributors_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `has_discussions` | `boolean` |  |
| `visibility` | `string` |  |
| `language` | `string` |  |
| `forks` | `integer` |  |
| `private` | `boolean` |  |
| `tags_url` | `string` |  |
| `downloads_url` | `string` |  |
| `hooks_url` | `string` |  |
| `clone_url` | `string` |  |
| `archived` | `boolean` |  |
| `updated_at` | `string` |  |
| `git_commits_url` | `string` |  |
| `license` | `object` |  |
| `keys_url` | `string` |  |
| `mirror_url` | `string` |  |
| `deployments_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `svn_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `created_at` | `string` |  |
| `subscribers_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `pulls_url` | `string` |  |
| `commits_url` | `string` |  |
| `statuses_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `archive_url` | `string` |  |
| `open_issues` | `integer` |  |
| `blobs_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `watchers` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `teams_url` | `string` |  |
| `events_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_user` | `SELECT` | `username` |
