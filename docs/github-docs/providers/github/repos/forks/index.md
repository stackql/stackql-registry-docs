---
title: forks
hide_title: false
hide_table_of_contents: false
keywords:
  - forks
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
<tr><td><b>Name</b></td><td><code>forks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.forks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `watchers_count` | `integer` |  |
| `commits_url` | `string` |  |
| `hooks_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `role_name` | `string` |  |
| `subscribers_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `languages_url` | `string` |  |
| `watchers` | `integer` |  |
| `contributors_url` | `string` |  |
| `pulls_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `milestones_url` | `string` |  |
| `owner` | `object` | Simple User |
| `private` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `forks_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `language` | `string` |  |
| `issues_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `forks_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `full_name` | `string` |  |
| `git_url` | `string` |  |
| `branches_url` | `string` |  |
| `forks` | `integer` |  |
| `blobs_url` | `string` |  |
| `ssh_url` | `string` |  |
| `homepage` | `string` |  |
| `comments_url` | `string` |  |
| `statuses_url` | `string` |  |
| `keys_url` | `string` |  |
| `merges_url` | `string` |  |
| `subscription_url` | `string` |  |
| `open_issues` | `integer` |  |
| `releases_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `archive_url` | `string` |  |
| `topics` | `array` |  |
| `stargazers_url` | `string` |  |
| `updated_at` | `string` |  |
| `teams_url` | `string` |  |
| `tags_url` | `string` |  |
| `labels_url` | `string` |  |
| `events_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `compare_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `default_branch` | `string` |  |
| `disabled` | `boolean` |  |
| `contents_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `archived` | `boolean` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `license` | `object` |  |
| `deployments_url` | `string` |  |
| `visibility` | `string` |  |
| `network_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `svn_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `size` | `integer` |  |
| `permissions` | `object` |  |
| `has_downloads` | `boolean` |  |
| `fork` | `boolean` |  |
| `clone_url` | `string` |  |
| `mirror_url` | `string` |  |
| `notifications_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `collaborators_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `html_url` | `string` |  |
| `assignees_url` | `string` |  |
| `url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `trees_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
