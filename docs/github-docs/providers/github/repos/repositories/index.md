---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
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
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `full_name` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `forks` | `integer` |  |
| `pulls_url` | `string` |  |
| `compare_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `contents_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `forks_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `url` | `string` |  |
| `releases_url` | `string` |  |
| `keys_url` | `string` |  |
| `svn_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `languages_url` | `string` |  |
| `archived` | `boolean` |  |
| `forks_count` | `integer` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `security_and_analysis` | `object` |  |
| `has_projects` | `boolean` |  |
| `git_url` | `string` |  |
| `archive_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `role_name` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `permissions` | `object` |  |
| `updated_at` | `string` |  |
| `fork` | `boolean` |  |
| `mirror_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `downloads_url` | `string` |  |
| `hooks_url` | `string` |  |
| `is_template` | `boolean` |  |
| `assignees_url` | `string` |  |
| `contributors_url` | `string` |  |
| `network_count` | `integer` |  |
| `tags_url` | `string` |  |
| `disabled` | `boolean` |  |
| `watchers` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `commits_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `merges_url` | `string` |  |
| `events_url` | `string` |  |
| `clone_url` | `string` |  |
| `milestones_url` | `string` |  |
| `issues_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `topics` | `array` |  |
| `open_issues` | `integer` |  |
| `homepage` | `string` |  |
| `has_downloads` | `boolean` |  |
| `statuses_url` | `string` |  |
| `language` | `string` |  |
| `subscription_url` | `string` |  |
| `teams_url` | `string` |  |
| `html_url` | `string` |  |
| `notifications_url` | `string` |  |
| `visibility` | `string` |  |
| `node_id` | `string` |  |
| `has_wiki` | `boolean` |  |
| `has_discussions` | `boolean` |  |
| `license` | `object` |  |
| `created_at` | `string` |  |
| `default_branch` | `string` |  |
| `open_issues_count` | `integer` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `issue_events_url` | `string` |  |
| `labels_url` | `string` |  |
| `comments_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `private` | `boolean` |  |
| `branches_url` | `string` |  |
| `trees_url` | `string` |  |
| `blobs_url` | `string` |  |
| `subscribers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
