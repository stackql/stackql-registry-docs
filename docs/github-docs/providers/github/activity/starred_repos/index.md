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
| `size` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `html_url` | `string` |  |
| `subscription_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `issues_url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `notifications_url` | `string` |  |
| `fork` | `boolean` |  |
| `blobs_url` | `string` |  |
| `full_name` | `string` |  |
| `compare_url` | `string` |  |
| `ssh_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `url` | `string` |  |
| `stargazers_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `statuses_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `merges_url` | `string` |  |
| `commits_url` | `string` |  |
| `license` | `object` | License Simple |
| `network_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `deployments_url` | `string` |  |
| `git_url` | `string` |  |
| `languages_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `git_refs_url` | `string` |  |
| `trees_url` | `string` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `keys_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `language` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `archive_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `releases_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `created_at` | `string` |  |
| `svn_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `permissions` | `object` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `node_id` | `string` |  |
| `milestones_url` | `string` |  |
| `owner` | `object` | Simple User |
| `contributors_url` | `string` |  |
| `pushed_at` | `string` |  |
| `hooks_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `clone_url` | `string` |  |
| `template_repository` | `object` |  |
| `updated_at` | `string` |  |
| `organization` | `object` | Simple User |
| `watchers` | `integer` |  |
| `mirror_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `topics` | `array` |  |
| `watchers_count` | `integer` |  |
| `teams_url` | `string` |  |
| `open_issues` | `integer` |  |
| `forks_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `private` | `boolean` | Whether the repository is private or public. |
| `assignees_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `forks` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `downloads_url` | `string` |  |
| `homepage` | `string` |  |
| `contents_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `starred_at` | `string` |  |
| `branches_url` | `string` |  |
| `pulls_url` | `string` |  |
| `master_branch` | `string` |  |
| `open_issues_count` | `integer` |  |
| `labels_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
