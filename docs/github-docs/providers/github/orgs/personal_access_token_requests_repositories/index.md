---
title: personal_access_token_requests_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - personal_access_token_requests_repositories
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
<tr><td><b>Name</b></td><td><code>personal_access_token_requests_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.personal_access_token_requests_repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `blobs_url` | `string` |  |
| `disabled` | `boolean` |  |
| `svn_url` | `string` |  |
| `url` | `string` |  |
| `homepage` | `string` |  |
| `html_url` | `string` |  |
| `git_url` | `string` |  |
| `milestones_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `downloads_url` | `string` |  |
| `topics` | `array` |  |
| `has_pages` | `boolean` |  |
| `private` | `boolean` |  |
| `ssh_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `assignees_url` | `string` |  |
| `subscription_url` | `string` |  |
| `teams_url` | `string` |  |
| `full_name` | `string` |  |
| `merges_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `open_issues` | `integer` |  |
| `owner` | `object` | A GitHub user. |
| `temp_clone_token` | `string` |  |
| `issues_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `forks` | `integer` |  |
| `fork` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `releases_url` | `string` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `comments_url` | `string` |  |
| `mirror_url` | `string` |  |
| `labels_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `permissions` | `object` |  |
| `visibility` | `string` |  |
| `branches_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `languages_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `hooks_url` | `string` |  |
| `contents_url` | `string` |  |
| `license` | `object` |  |
| `has_discussions` | `boolean` |  |
| `compare_url` | `string` |  |
| `forks_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `keys_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `network_count` | `integer` |  |
| `security_and_analysis` | `object` |  |
| `statuses_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `tags_url` | `string` |  |
| `contributors_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `has_projects` | `boolean` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `default_branch` | `string` |  |
| `open_issues_count` | `integer` |  |
| `language` | `string` |  |
| `notifications_url` | `string` |  |
| `clone_url` | `string` |  |
| `commits_url` | `string` |  |
| `created_at` | `string` |  |
| `archive_url` | `string` |  |
| `deployments_url` | `string` |  |
| `watchers` | `integer` |  |
| `updated_at` | `string` |  |
| `archived` | `boolean` |  |
| `pushed_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_request_repositories` | `SELECT` | `org, pat_request_id` |
