---
title: user_starred
hide_title: false
hide_table_of_contents: false
keywords:
  - user_starred
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
<tr><td><b>Name</b></td><td><code>user_starred</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.user_starred</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `permissions` | `object` |  |
| `blobs_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `issue_events_url` | `string` |  |
| `compare_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_discussions` | `boolean` | Whether discussions are enabled. |
| `deployments_url` | `string` |  |
| `fork` | `boolean` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `merges_url` | `string` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `git_refs_url` | `string` |  |
| `forks_count` | `integer` |  |
| `use_squash_pr_title_as_default` | `boolean` | Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead. |
| `stargazers_count` | `integer` |  |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `branches_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `allow_update_branch` | `boolean` | Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging. |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `license` | `object` | License Simple |
| `releases_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `git_url` | `string` |  |
| `homepage` | `string` |  |
| `full_name` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `hooks_url` | `string` |  |
| `watchers` | `integer` |  |
| `clone_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `downloads_url` | `string` |  |
| `node_id` | `string` |  |
| `subscription_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `web_commit_signoff_required` | `boolean` | Whether to require contributors to sign off on web-based commits |
| `git_commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `html_url` | `string` |  |
| `pulls_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `pushed_at` | `string` |  |
| `issues_url` | `string` |  |
| `organization` | `object` | A GitHub user. |
| `forks` | `integer` |  |
| `created_at` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `ssh_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `keys_url` | `string` |  |
| `contents_url` | `string` |  |
| `statuses_url` | `string` |  |
| `archive_url` | `string` |  |
| `template_repository` | `object` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `teams_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `commits_url` | `string` |  |
| `mirror_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `events_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `network_count` | `integer` |  |
| `topics` | `array` |  |
| `svn_url` | `string` |  |
| `labels_url` | `string` |  |
| `starred_at` | `string` |  |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is enabled for this repository |
| `archived` | `boolean` | Whether the repository is archived. |
| `milestones_url` | `string` |  |
| `language` | `string` |  |
| `trees_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `assignees_url` | `string` |  |
| `tags_url` | `string` |  |
| `forks_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `languages_url` | `string` |  |
| `contributors_url` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `watchers_count` | `integer` |  |
| `master_branch` | `string` |  |
| `subscribers_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `updated_at` | `string` |  |
| `comments_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_starred_by_authenticated_user` | `SELECT` |  | Lists repositories the authenticated user has starred.<br /><br />You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: `application/vnd.github.star+json`. |
| `check_repo_is_starred_by_authenticated_user` | `EXEC` | `owner, repo` | Whether the authenticated user has starred the repository. |
| `star_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Unstar a repository that the authenticated user has previously starred. |
