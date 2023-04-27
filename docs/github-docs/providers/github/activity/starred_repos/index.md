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
| `has_projects` | `boolean` | Whether projects are enabled. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `statuses_url` | `string` |  |
| `clone_url` | `string` |  |
| `downloads_url` | `string` |  |
| `template_repository` | `object` |  |
| `releases_url` | `string` |  |
| `git_url` | `string` |  |
| `organization` | `object` | Simple User |
| `permissions` | `object` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `forks_count` | `integer` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `git_commits_url` | `string` |  |
| `issues_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `forks_url` | `string` |  |
| `contributors_url` | `string` |  |
| `created_at` | `string` |  |
| `watchers_count` | `integer` |  |
| `full_name` | `string` |  |
| `contents_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `deployments_url` | `string` |  |
| `forks` | `integer` |  |
| `subscription_url` | `string` |  |
| `master_branch` | `string` |  |
| `network_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `events_url` | `string` |  |
| `keys_url` | `string` |  |
| `topics` | `array` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `archive_url` | `string` |  |
| `license` | `object` | License Simple |
| `labels_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `open_issues_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `fork` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `mirror_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `comments_url` | `string` |  |
| `trees_url` | `string` |  |
| `branches_url` | `string` |  |
| `teams_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `html_url` | `string` |  |
| `commits_url` | `string` |  |
| `languages_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `svn_url` | `string` |  |
| `pulls_url` | `string` |  |
| `size` | `integer` |  |
| `compare_url` | `string` |  |
| `node_id` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `url` | `string` |  |
| `language` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `starred_at` | `string` |  |
| `assignees_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `git_refs_url` | `string` |  |
| `owner` | `object` | Simple User |
| `blobs_url` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `subscribers_url` | `string` |  |
| `watchers` | `integer` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `milestones_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `updated_at` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `ssh_url` | `string` |  |
| `homepage` | `string` |  |
| `pushed_at` | `string` |  |
| `notifications_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `merges_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `issue_events_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
