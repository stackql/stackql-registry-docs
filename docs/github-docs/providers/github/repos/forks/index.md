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
| `comments_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `role_name` | `string` |  |
| `events_url` | `string` |  |
| `commits_url` | `string` |  |
| `keys_url` | `string` |  |
| `owner` | `object` | Simple User |
| `pulls_url` | `string` |  |
| `permissions` | `object` |  |
| `blobs_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `compare_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `url` | `string` |  |
| `watchers` | `integer` |  |
| `html_url` | `string` |  |
| `homepage` | `string` |  |
| `milestones_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `labels_url` | `string` |  |
| `contributors_url` | `string` |  |
| `license` | `object` |  |
| `forks` | `integer` |  |
| `trees_url` | `string` |  |
| `clone_url` | `string` |  |
| `merges_url` | `string` |  |
| `created_at` | `string` |  |
| `languages_url` | `string` |  |
| `archive_url` | `string` |  |
| `visibility` | `string` |  |
| `is_template` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `size` | `integer` |  |
| `node_id` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `hooks_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `has_projects` | `boolean` |  |
| `language` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `downloads_url` | `string` |  |
| `topics` | `array` |  |
| `template_repository` | `object` | A git repository |
| `full_name` | `string` |  |
| `branches_url` | `string` |  |
| `pushed_at` | `string` |  |
| `private` | `boolean` |  |
| `git_url` | `string` |  |
| `deployments_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `statuses_url` | `string` |  |
| `updated_at` | `string` |  |
| `stargazers_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `releases_url` | `string` |  |
| `issues_url` | `string` |  |
| `forks_url` | `string` |  |
| `teams_url` | `string` |  |
| `forks_count` | `integer` |  |
| `tags_url` | `string` |  |
| `contents_url` | `string` |  |
| `notifications_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `assignees_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `network_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `svn_url` | `string` |  |
| `disabled` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `archived` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `default_branch` | `string` |  |
| `ssh_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
