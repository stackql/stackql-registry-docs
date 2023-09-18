---
title: repos_for_pat_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_for_pat_grants
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
<tr><td><b>Name</b></td><td><code>repos_for_pat_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.repos_for_pat_grants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `has_downloads` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `html_url` | `string` |  |
| `fork` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `homepage` | `string` |  |
| `updated_at` | `string` |  |
| `comments_url` | `string` |  |
| `downloads_url` | `string` |  |
| `language` | `string` |  |
| `subscription_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `has_discussions` | `boolean` |  |
| `forks` | `integer` |  |
| `issues_url` | `string` |  |
| `compare_url` | `string` |  |
| `forks_url` | `string` |  |
| `url` | `string` |  |
| `statuses_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `tags_url` | `string` |  |
| `network_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `forks_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `archive_url` | `string` |  |
| `releases_url` | `string` |  |
| `teams_url` | `string` |  |
| `private` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `keys_url` | `string` |  |
| `hooks_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `pushed_at` | `string` |  |
| `visibility` | `string` |  |
| `full_name` | `string` |  |
| `labels_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `contents_url` | `string` |  |
| `assignees_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `open_issues` | `integer` |  |
| `milestones_url` | `string` |  |
| `archived` | `boolean` |  |
| `is_template` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `notifications_url` | `string` |  |
| `events_url` | `string` |  |
| `git_url` | `string` |  |
| `topics` | `array` |  |
| `role_name` | `string` |  |
| `node_id` | `string` |  |
| `temp_clone_token` | `string` |  |
| `subscribers_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `merges_url` | `string` |  |
| `ssh_url` | `string` |  |
| `clone_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `trees_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `deployments_url` | `string` |  |
| `permissions` | `object` |  |
| `commits_url` | `string` |  |
| `disabled` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `license` | `object` |  |
| `languages_url` | `string` |  |
| `watchers` | `integer` |  |
| `stargazers_url` | `string` |  |
| `default_branch` | `string` |  |
| `created_at` | `string` |  |
| `svn_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `mirror_url` | `string` |  |
| `branches_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_repositories` | `SELECT` | `org, pat_id` |
