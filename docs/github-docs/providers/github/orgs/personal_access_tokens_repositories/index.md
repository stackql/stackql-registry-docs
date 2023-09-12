---
title: personal_access_tokens_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - personal_access_tokens_repositories
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
<tr><td><b>Name</b></td><td><code>personal_access_tokens_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.personal_access_tokens_repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `clone_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `homepage` | `string` |  |
| `assignees_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `pushed_at` | `string` |  |
| `subscription_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `archive_url` | `string` |  |
| `private` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `compare_url` | `string` |  |
| `notifications_url` | `string` |  |
| `open_issues` | `integer` |  |
| `commits_url` | `string` |  |
| `full_name` | `string` |  |
| `language` | `string` |  |
| `has_discussions` | `boolean` |  |
| `pulls_url` | `string` |  |
| `merges_url` | `string` |  |
| `forks_count` | `integer` |  |
| `branches_url` | `string` |  |
| `labels_url` | `string` |  |
| `comments_url` | `string` |  |
| `permissions` | `object` |  |
| `fork` | `boolean` |  |
| `ssh_url` | `string` |  |
| `keys_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `tags_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `created_at` | `string` |  |
| `has_issues` | `boolean` |  |
| `milestones_url` | `string` |  |
| `node_id` | `string` |  |
| `watchers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `statuses_url` | `string` |  |
| `license` | `object` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `issues_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `forks_url` | `string` |  |
| `svn_url` | `string` |  |
| `languages_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `mirror_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `subscribers_url` | `string` |  |
| `html_url` | `string` |  |
| `teams_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `network_count` | `integer` |  |
| `visibility` | `string` |  |
| `disabled` | `boolean` |  |
| `topics` | `array` |  |
| `events_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `default_branch` | `string` |  |
| `role_name` | `string` |  |
| `forks` | `integer` |  |
| `hooks_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `releases_url` | `string` |  |
| `archived` | `boolean` |  |
| `downloads_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `contents_url` | `string` |  |
| `trees_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `updated_at` | `string` |  |
| `has_pages` | `boolean` |  |
| `watchers` | `integer` |  |
| `git_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `deployments_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_repositories` | `SELECT` | `org, pat_id` |
