---
title: starred_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - starred_repos
  - activity
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
<tr><td><b>Name</b></td><td><code>starred_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.starred_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `network_count` | `integer` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `master_branch` | `string` |  |
| `organization` | `object` | Simple User |
| `comments_url` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `node_id` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `open_issues` | `integer` |  |
| `deployments_url` | `string` |  |
| `forks` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `subscription_url` | `string` |  |
| `contributors_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `assignees_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `language` | `string` |  |
| `blobs_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `license` | `object` | License Simple |
| `subscribers_url` | `string` |  |
| `fork` | `boolean` |  |
| `topics` | `array` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `owner` | `object` | Simple User |
| `stargazers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `notifications_url` | `string` |  |
| `events_url` | `string` |  |
| `git_url` | `string` |  |
| `permissions` | `object` |  |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `size` | `integer` |  |
| `pushed_at` | `string` |  |
| `teams_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `forks_count` | `integer` |  |
| `clone_url` | `string` |  |
| `keys_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `private` | `boolean` | Whether the repository is private or public. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `issues_url` | `string` |  |
| `svn_url` | `string` |  |
| `contents_url` | `string` |  |
| `compare_url` | `string` |  |
| `created_at` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `html_url` | `string` |  |
| `hooks_url` | `string` |  |
| `labels_url` | `string` |  |
| `ssh_url` | `string` |  |
| `milestones_url` | `string` |  |
| `branches_url` | `string` |  |
| `template_repository` | `object` |  |
| `releases_url` | `string` |  |
| `trees_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `archive_url` | `string` |  |
| `forks_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `git_commits_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `starred_at` | `string` |  |
| `statuses_url` | `string` |  |
| `languages_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `downloads_url` | `string` |  |
| `commits_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `homepage` | `string` |  |
| `has_pages` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `full_name` | `string` |  |
| `issue_events_url` | `string` |  |
| `pulls_url` | `string` |  |
| `merges_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `watchers` | `integer` |  |
| `temp_clone_token` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
