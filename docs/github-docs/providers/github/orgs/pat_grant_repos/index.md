---
title: pat_grant_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - pat_grant_repos
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
<tr><td><b>Name</b></td><td><code>pat_grant_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.pat_grant_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `license` | `object` |  |
| `has_downloads` | `boolean` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `subscription_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `assignees_url` | `string` |  |
| `url` | `string` |  |
| `blobs_url` | `string` |  |
| `default_branch` | `string` |  |
| `created_at` | `string` |  |
| `pushed_at` | `string` |  |
| `subscribers_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `issues_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `downloads_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `labels_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `notifications_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `language` | `string` |  |
| `ssh_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `permissions` | `object` |  |
| `watchers` | `integer` |  |
| `visibility` | `string` |  |
| `full_name` | `string` |  |
| `updated_at` | `string` |  |
| `contents_url` | `string` |  |
| `statuses_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `has_discussions` | `boolean` |  |
| `branches_url` | `string` |  |
| `deployments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `git_url` | `string` |  |
| `releases_url` | `string` |  |
| `languages_url` | `string` |  |
| `contributors_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `private` | `boolean` |  |
| `comments_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `git_refs_url` | `string` |  |
| `trees_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `keys_url` | `string` |  |
| `clone_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `archive_url` | `string` |  |
| `network_count` | `integer` |  |
| `commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `git_tags_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `archived` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `events_url` | `string` |  |
| `forks` | `integer` |  |
| `is_template` | `boolean` |  |
| `fork` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `forks_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `disabled` | `boolean` |  |
| `merges_url` | `string` |  |
| `tags_url` | `string` |  |
| `teams_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `role_name` | `string` |  |
| `topics` | `array` |  |
| `compare_url` | `string` |  |
| `pulls_url` | `string` |  |
| `homepage` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pat_grant_repositories` | `SELECT` | `org, pat_id` |
