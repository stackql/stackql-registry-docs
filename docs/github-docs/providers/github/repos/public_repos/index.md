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
| `milestones_url` | `string` |  |
| `disabled` | `boolean` |  |
| `is_template` | `boolean` |  |
| `comments_url` | `string` |  |
| `forks_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `homepage` | `string` |  |
| `owner` | `object` | Simple User |
| `notifications_url` | `string` |  |
| `releases_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `clone_url` | `string` |  |
| `events_url` | `string` |  |
| `archived` | `boolean` |  |
| `node_id` | `string` |  |
| `git_url` | `string` |  |
| `merges_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `forks` | `integer` |  |
| `git_refs_url` | `string` |  |
| `default_branch` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `forks_count` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `assignees_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `subscription_url` | `string` |  |
| `contributors_url` | `string` |  |
| `fork` | `boolean` |  |
| `updated_at` | `string` |  |
| `has_projects` | `boolean` |  |
| `size` | `integer` |  |
| `svn_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `visibility` | `string` |  |
| `topics` | `array` |  |
| `mirror_url` | `string` |  |
| `role_name` | `string` |  |
| `stargazers_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `url` | `string` |  |
| `tags_url` | `string` |  |
| `issues_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `created_at` | `string` |  |
| `keys_url` | `string` |  |
| `commits_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `allow_forking` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `contents_url` | `string` |  |
| `downloads_url` | `string` |  |
| `labels_url` | `string` |  |
| `full_name` | `string` |  |
| `network_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `hooks_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `watchers` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `permissions` | `object` |  |
| `private` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `statuses_url` | `string` |  |
| `blobs_url` | `string` |  |
| `compare_url` | `string` |  |
| `archive_url` | `string` |  |
| `teams_url` | `string` |  |
| `ssh_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `branches_url` | `string` |  |
| `trees_url` | `string` |  |
| `languages_url` | `string` |  |
| `language` | `string` |  |
| `license` | `object` |  |
| `pushed_at` | `string` |  |
| `subscribers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
