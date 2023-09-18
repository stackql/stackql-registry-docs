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
| `teams_url` | `string` |  |
| `is_template` | `boolean` |  |
| `forks_url` | `string` |  |
| `full_name` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `score` | `number` |  |
| `allow_merge_commit` | `boolean` |  |
| `downloads_url` | `string` |  |
| `permissions` | `object` |  |
| `allow_squash_merge` | `boolean` |  |
| `blobs_url` | `string` |  |
| `pushed_at` | `string` |  |
| `git_refs_url` | `string` |  |
| `master_branch` | `string` |  |
| `forks_count` | `integer` |  |
| `size` | `integer` |  |
| `branches_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `trees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `license` | `object` | License Simple |
| `subscribers_url` | `string` |  |
| `labels_url` | `string` |  |
| `forks` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `archived` | `boolean` |  |
| `releases_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `languages_url` | `string` |  |
| `issues_url` | `string` |  |
| `hooks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `homepage` | `string` |  |
| `events_url` | `string` |  |
| `private` | `boolean` |  |
| `allow_auto_merge` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `git_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `updated_at` | `string` |  |
| `mirror_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `default_branch` | `string` |  |
| `watchers` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `tags_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `contributors_url` | `string` |  |
| `ssh_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `archive_url` | `string` |  |
| `deployments_url` | `string` |  |
| `clone_url` | `string` |  |
| `assignees_url` | `string` |  |
| `topics` | `array` |  |
| `statuses_url` | `string` |  |
| `svn_url` | `string` |  |
| `text_matches` | `array` |  |
| `watchers_count` | `integer` |  |
| `language` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `milestones_url` | `string` |  |
| `notifications_url` | `string` |  |
| `fork` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `subscription_url` | `string` |  |
| `merges_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `comments_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `compare_url` | `string` |  |
| `open_issues` | `integer` |  |
| `contents_url` | `string` |  |
| `keys_url` | `string` |  |
| `commits_url` | `string` |  |
| `has_discussions` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `repos` | `SELECT` | `q` |
