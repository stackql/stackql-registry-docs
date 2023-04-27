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
| `comments_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `blobs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `archived` | `boolean` |  |
| `commits_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `pushed_at` | `string` |  |
| `fork` | `boolean` |  |
| `downloads_url` | `string` |  |
| `private` | `boolean` |  |
| `events_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `labels_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `updated_at` | `string` |  |
| `contributors_url` | `string` |  |
| `issues_url` | `string` |  |
| `clone_url` | `string` |  |
| `releases_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `trees_url` | `string` |  |
| `keys_url` | `string` |  |
| `url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `teams_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `stargazers_count` | `integer` |  |
| `license` | `object` |  |
| `visibility` | `string` |  |
| `mirror_url` | `string` |  |
| `created_at` | `string` |  |
| `git_url` | `string` |  |
| `subscription_url` | `string` |  |
| `watchers` | `integer` |  |
| `pulls_url` | `string` |  |
| `full_name` | `string` |  |
| `assignees_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `node_id` | `string` |  |
| `hooks_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `tags_url` | `string` |  |
| `owner` | `object` | Simple User |
| `default_branch` | `string` |  |
| `has_wiki` | `boolean` |  |
| `deployments_url` | `string` |  |
| `milestones_url` | `string` |  |
| `languages_url` | `string` |  |
| `notifications_url` | `string` |  |
| `disabled` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `permissions` | `object` |  |
| `git_tags_url` | `string` |  |
| `merges_url` | `string` |  |
| `size` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `forks_url` | `string` |  |
| `role_name` | `string` |  |
| `open_issues_count` | `integer` |  |
| `statuses_url` | `string` |  |
| `ssh_url` | `string` |  |
| `contents_url` | `string` |  |
| `svn_url` | `string` |  |
| `topics` | `array` |  |
| `has_downloads` | `boolean` |  |
| `language` | `string` |  |
| `branches_url` | `string` |  |
| `forks` | `integer` |  |
| `open_issues` | `integer` |  |
| `archive_url` | `string` |  |
| `network_count` | `integer` |  |
| `compare_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `homepage` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
