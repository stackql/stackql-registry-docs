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
| `merges_url` | `string` |  |
| `language` | `string` |  |
| `created_at` | `string` |  |
| `forks_count` | `integer` |  |
| `clone_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `is_template` | `boolean` |  |
| `has_discussions` | `boolean` |  |
| `statuses_url` | `string` |  |
| `labels_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `milestones_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `forks` | `integer` |  |
| `disabled` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `branches_url` | `string` |  |
| `compare_url` | `string` |  |
| `default_branch` | `string` |  |
| `releases_url` | `string` |  |
| `updated_at` | `string` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `web_commit_signoff_required` | `boolean` |  |
| `languages_url` | `string` |  |
| `watchers` | `integer` |  |
| `visibility` | `string` |  |
| `has_wiki` | `boolean` |  |
| `subscription_url` | `string` |  |
| `pulls_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `private` | `boolean` |  |
| `teams_url` | `string` |  |
| `role_name` | `string` |  |
| `has_downloads` | `boolean` |  |
| `full_name` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `downloads_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `contributors_url` | `string` |  |
| `archive_url` | `string` |  |
| `open_issues` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `fork` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `deployments_url` | `string` |  |
| `comments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `assignees_url` | `string` |  |
| `mirror_url` | `string` |  |
| `license` | `object` |  |
| `issue_comment_url` | `string` |  |
| `trees_url` | `string` |  |
| `commits_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `events_url` | `string` |  |
| `ssh_url` | `string` |  |
| `homepage` | `string` |  |
| `svn_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `archived` | `boolean` |  |
| `blobs_url` | `string` |  |
| `contents_url` | `string` |  |
| `issues_url` | `string` |  |
| `git_url` | `string` |  |
| `tags_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `permissions` | `object` |  |
| `pushed_at` | `string` |  |
| `url` | `string` |  |
| `topics` | `array` |  |
| `network_count` | `integer` |  |
| `security_and_analysis` | `object` |  |
| `keys_url` | `string` |  |
| `hooks_url` | `string` |  |
| `forks_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_org` | `SELECT` | `org` | Lists repositories for the specified organization.<br /><br />**Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| `list_for_user` | `SELECT` | `username` | Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user. |
| `list_public` | `SELECT` |  | Lists all public repositories in the order that they were created.<br /><br />Note:<br />- For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise.<br />- Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of repositories. |
| `create_in_org` | `INSERT` | `org, data__name` | Creates a new repository in the specified organization. The authenticated user must be a member of the organization.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| `delete` | `DELETE` | `owner, repo` | Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.<br /><br />If an organization owner has configured the organization to prevent members from deleting organization-owned<br />repositories, you will get a `403 Forbidden` response. |
| `check_vulnerability_alerts` | `EXEC` | `owner, repo` | Shows whether dependency alerts are enabled or disabled for a repository. The authenticated user must have admin read access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)". |
| `codeowners_errors` | `EXEC` | `owner, repo` | List any syntax errors that are detected in the CODEOWNERS<br />file.<br /><br />For more information about the correct CODEOWNERS syntax,<br />see "[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)." |
| `create_dispatch_event` | `EXEC` | `owner, repo, data__event_type` | You can use this endpoint to trigger a webhook event called `repository_dispatch` when you want activity that happens outside of GitHub to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the `repository_dispatch` event occurs. For an example `repository_dispatch` webhook payload, see "[RepositoryDispatchEvent](https://docs.github.com/webhooks/event-payloads/#repository_dispatch)."<br /><br />The `client_payload` parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the `client_payload` can include a message that a user would like to send using a GitHub Actions workflow. Or the `client_payload` can be used as a test to debug your workflow.<br /><br />This endpoint requires write access to the repository by providing either:<br /><br />  - Personal access tokens with `repo` scope. For more information, see "[Creating a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line)" in the GitHub Help documentation.<br />  - GitHub Apps with both `metadata:read` and `contents:read&write` permissions.<br /><br />This input example shows how you can use the `client_payload` as a test to debug your workflow. |
| `create_using_template` | `EXEC` | `template_owner, template_repo, data__name` | Creates a new repository using a repository template. Use the `template_owner` and `template_repo` route parameters to specify the repository to use as the template. If the repository is not public, the authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository's information using the [Get a repository](https://docs.github.com/rest/repos/repos#get-a-repository) endpoint and check that the `is_template` key is `true`.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| `disable_private_vulnerability_reporting` | `EXEC` | `owner, repo` | Disables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)". |
| `disable_vulnerability_alerts` | `EXEC` | `owner, repo` | Disables dependency alerts and the dependency graph for a repository.<br />The authenticated user must have admin access to the repository. For more information,<br />see "[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)". |
| `enable_private_vulnerability_reporting` | `EXEC` | `owner, repo` | Enables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)." |
| `enable_vulnerability_alerts` | `EXEC` | `owner, repo` | Enables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)". |
| `list_languages` | `EXEC` | `owner, repo` | Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language. |
| `transfer` | `EXEC` | `owner, repo, data__new_owner` | A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original `owner`, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).<br />You must use a personal access token (classic) or an OAuth token for this endpoint. An installation access token or a fine-grained personal access token cannot be used because they are only granted access to a single account. |
| `update` | `EXEC` | `owner, repo` | **Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) endpoint. |
