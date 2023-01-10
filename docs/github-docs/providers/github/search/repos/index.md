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
| `allow_merge_commit` | `boolean` |  |
| `milestones_url` | `string` |  |
| `pushed_at` | `string` |  |
| `notifications_url` | `string` |  |
| `permissions` | `object` |  |
| `allow_rebase_merge` | `boolean` |  |
| `contents_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `has_wiki` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `html_url` | `string` |  |
| `subscription_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `score` | `number` |  |
| `watchers_count` | `integer` |  |
| `forks` | `integer` |  |
| `has_issues` | `boolean` |  |
| `allow_squash_merge` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `node_id` | `string` |  |
| `is_template` | `boolean` |  |
| `license` | `object` | License Simple |
| `subscribers_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `archive_url` | `string` |  |
| `open_issues` | `integer` |  |
| `languages_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `issues_url` | `string` |  |
| `downloads_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `text_matches` | `array` |  |
| `owner` | `object` | Simple User |
| `compare_url` | `string` |  |
| `events_url` | `string` |  |
| `releases_url` | `string` |  |
| `svn_url` | `string` |  |
| `git_url` | `string` |  |
| `comments_url` | `string` |  |
| `deployments_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `trees_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `default_branch` | `string` |  |
| `tags_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `commits_url` | `string` |  |
| `forks_url` | `string` |  |
| `merges_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `url` | `string` |  |
| `keys_url` | `string` |  |
| `watchers` | `integer` |  |
| `full_name` | `string` |  |
| `issue_comment_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `fork` | `boolean` |  |
| `language` | `string` |  |
| `clone_url` | `string` |  |
| `pulls_url` | `string` |  |
| `size` | `integer` |  |
| `collaborators_url` | `string` |  |
| `updated_at` | `string` |  |
| `blobs_url` | `string` |  |
| `mirror_url` | `string` |  |
| `labels_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `teams_url` | `string` |  |
| `created_at` | `string` |  |
| `archived` | `boolean` |  |
| `ssh_url` | `string` |  |
| `hooks_url` | `string` |  |
| `branches_url` | `string` |  |
| `assignees_url` | `string` |  |
| `contributors_url` | `string` |  |
| `homepage` | `string` |  |
| `forks_count` | `integer` |  |
| `master_branch` | `string` |  |
| `private` | `boolean` |  |
| `statuses_url` | `string` |  |
| `topics` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `repos` | `SELECT` | `q` |
