---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - repos
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `tags_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `open_issues_count` | `integer` |  |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is enabled for this repository |
| `git_tags_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `homepage` | `string` |  |
| `fork` | `boolean` |  |
| `hooks_url` | `string` |  |
| `open_issues` | `integer` |  |
| `has_discussions` | `boolean` | Whether discussions are enabled. |
| `default_branch` | `string` | The default branch of the repository. |
| `forks` | `integer` |  |
| `stargazers_url` | `string` |  |
| `topics` | `array` |  |
| `watchers_count` | `integer` |  |
| `downloads_url` | `string` |  |
| `subscription_url` | `string` |  |
| `pulls_url` | `string` |  |
| `comments_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `full_name` | `string` |  |
| `starred_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `network_count` | `integer` |  |
| `keys_url` | `string` |  |
| `master_branch` | `string` |  |
| `created_at` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `languages_url` | `string` |  |
| `milestones_url` | `string` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `teams_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `git_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `merges_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `trees_url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `compare_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `assignees_url` | `string` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `contributors_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `license` | `object` | License Simple |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `branches_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `temp_clone_token` | `string` |  |
| `language` | `string` |  |
| `web_commit_signoff_required` | `boolean` | Whether to require contributors to sign off on web-based commits |
| `svn_url` | `string` |  |
| `mirror_url` | `string` |  |
| `issues_url` | `string` |  |
| `html_url` | `string` |  |
| `blobs_url` | `string` |  |
| `archive_url` | `string` |  |
| `statuses_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `commits_url` | `string` |  |
| `template_repository` | `object` |  |
| `stargazers_count` | `integer` |  |
| `issue_events_url` | `string` |  |
| `permissions` | `object` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `notifications_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `events_url` | `string` |  |
| `node_id` | `string` |  |
| `clone_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `pushed_at` | `string` |  |
| `updated_at` | `string` |  |
| `allow_update_branch` | `boolean` | Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging. |
| `use_squash_pr_title_as_default` | `boolean` | Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead. |
| `forks_count` | `integer` |  |
| `url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `releases_url` | `string` |  |
| `labels_url` | `string` |  |
| `ssh_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `organization` | `object` | A GitHub user. |
| `watchers` | `integer` |  |
| `deployments_url` | `string` |  |
| `contents_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `git_commits_url` | `string` |  |
| `forks_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_authenticated_user` | `SELECT` |  | Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership. |
| `create_for_authenticated_user` | `INSERT` | `data__name` | Creates a new repository for the authenticated user.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository. |
