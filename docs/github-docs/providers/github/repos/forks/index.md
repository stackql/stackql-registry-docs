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
| `mirror_url` | `string` |  |
| `is_template` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `forks` | `integer` |  |
| `language` | `string` |  |
| `comments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `updated_at` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `fork` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `events_url` | `string` |  |
| `statuses_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `tags_url` | `string` |  |
| `issues_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `node_id` | `string` |  |
| `teams_url` | `string` |  |
| `clone_url` | `string` |  |
| `svn_url` | `string` |  |
| `trees_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `private` | `boolean` |  |
| `git_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `archive_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `html_url` | `string` |  |
| `branches_url` | `string` |  |
| `full_name` | `string` |  |
| `permissions` | `object` |  |
| `assignees_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `git_refs_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `topics` | `array` |  |
| `disabled` | `boolean` |  |
| `contributors_url` | `string` |  |
| `hooks_url` | `string` |  |
| `labels_url` | `string` |  |
| `watchers` | `integer` |  |
| `releases_url` | `string` |  |
| `notifications_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `blobs_url` | `string` |  |
| `compare_url` | `string` |  |
| `visibility` | `string` |  |
| `ssh_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `pushed_at` | `string` |  |
| `forks_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `homepage` | `string` |  |
| `subscription_url` | `string` |  |
| `url` | `string` |  |
| `archived` | `boolean` |  |
| `forks_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `network_count` | `integer` |  |
| `role_name` | `string` |  |
| `default_branch` | `string` |  |
| `license` | `object` |  |
| `stargazers_url` | `string` |  |
| `keys_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `downloads_url` | `string` |  |
| `contents_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `open_issues` | `integer` |  |
| `languages_url` | `string` |  |
| `commits_url` | `string` |  |
| `pulls_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `security_and_analysis` | `object` |  |
| `merges_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `owner, repo` |  |
| `create_fork` | `INSERT` | `owner, repo` | Create a fork for the authenticated user.<br /><br />**Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).<br /><br />**Note**: Although this endpoint works with GitHub Apps, the GitHub App must be installed on the destination account with access to all repositories and on the source account with access to the source repository. |
