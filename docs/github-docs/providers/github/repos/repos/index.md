---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `is_template` | `boolean` |  |
| `has_discussions` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `homepage` | `string` |  |
| `watchers_count` | `integer` |  |
| `updated_at` | `string` |  |
| `subscription_url` | `string` |  |
| `comments_url` | `string` |  |
| `deployments_url` | `string` |  |
| `blobs_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `git_refs_url` | `string` |  |
| `commits_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `pushed_at` | `string` |  |
| `html_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `open_issues` | `integer` |  |
| `security_and_analysis` | `object` |  |
| `clone_url` | `string` |  |
| `disabled` | `boolean` |  |
| `ssh_url` | `string` |  |
| `downloads_url` | `string` |  |
| `events_url` | `string` |  |
| `contributors_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `git_tags_url` | `string` |  |
| `compare_url` | `string` |  |
| `forks_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `releases_url` | `string` |  |
| `languages_url` | `string` |  |
| `pulls_url` | `string` |  |
| `visibility` | `string` |  |
| `tags_url` | `string` |  |
| `hooks_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `topics` | `array` |  |
| `forks` | `integer` |  |
| `branches_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `node_id` | `string` |  |
| `statuses_url` | `string` |  |
| `role_name` | `string` |  |
| `archive_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `trees_url` | `string` |  |
| `issues_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `private` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `svn_url` | `string` |  |
| `fork` | `boolean` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `default_branch` | `string` |  |
| `merges_url` | `string` |  |
| `url` | `string` |  |
| `keys_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `teams_url` | `string` |  |
| `contents_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `watchers` | `integer` |  |
| `created_at` | `string` |  |
| `mirror_url` | `string` |  |
| `milestones_url` | `string` |  |
| `forks_url` | `string` |  |
| `permissions` | `object` |  |
| `notifications_url` | `string` |  |
| `network_count` | `integer` |  |
| `full_name` | `string` |  |
| `language` | `string` |  |
| `stargazers_url` | `string` |  |
| `labels_url` | `string` |  |
| `archived` | `boolean` |  |
| `git_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `assignees_url` | `string` |  |
| `license` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_org` | `SELECT` | `org` | Lists repositories for the specified organization.<br /><br />**Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| `list_for_user` | `SELECT` | `username` | Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user. |
| `list_public` | `SELECT` |  | Lists all public repositories in the order that they were created.<br /><br />Note:<br />- For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise.<br />- Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of repositories. |
| `create_in_org` | `INSERT` | `org, data__name` | Creates a new repository in the specified organization. The authenticated user must be a member of the organization.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| `delete` | `DELETE` | `owner, repo` | Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.<br /><br />If an organization owner has configured the organization to prevent members from deleting organization-owned<br />repositories, you will get a `403 Forbidden` response. |
| `codeowners_errors` | `EXEC` | `owner, repo` | List any syntax errors that are detected in the CODEOWNERS<br />file.<br /><br />For more information about the correct CODEOWNERS syntax,<br />see "[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)." |
| `list_languages` | `EXEC` | `owner, repo` | Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language. |
| `transfer` | `EXEC` | `owner, repo, data__new_owner` | A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original `owner`, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).<br />You must use a personal access token (classic) or an OAuth token for this endpoint. An installation access token or a fine-grained personal access token cannot be used because they are only granted access to a single account. |
| `update` | `EXEC` | `owner, repo` | **Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) endpoint. |
