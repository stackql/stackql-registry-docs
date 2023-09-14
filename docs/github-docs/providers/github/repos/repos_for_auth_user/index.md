---
title: repos_for_auth_user
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_for_auth_user
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
<tr><td><b>Name</b></td><td><code>repos_for_auth_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.repos_for_auth_user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `tags_url` | `string` |  |
| `subscription_url` | `string` |  |
| `html_url` | `string` |  |
| `trees_url` | `string` |  |
| `homepage` | `string` |  |
| `forks` | `integer` |  |
| `compare_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `clone_url` | `string` |  |
| `license` | `object` | License Simple |
| `organization` | `object` | A GitHub user. |
| `pulls_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `milestones_url` | `string` |  |
| `updated_at` | `string` |  |
| `comments_url` | `string` |  |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is enabled for this repository |
| `issue_events_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `created_at` | `string` |  |
| `has_pages` | `boolean` |  |
| `keys_url` | `string` |  |
| `full_name` | `string` |  |
| `topics` | `array` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `pushed_at` | `string` |  |
| `temp_clone_token` | `string` |  |
| `contents_url` | `string` |  |
| `merges_url` | `string` |  |
| `issues_url` | `string` |  |
| `statuses_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `assignees_url` | `string` |  |
| `node_id` | `string` |  |
| `network_count` | `integer` |  |
| `owner` | `object` | A GitHub user. |
| `fork` | `boolean` |  |
| `blobs_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `forks_url` | `string` |  |
| `allow_update_branch` | `boolean` | Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging. |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `language` | `string` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `git_commits_url` | `string` |  |
| `hooks_url` | `string` |  |
| `url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `use_squash_pr_title_as_default` | `boolean` | Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead. |
| `issue_comment_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `archive_url` | `string` |  |
| `teams_url` | `string` |  |
| `ssh_url` | `string` |  |
| `commits_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `notifications_url` | `string` |  |
| `events_url` | `string` |  |
| `has_discussions` | `boolean` | Whether discussions are enabled. |
| `deployments_url` | `string` |  |
| `permissions` | `object` |  |
| `git_url` | `string` |  |
| `svn_url` | `string` |  |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `languages_url` | `string` |  |
| `releases_url` | `string` |  |
| `watchers` | `integer` |  |
| `labels_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `template_repository` | `object` |  |
| `mirror_url` | `string` |  |
| `contributors_url` | `string` |  |
| `branches_url` | `string` |  |
| `master_branch` | `string` |  |
| `git_refs_url` | `string` |  |
| `open_issues` | `integer` |  |
| `stargazers_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `subscribers_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` | Whether to require contributors to sign off on web-based commits |
| `starred_at` | `string` |  |
| `downloads_url` | `string` |  |
| `forks_count` | `integer` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `watchers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_authenticated_user` | `SELECT` |  | Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership. |
| `create_for_authenticated_user` | `INSERT` | `data__name` | Creates a new repository for the authenticated user.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository. |
