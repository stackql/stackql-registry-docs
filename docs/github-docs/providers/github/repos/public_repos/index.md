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
| `events_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `blobs_url` | `string` |  |
| `merges_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `clone_url` | `string` |  |
| `labels_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `homepage` | `string` |  |
| `issue_comment_url` | `string` |  |
| `branches_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `language` | `string` |  |
| `network_count` | `integer` |  |
| `contents_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `archived` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `open_issues` | `integer` |  |
| `downloads_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `comments_url` | `string` |  |
| `notifications_url` | `string` |  |
| `issues_url` | `string` |  |
| `languages_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `url` | `string` |  |
| `commits_url` | `string` |  |
| `pulls_url` | `string` |  |
| `svn_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `license` | `object` |  |
| `size` | `integer` |  |
| `owner` | `object` | Simple User |
| `pushed_at` | `string` |  |
| `git_tags_url` | `string` |  |
| `permissions` | `object` |  |
| `git_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `forks_count` | `integer` |  |
| `keys_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `forks_url` | `string` |  |
| `node_id` | `string` |  |
| `subscription_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `default_branch` | `string` |  |
| `html_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `watchers` | `integer` |  |
| `private` | `boolean` |  |
| `created_at` | `string` |  |
| `full_name` | `string` |  |
| `ssh_url` | `string` |  |
| `forks` | `integer` |  |
| `hooks_url` | `string` |  |
| `archive_url` | `string` |  |
| `trees_url` | `string` |  |
| `visibility` | `string` |  |
| `open_issues_count` | `integer` |  |
| `teams_url` | `string` |  |
| `releases_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `role_name` | `string` |  |
| `mirror_url` | `string` |  |
| `is_template` | `boolean` |  |
| `topics` | `array` |  |
| `assignees_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `milestones_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `updated_at` | `string` |  |
| `statuses_url` | `string` |  |
| `tags_url` | `string` |  |
| `contributors_url` | `string` |  |
| `fork` | `boolean` |  |
| `deployments_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
