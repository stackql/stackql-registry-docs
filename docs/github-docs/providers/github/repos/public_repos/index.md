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
| `collaborators_url` | `string` |  |
| `teams_url` | `string` |  |
| `forks_count` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `topics` | `array` |  |
| `open_issues_count` | `integer` |  |
| `permissions` | `object` |  |
| `temp_clone_token` | `string` |  |
| `role_name` | `string` |  |
| `releases_url` | `string` |  |
| `is_template` | `boolean` |  |
| `assignees_url` | `string` |  |
| `keys_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `pulls_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `license` | `object` |  |
| `hooks_url` | `string` |  |
| `branches_url` | `string` |  |
| `updated_at` | `string` |  |
| `git_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `comments_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `watchers` | `integer` |  |
| `default_branch` | `string` |  |
| `network_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `language` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_pages` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `size` | `integer` |  |
| `deployments_url` | `string` |  |
| `compare_url` | `string` |  |
| `issues_url` | `string` |  |
| `notifications_url` | `string` |  |
| `private` | `boolean` |  |
| `labels_url` | `string` |  |
| `languages_url` | `string` |  |
| `blobs_url` | `string` |  |
| `milestones_url` | `string` |  |
| `events_url` | `string` |  |
| `open_issues` | `integer` |  |
| `tags_url` | `string` |  |
| `url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `subscription_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `statuses_url` | `string` |  |
| `merges_url` | `string` |  |
| `archived` | `boolean` |  |
| `downloads_url` | `string` |  |
| `trees_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `owner` | `object` | Simple User |
| `homepage` | `string` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `contributors_url` | `string` |  |
| `visibility` | `string` |  |
| `git_tags_url` | `string` |  |
| `archive_url` | `string` |  |
| `commits_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `clone_url` | `string` |  |
| `disabled` | `boolean` |  |
| `forks` | `integer` |  |
| `full_name` | `string` |  |
| `git_refs_url` | `string` |  |
| `created_at` | `string` |  |
| `mirror_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `contents_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `forks_url` | `string` |  |
| `svn_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
