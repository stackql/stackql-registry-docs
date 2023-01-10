---
title: public_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - public_repos
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
<tr><td><b>Name</b></td><td><code>public_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.public_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `archive_url` | `string` |  |
| `is_template` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `compare_url` | `string` |  |
| `milestones_url` | `string` |  |
| `updated_at` | `string` |  |
| `has_pages` | `boolean` |  |
| `git_url` | `string` |  |
| `watchers` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `open_issues` | `integer` |  |
| `assignees_url` | `string` |  |
| `homepage` | `string` |  |
| `svn_url` | `string` |  |
| `owner` | `object` | Simple User |
| `branches_url` | `string` |  |
| `size` | `integer` |  |
| `downloads_url` | `string` |  |
| `network_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `role_name` | `string` |  |
| `issues_url` | `string` |  |
| `mirror_url` | `string` |  |
| `license` | `object` |  |
| `ssh_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `subscription_url` | `string` |  |
| `deployments_url` | `string` |  |
| `language` | `string` |  |
| `notifications_url` | `string` |  |
| `labels_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `statuses_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `clone_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `fork` | `boolean` |  |
| `releases_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `default_branch` | `string` |  |
| `pushed_at` | `string` |  |
| `node_id` | `string` |  |
| `git_refs_url` | `string` |  |
| `full_name` | `string` |  |
| `merges_url` | `string` |  |
| `disabled` | `boolean` |  |
| `events_url` | `string` |  |
| `commits_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `blobs_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `issue_comment_url` | `string` |  |
| `teams_url` | `string` |  |
| `html_url` | `string` |  |
| `forks` | `integer` |  |
| `visibility` | `string` |  |
| `collaborators_url` | `string` |  |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `topics` | `array` |  |
| `created_at` | `string` |  |
| `keys_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `forks_count` | `integer` |  |
| `permissions` | `object` |  |
| `contributors_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `languages_url` | `string` |  |
| `archived` | `boolean` |  |
| `contents_url` | `string` |  |
| `trees_url` | `string` |  |
| `comments_url` | `string` |  |
| `private` | `boolean` |  |
| `hooks_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `pulls_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
