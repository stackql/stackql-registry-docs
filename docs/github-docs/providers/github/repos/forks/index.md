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
| `subscribers_url` | `string` |  |
| `contributors_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `deployments_url` | `string` |  |
| `is_template` | `boolean` |  |
| `archived` | `boolean` |  |
| `url` | `string` |  |
| `permissions` | `object` |  |
| `events_url` | `string` |  |
| `clone_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `statuses_url` | `string` |  |
| `merges_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `mirror_url` | `string` |  |
| `comments_url` | `string` |  |
| `private` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `subscription_url` | `string` |  |
| `assignees_url` | `string` |  |
| `default_branch` | `string` |  |
| `has_issues` | `boolean` |  |
| `git_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `subscribers_count` | `integer` |  |
| `updated_at` | `string` |  |
| `visibility` | `string` |  |
| `labels_url` | `string` |  |
| `forks_count` | `integer` |  |
| `trees_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `has_pages` | `boolean` |  |
| `html_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `web_commit_signoff_required` | `boolean` |  |
| `created_at` | `string` |  |
| `git_tags_url` | `string` |  |
| `role_name` | `string` |  |
| `teams_url` | `string` |  |
| `issues_url` | `string` |  |
| `svn_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `tags_url` | `string` |  |
| `downloads_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `forks_url` | `string` |  |
| `compare_url` | `string` |  |
| `watchers` | `integer` |  |
| `forks` | `integer` |  |
| `open_issues` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `commits_url` | `string` |  |
| `full_name` | `string` |  |
| `issue_comment_url` | `string` |  |
| `node_id` | `string` |  |
| `license` | `object` |  |
| `network_count` | `integer` |  |
| `topics` | `array` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `stargazers_url` | `string` |  |
| `language` | `string` |  |
| `archive_url` | `string` |  |
| `releases_url` | `string` |  |
| `contents_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `issue_events_url` | `string` |  |
| `fork` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `homepage` | `string` |  |
| `hooks_url` | `string` |  |
| `languages_url` | `string` |  |
| `notifications_url` | `string` |  |
| `branches_url` | `string` |  |
| `blobs_url` | `string` |  |
| `keys_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).<br /><br />**Note**: Although this endpoint works with GitHub Apps, the GitHub App must be installed on the destination account with access to all repositories and on the source account with access to the source repository. |
