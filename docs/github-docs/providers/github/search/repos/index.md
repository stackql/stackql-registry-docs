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
| `forks` | `integer` |  |
| `svn_url` | `string` |  |
| `languages_url` | `string` |  |
| `git_url` | `string` |  |
| `milestones_url` | `string` |  |
| `default_branch` | `string` |  |
| `has_wiki` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `mirror_url` | `string` |  |
| `branches_url` | `string` |  |
| `language` | `string` |  |
| `license` | `object` | License Simple |
| `merges_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `contents_url` | `string` |  |
| `compare_url` | `string` |  |
| `events_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `is_template` | `boolean` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `issue_comment_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `updated_at` | `string` |  |
| `fork` | `boolean` |  |
| `allow_auto_merge` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `text_matches` | `array` |  |
| `homepage` | `string` |  |
| `temp_clone_token` | `string` |  |
| `contributors_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `size` | `integer` |  |
| `forks_count` | `integer` |  |
| `trees_url` | `string` |  |
| `permissions` | `object` |  |
| `assignees_url` | `string` |  |
| `subscription_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `labels_url` | `string` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `commits_url` | `string` |  |
| `created_at` | `string` |  |
| `tags_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `notifications_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `pushed_at` | `string` |  |
| `releases_url` | `string` |  |
| `deployments_url` | `string` |  |
| `open_issues` | `integer` |  |
| `private` | `boolean` |  |
| `topics` | `array` |  |
| `has_pages` | `boolean` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `stargazers_count` | `integer` |  |
| `full_name` | `string` |  |
| `blobs_url` | `string` |  |
| `keys_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `url` | `string` |  |
| `pulls_url` | `string` |  |
| `watchers` | `integer` |  |
| `comments_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `master_branch` | `string` |  |
| `clone_url` | `string` |  |
| `owner` | `object` | Simple User |
| `archive_url` | `string` |  |
| `downloads_url` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `issues_url` | `string` |  |
| `ssh_url` | `string` |  |
| `teams_url` | `string` |  |
| `statuses_url` | `string` |  |
| `forks_url` | `string` |  |
| `hooks_url` | `string` |  |
| `archived` | `boolean` |  |
| `score` | `number` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `repos` | `SELECT` | `q` |
