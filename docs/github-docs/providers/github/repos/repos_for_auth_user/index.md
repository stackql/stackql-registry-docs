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
| `releases_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `contributors_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `stargazers_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `html_url` | `string` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `updated_at` | `string` |  |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is enabled for this repository |
| `git_tags_url` | `string` |  |
| `starred_at` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `owner` | `object` | A GitHub user. |
| `web_commit_signoff_required` | `boolean` | Whether to require contributors to sign off on web-based commits |
| `topics` | `array` |  |
| `languages_url` | `string` |  |
| `contents_url` | `string` |  |
| `homepage` | `string` |  |
| `pushed_at` | `string` |  |
| `tags_url` | `string` |  |
| `watchers` | `integer` |  |
| `archive_url` | `string` |  |
| `assignees_url` | `string` |  |
| `fork` | `boolean` |  |
| `permissions` | `object` |  |
| `clone_url` | `string` |  |
| `language` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `organization` | `object` | A GitHub user. |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `forks_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `archived` | `boolean` | Whether the repository is archived. |
| `private` | `boolean` | Whether the repository is private or public. |
| `template_repository` | `object` |  |
| `downloads_url` | `string` |  |
| `url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `svn_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `blobs_url` | `string` |  |
| `issues_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `branches_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `license` | `object` | License Simple |
| `has_discussions` | `boolean` | Whether discussions are enabled. |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `pulls_url` | `string` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `forks_count` | `integer` |  |
| `allow_update_branch` | `boolean` | Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging. |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `git_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `teams_url` | `string` |  |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `trees_url` | `string` |  |
| `keys_url` | `string` |  |
| `full_name` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `subscription_url` | `string` |  |
| `comments_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `forks` | `integer` |  |
| `subscribers_url` | `string` |  |
| `network_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `commits_url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `master_branch` | `string` |  |
| `created_at` | `string` |  |
| `merges_url` | `string` |  |
| `ssh_url` | `string` |  |
| `node_id` | `string` |  |
| `labels_url` | `string` |  |
| `mirror_url` | `string` |  |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `hooks_url` | `string` |  |
| `notifications_url` | `string` |  |
| `use_squash_pr_title_as_default` | `boolean` | Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead. |
| `events_url` | `string` |  |
| `deployments_url` | `string` |  |
| `compare_url` | `string` |  |
| `milestones_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `watchers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_authenticated_user` | `SELECT` |  | Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership. |
| `create_for_authenticated_user` | `INSERT` | `data__name` | Creates a new repository for the authenticated user.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository. |
