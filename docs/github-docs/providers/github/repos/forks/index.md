---
title: forks
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `events_url` | `string` |  |
| `default_branch` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `teams_url` | `string` |  |
| `updated_at` | `string` |  |
| `pulls_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `comments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `full_name` | `string` |  |
| `watchers_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `keys_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `releases_url` | `string` |  |
| `created_at` | `string` |  |
| `subscribers_url` | `string` |  |
| `forks` | `integer` |  |
| `languages_url` | `string` |  |
| `commits_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `homepage` | `string` |  |
| `tags_url` | `string` |  |
| `hooks_url` | `string` |  |
| `private` | `boolean` |  |
| `trees_url` | `string` |  |
| `downloads_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `watchers` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `language` | `string` |  |
| `git_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `archive_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `archived` | `boolean` |  |
| `owner` | `object` | Simple User |
| `delete_branch_on_merge` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `assignees_url` | `string` |  |
| `milestones_url` | `string` |  |
| `is_template` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `deployments_url` | `string` |  |
| `size` | `integer` |  |
| `blobs_url` | `string` |  |
| `labels_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `branches_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `forks_url` | `string` |  |
| `role_name` | `string` |  |
| `network_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `disabled` | `boolean` |  |
| `fork` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `issues_url` | `string` |  |
| `merges_url` | `string` |  |
| `topics` | `array` |  |
| `node_id` | `string` |  |
| `issue_events_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `ssh_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `statuses_url` | `string` |  |
| `visibility` | `string` |  |
| `contributors_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `compare_url` | `string` |  |
| `notifications_url` | `string` |  |
| `open_issues` | `integer` |  |
| `clone_url` | `string` |  |
| `permissions` | `object` |  |
| `license` | `object` |  |
| `contents_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api). |
