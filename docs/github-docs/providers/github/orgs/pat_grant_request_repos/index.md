---
title: pat_grant_request_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - pat_grant_request_repos
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
<tr><td><b>Name</b></td><td><code>pat_grant_request_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.pat_grant_request_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `is_template` | `boolean` |  |
| `private` | `boolean` |  |
| `url` | `string` |  |
| `collaborators_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `html_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `milestones_url` | `string` |  |
| `forks_url` | `string` |  |
| `releases_url` | `string` |  |
| `forks_count` | `integer` |  |
| `branches_url` | `string` |  |
| `subscription_url` | `string` |  |
| `clone_url` | `string` |  |
| `commits_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `node_id` | `string` |  |
| `has_issues` | `boolean` |  |
| `permissions` | `object` |  |
| `hooks_url` | `string` |  |
| `events_url` | `string` |  |
| `teams_url` | `string` |  |
| `language` | `string` |  |
| `network_count` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `comments_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `assignees_url` | `string` |  |
| `contributors_url` | `string` |  |
| `visibility` | `string` |  |
| `notifications_url` | `string` |  |
| `fork` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `security_and_analysis` | `object` |  |
| `merges_url` | `string` |  |
| `pulls_url` | `string` |  |
| `open_issues` | `integer` |  |
| `tags_url` | `string` |  |
| `downloads_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `blobs_url` | `string` |  |
| `keys_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `mirror_url` | `string` |  |
| `default_branch` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `pushed_at` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `updated_at` | `string` |  |
| `issues_url` | `string` |  |
| `svn_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `role_name` | `string` |  |
| `has_downloads` | `boolean` |  |
| `watchers` | `integer` |  |
| `languages_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `compare_url` | `string` |  |
| `license` | `object` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `homepage` | `string` |  |
| `archived` | `boolean` |  |
| `created_at` | `string` |  |
| `forks` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `trees_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `archive_url` | `string` |  |
| `deployments_url` | `string` |  |
| `git_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `disabled` | `boolean` |  |
| `labels_url` | `string` |  |
| `topics` | `array` |  |
| `ssh_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `full_name` | `string` |  |
| `contents_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_request_repositories` | `SELECT` | `org, pat_request_id` |
