---
title: repos_for_pat_grant_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_for_pat_grant_requests
  - orgs
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
<tr><td><b>Name</b></td><td><code>repos_for_pat_grant_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.repos_for_pat_grant_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `forks_count` | `integer` |  |
| `clone_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `full_name` | `string` |  |
| `url` | `string` |  |
| `language` | `string` |  |
| `subscribers_url` | `string` |  |
| `assignees_url` | `string` |  |
| `default_branch` | `string` |  |
| `ssh_url` | `string` |  |
| `merges_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `contents_url` | `string` |  |
| `languages_url` | `string` |  |
| `notifications_url` | `string` |  |
| `blobs_url` | `string` |  |
| `forks` | `integer` |  |
| `updated_at` | `string` |  |
| `visibility` | `string` |  |
| `topics` | `array` |  |
| `issue_comment_url` | `string` |  |
| `tags_url` | `string` |  |
| `compare_url` | `string` |  |
| `branches_url` | `string` |  |
| `statuses_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `releases_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `mirror_url` | `string` |  |
| `disabled` | `boolean` |  |
| `homepage` | `string` |  |
| `role_name` | `string` |  |
| `node_id` | `string` |  |
| `issue_events_url` | `string` |  |
| `hooks_url` | `string` |  |
| `open_issues` | `integer` |  |
| `git_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `comments_url` | `string` |  |
| `subscription_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `labels_url` | `string` |  |
| `svn_url` | `string` |  |
| `archived` | `boolean` |  |
| `forks_url` | `string` |  |
| `issues_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `private` | `boolean` |  |
| `license` | `object` |  |
| `deployments_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `downloads_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `contributors_url` | `string` |  |
| `is_template` | `boolean` |  |
| `network_count` | `integer` |  |
| `git_refs_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `events_url` | `string` |  |
| `teams_url` | `string` |  |
| `permissions` | `object` |  |
| `stargazers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `trees_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `watchers` | `integer` |  |
| `commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `archive_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `keys_url` | `string` |  |
| `created_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `fork` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_request_repositories` | `SELECT` | `org, pat_request_id` |
