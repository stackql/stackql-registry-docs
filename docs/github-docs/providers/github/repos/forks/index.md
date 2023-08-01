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
| `has_pages` | `boolean` |  |
| `private` | `boolean` |  |
| `pulls_url` | `string` |  |
| `open_issues` | `integer` |  |
| `statuses_url` | `string` |  |
| `blobs_url` | `string` |  |
| `url` | `string` |  |
| `events_url` | `string` |  |
| `contents_url` | `string` |  |
| `commits_url` | `string` |  |
| `node_id` | `string` |  |
| `contributors_url` | `string` |  |
| `topics` | `array` |  |
| `allow_forking` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `branches_url` | `string` |  |
| `license` | `object` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `homepage` | `string` |  |
| `owner` | `object` | Simple User |
| `releases_url` | `string` |  |
| `milestones_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `comments_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `clone_url` | `string` |  |
| `issues_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `updated_at` | `string` |  |
| `teams_url` | `string` |  |
| `visibility` | `string` |  |
| `subscription_url` | `string` |  |
| `languages_url` | `string` |  |
| `full_name` | `string` |  |
| `stargazers_url` | `string` |  |
| `compare_url` | `string` |  |
| `forks` | `integer` |  |
| `is_template` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `keys_url` | `string` |  |
| `trees_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `svn_url` | `string` |  |
| `notifications_url` | `string` |  |
| `assignees_url` | `string` |  |
| `created_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `size` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `fork` | `boolean` |  |
| `downloads_url` | `string` |  |
| `archive_url` | `string` |  |
| `merges_url` | `string` |  |
| `disabled` | `boolean` |  |
| `pushed_at` | `string` |  |
| `forks_url` | `string` |  |
| `role_name` | `string` |  |
| `has_downloads` | `boolean` |  |
| `watchers` | `integer` |  |
| `permissions` | `object` |  |
| `network_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `default_branch` | `string` |  |
| `forks_count` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_projects` | `boolean` |  |
| `git_url` | `string` |  |
| `tags_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `deployments_url` | `string` |  |
| `hooks_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `subscribers_url` | `string` |  |
| `labels_url` | `string` |  |
| `ssh_url` | `string` |  |
| `archived` | `boolean` |  |
| `language` | `string` |  |
| `mirror_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
