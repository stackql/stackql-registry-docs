---
title: starred_repos
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
| `watchers_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `branches_url` | `string` |  |
| `mirror_url` | `string` |  |
| `contents_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `subscribers_count` | `integer` |  |
| `labels_url` | `string` |  |
| `merges_url` | `string` |  |
| `pulls_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `issues_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `organization` | `object` | Simple User |
| `network_count` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `git_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `clone_url` | `string` |  |
| `forks` | `integer` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `downloads_url` | `string` |  |
| `trees_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `releases_url` | `string` |  |
| `archive_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `updated_at` | `string` |  |
| `keys_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `events_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `has_pages` | `boolean` |  |
| `full_name` | `string` |  |
| `subscribers_url` | `string` |  |
| `starred_at` | `string` |  |
| `template_repository` | `object` |  |
| `ssh_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `created_at` | `string` |  |
| `statuses_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `commits_url` | `string` |  |
| `fork` | `boolean` |  |
| `html_url` | `string` |  |
| `milestones_url` | `string` |  |
| `subscription_url` | `string` |  |
| `contributors_url` | `string` |  |
| `owner` | `object` | Simple User |
| `permissions` | `object` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `issue_comment_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `tags_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `language` | `string` |  |
| `blobs_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `comments_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `license` | `object` | License Simple |
| `notifications_url` | `string` |  |
| `url` | `string` |  |
| `open_issues` | `integer` |  |
| `pushed_at` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `homepage` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `size` | `integer` |  |
| `master_branch` | `string` |  |
| `assignees_url` | `string` |  |
| `deployments_url` | `string` |  |
| `forks_count` | `integer` |  |
| `teams_url` | `string` |  |
| `svn_url` | `string` |  |
| `watchers` | `integer` |  |
| `topics` | `array` |  |
| `git_refs_url` | `string` |  |
| `languages_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` |  |
| `list_repos_starred_by_user` | `EXEC` | `username` | Lists repositories a user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` |  |
