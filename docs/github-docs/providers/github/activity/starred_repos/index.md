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
| `pulls_url` | `string` |  |
| `topics` | `array` |  |
| `has_pages` | `boolean` |  |
| `branches_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `clone_url` | `string` |  |
| `keys_url` | `string` |  |
| `mirror_url` | `string` |  |
| `trees_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `full_name` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `merges_url` | `string` |  |
| `notifications_url` | `string` |  |
| `forks_count` | `integer` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `node_id` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `contributors_url` | `string` |  |
| `comments_url` | `string` |  |
| `updated_at` | `string` |  |
| `git_refs_url` | `string` |  |
| `homepage` | `string` |  |
| `assignees_url` | `string` |  |
| `languages_url` | `string` |  |
| `network_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `starred_at` | `string` |  |
| `subscription_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `ssh_url` | `string` |  |
| `archive_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `watchers_count` | `integer` |  |
| `license` | `object` | License Simple |
| `issue_comment_url` | `string` |  |
| `labels_url` | `string` |  |
| `tags_url` | `string` |  |
| `hooks_url` | `string` |  |
| `downloads_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `issue_events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `collaborators_url` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `milestones_url` | `string` |  |
| `fork` | `boolean` |  |
| `organization` | `object` | Simple User |
| `owner` | `object` | Simple User |
| `permissions` | `object` |  |
| `statuses_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `language` | `string` |  |
| `compare_url` | `string` |  |
| `deployments_url` | `string` |  |
| `issues_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `template_repository` | `object` |  |
| `svn_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `pushed_at` | `string` |  |
| `events_url` | `string` |  |
| `created_at` | `string` |  |
| `subscribers_count` | `integer` |  |
| `commits_url` | `string` |  |
| `teams_url` | `string` |  |
| `forks` | `integer` |  |
| `forks_url` | `string` |  |
| `blobs_url` | `string` |  |
| `open_issues` | `integer` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `releases_url` | `string` |  |
| `size` | `integer` |  |
| `master_branch` | `string` |  |
| `contents_url` | `string` |  |
| `git_url` | `string` |  |
| `watchers` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
