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
| `security_and_analysis` | `object` |  |
| `notifications_url` | `string` |  |
| `topics` | `array` |  |
| `git_commits_url` | `string` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `labels_url` | `string` |  |
| `html_url` | `string` |  |
| `network_count` | `integer` |  |
| `clone_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `events_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `watchers` | `integer` |  |
| `assignees_url` | `string` |  |
| `forks_count` | `integer` |  |
| `node_id` | `string` |  |
| `archived` | `boolean` |  |
| `visibility` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `hooks_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_wiki` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `languages_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `merges_url` | `string` |  |
| `contents_url` | `string` |  |
| `private` | `boolean` |  |
| `forks` | `integer` |  |
| `license` | `object` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `disabled` | `boolean` |  |
| `full_name` | `string` |  |
| `statuses_url` | `string` |  |
| `mirror_url` | `string` |  |
| `downloads_url` | `string` |  |
| `releases_url` | `string` |  |
| `pulls_url` | `string` |  |
| `forks_url` | `string` |  |
| `language` | `string` |  |
| `created_at` | `string` |  |
| `is_template` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `svn_url` | `string` |  |
| `contributors_url` | `string` |  |
| `url` | `string` |  |
| `ssh_url` | `string` |  |
| `updated_at` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `comments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `blobs_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `milestones_url` | `string` |  |
| `subscription_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `teams_url` | `string` |  |
| `archive_url` | `string` |  |
| `branches_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `issues_url` | `string` |  |
| `tags_url` | `string` |  |
| `permissions` | `object` |  |
| `git_url` | `string` |  |
| `keys_url` | `string` |  |
| `fork` | `boolean` |  |
| `commits_url` | `string` |  |
| `open_issues` | `integer` |  |
| `stargazers_url` | `string` |  |
| `default_branch` | `string` |  |
| `issue_events_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `homepage` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).<br /><br />**Note**: Although this endpoint works with GitHub Apps, the GitHub App must be installed on the destination account with access to all repositories and on the source account with access to the source repository. |
