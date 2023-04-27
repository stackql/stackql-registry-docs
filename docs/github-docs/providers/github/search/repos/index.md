---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
  - search
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `topics` | `array` |  |
| `is_template` | `boolean` |  |
| `forks` | `integer` |  |
| `fork` | `boolean` |  |
| `score` | `number` |  |
| `git_refs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `blobs_url` | `string` |  |
| `contents_url` | `string` |  |
| `mirror_url` | `string` |  |
| `commits_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `archive_url` | `string` |  |
| `teams_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `master_branch` | `string` |  |
| `events_url` | `string` |  |
| `text_matches` | `array` |  |
| `archived` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `git_tags_url` | `string` |  |
| `assignees_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `trees_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `watchers` | `integer` |  |
| `notifications_url` | `string` |  |
| `tags_url` | `string` |  |
| `clone_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `merges_url` | `string` |  |
| `subscription_url` | `string` |  |
| `forks_count` | `integer` |  |
| `license` | `object` | License Simple |
| `subscribers_url` | `string` |  |
| `contributors_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `git_url` | `string` |  |
| `hooks_url` | `string` |  |
| `full_name` | `string` |  |
| `issues_url` | `string` |  |
| `default_branch` | `string` |  |
| `html_url` | `string` |  |
| `private` | `boolean` |  |
| `size` | `integer` |  |
| `allow_rebase_merge` | `boolean` |  |
| `svn_url` | `string` |  |
| `permissions` | `object` |  |
| `allow_forking` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `labels_url` | `string` |  |
| `owner` | `object` | Simple User |
| `milestones_url` | `string` |  |
| `comments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_projects` | `boolean` |  |
| `allow_merge_commit` | `boolean` |  |
| `homepage` | `string` |  |
| `languages_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `ssh_url` | `string` |  |
| `url` | `string` |  |
| `compare_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `downloads_url` | `string` |  |
| `releases_url` | `string` |  |
| `created_at` | `string` |  |
| `keys_url` | `string` |  |
| `language` | `string` |  |
| `pushed_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `deployments_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `branches_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `repos` | `SELECT` | `q` |
