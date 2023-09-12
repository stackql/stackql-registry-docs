---
title: orgs_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_repositories
  - migrations
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
<tr><td><b>Name</b></td><td><code>orgs_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.orgs_repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `topics` | `array` |  |
| `role_name` | `string` |  |
| `has_wiki` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `git_url` | `string` |  |
| `downloads_url` | `string` |  |
| `pushed_at` | `string` |  |
| `languages_url` | `string` |  |
| `branches_url` | `string` |  |
| `mirror_url` | `string` |  |
| `milestones_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `permissions` | `object` |  |
| `homepage` | `string` |  |
| `collaborators_url` | `string` |  |
| `archived` | `boolean` |  |
| `comments_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `open_issues` | `integer` |  |
| `clone_url` | `string` |  |
| `teams_url` | `string` |  |
| `notifications_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `events_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `subscribers_count` | `integer` |  |
| `license` | `object` |  |
| `stargazers_count` | `integer` |  |
| `fork` | `boolean` |  |
| `labels_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `deployments_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `network_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `compare_url` | `string` |  |
| `contributors_url` | `string` |  |
| `releases_url` | `string` |  |
| `watchers` | `integer` |  |
| `keys_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `updated_at` | `string` |  |
| `contents_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `forks_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `commits_url` | `string` |  |
| `default_branch` | `string` |  |
| `statuses_url` | `string` |  |
| `disabled` | `boolean` |  |
| `subscription_url` | `string` |  |
| `assignees_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `trees_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `forks_count` | `integer` |  |
| `archive_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `merges_url` | `string` |  |
| `private` | `boolean` |  |
| `tags_url` | `string` |  |
| `visibility` | `string` |  |
| `created_at` | `string` |  |
| `watchers_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `url` | `string` |  |
| `full_name` | `string` |  |
| `forks` | `integer` |  |
| `svn_url` | `string` |  |
| `language` | `string` |  |
| `blobs_url` | `string` |  |
| `pulls_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `hooks_url` | `string` |  |
| `issues_url` | `string` |  |
| `ssh_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_repos_for_org` | `SELECT` | `migration_id, org` |
