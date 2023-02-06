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
| `node_id` | `string` |  |
| `branches_url` | `string` |  |
| `labels_url` | `string` |  |
| `clone_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `hooks_url` | `string` |  |
| `events_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `compare_url` | `string` |  |
| `mirror_url` | `string` |  |
| `url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `size` | `integer` |  |
| `releases_url` | `string` |  |
| `forks` | `integer` |  |
| `svn_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `statuses_url` | `string` |  |
| `pulls_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `notifications_url` | `string` |  |
| `tags_url` | `string` |  |
| `forks_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `homepage` | `string` |  |
| `language` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `contents_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `contributors_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `blobs_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `archive_url` | `string` |  |
| `archived` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `watchers` | `integer` |  |
| `default_branch` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `score` | `number` |  |
| `full_name` | `string` |  |
| `permissions` | `object` |  |
| `updated_at` | `string` |  |
| `stargazers_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `commits_url` | `string` |  |
| `deployments_url` | `string` |  |
| `comments_url` | `string` |  |
| `is_template` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `merges_url` | `string` |  |
| `languages_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `milestones_url` | `string` |  |
| `created_at` | `string` |  |
| `topics` | `array` |  |
| `issues_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `subscription_url` | `string` |  |
| `fork` | `boolean` |  |
| `teams_url` | `string` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `open_issues` | `integer` |  |
| `owner` | `object` | Simple User |
| `downloads_url` | `string` |  |
| `git_url` | `string` |  |
| `master_branch` | `string` |  |
| `temp_clone_token` | `string` |  |
| `text_matches` | `array` |  |
| `allow_rebase_merge` | `boolean` |  |
| `license` | `object` | License Simple |
| `assignees_url` | `string` |  |
| `forks_count` | `integer` |  |
| `private` | `boolean` |  |
| `keys_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `html_url` | `string` |  |
| `trees_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `repos` | `SELECT` | `q` |
