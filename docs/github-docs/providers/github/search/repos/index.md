---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `clone_url` | `string` |  |
| `forks` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `default_branch` | `string` |  |
| `allow_forking` | `boolean` |  |
| `allow_rebase_merge` | `boolean` |  |
| `ssh_url` | `string` |  |
| `mirror_url` | `string` |  |
| `compare_url` | `string` |  |
| `forks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `teams_url` | `string` |  |
| `labels_url` | `string` |  |
| `subscription_url` | `string` |  |
| `is_template` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `assignees_url` | `string` |  |
| `watchers` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `issue_comment_url` | `string` |  |
| `git_url` | `string` |  |
| `full_name` | `string` |  |
| `open_issues_count` | `integer` |  |
| `keys_url` | `string` |  |
| `text_matches` | `array` |  |
| `created_at` | `string` |  |
| `archived` | `boolean` |  |
| `allow_auto_merge` | `boolean` |  |
| `license` | `object` | License Simple |
| `contents_url` | `string` |  |
| `commits_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `updated_at` | `string` |  |
| `git_tags_url` | `string` |  |
| `pushed_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `deployments_url` | `string` |  |
| `events_url` | `string` |  |
| `blobs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `notifications_url` | `string` |  |
| `milestones_url` | `string` |  |
| `private` | `boolean` |  |
| `tags_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `issues_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_issues` | `boolean` |  |
| `allow_merge_commit` | `boolean` |  |
| `language` | `string` |  |
| `trees_url` | `string` |  |
| `topics` | `array` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | Simple User |
| `node_id` | `string` |  |
| `branches_url` | `string` |  |
| `archive_url` | `string` |  |
| `url` | `string` |  |
| `downloads_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `allow_squash_merge` | `boolean` |  |
| `forks_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `fork` | `boolean` |  |
| `svn_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `size` | `integer` |  |
| `master_branch` | `string` |  |
| `has_pages` | `boolean` |  |
| `contributors_url` | `string` |  |
| `releases_url` | `string` |  |
| `pulls_url` | `string` |  |
| `permissions` | `object` |  |
| `score` | `number` |  |
| `languages_url` | `string` |  |
| `homepage` | `string` |  |
| `merges_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `hooks_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `repos` | `SELECT` | `q` |
