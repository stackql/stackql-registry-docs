---
title: public_repos
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
| `issue_events_url` | `string` |  |
| `watchers` | `integer` |  |
| `full_name` | `string` |  |
| `statuses_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `assignees_url` | `string` |  |
| `language` | `string` |  |
| `languages_url` | `string` |  |
| `size` | `integer` |  |
| `node_id` | `string` |  |
| `downloads_url` | `string` |  |
| `owner` | `object` | Simple User |
| `topics` | `array` |  |
| `subscription_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `keys_url` | `string` |  |
| `compare_url` | `string` |  |
| `license` | `object` |  |
| `branches_url` | `string` |  |
| `contents_url` | `string` |  |
| `labels_url` | `string` |  |
| `comments_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `trees_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `pulls_url` | `string` |  |
| `milestones_url` | `string` |  |
| `archived` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `notifications_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `forks_count` | `integer` |  |
| `visibility` | `string` |  |
| `blobs_url` | `string` |  |
| `clone_url` | `string` |  |
| `private` | `boolean` |  |
| `merges_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `issues_url` | `string` |  |
| `network_count` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `created_at` | `string` |  |
| `ssh_url` | `string` |  |
| `teams_url` | `string` |  |
| `fork` | `boolean` |  |
| `updated_at` | `string` |  |
| `contributors_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `git_commits_url` | `string` |  |
| `html_url` | `string` |  |
| `open_issues` | `integer` |  |
| `default_branch` | `string` |  |
| `archive_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `disabled` | `boolean` |  |
| `releases_url` | `string` |  |
| `svn_url` | `string` |  |
| `hooks_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `forks_url` | `string` |  |
| `mirror_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `git_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `homepage` | `string` |  |
| `url` | `string` |  |
| `role_name` | `string` |  |
| `permissions` | `object` |  |
| `has_downloads` | `boolean` |  |
| `pushed_at` | `string` |  |
| `forks` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
