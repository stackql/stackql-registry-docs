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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.repos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="allow_forking" /> | `boolean` |  |
| <CopyableCode code="archive_url" /> | `string` |  |
| <CopyableCode code="archived" /> | `boolean` |  |
| <CopyableCode code="assignees_url" /> | `string` |  |
| <CopyableCode code="blobs_url" /> | `string` |  |
| <CopyableCode code="branches_url" /> | `string` |  |
| <CopyableCode code="clone_url" /> | `string` |  |
| <CopyableCode code="code_of_conduct" /> | `object` | Code Of Conduct |
| <CopyableCode code="collaborators_url" /> | `string` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commits_url" /> | `string` |  |
| <CopyableCode code="compare_url" /> | `string` |  |
| <CopyableCode code="contents_url" /> | `string` |  |
| <CopyableCode code="contributors_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="default_branch" /> | `string` |  |
| <CopyableCode code="delete_branch_on_merge" /> | `boolean` |  |
| <CopyableCode code="deployments_url" /> | `string` |  |
| <CopyableCode code="disabled" /> | `boolean` |  |
| <CopyableCode code="downloads_url" /> | `string` |  |
| <CopyableCode code="events_url" /> | `string` |  |
| <CopyableCode code="fork" /> | `boolean` |  |
| <CopyableCode code="forks" /> | `integer` |  |
| <CopyableCode code="forks_count" /> | `integer` |  |
| <CopyableCode code="forks_url" /> | `string` |  |
| <CopyableCode code="full_name" /> | `string` |  |
| <CopyableCode code="git_commits_url" /> | `string` |  |
| <CopyableCode code="git_refs_url" /> | `string` |  |
| <CopyableCode code="git_tags_url" /> | `string` |  |
| <CopyableCode code="git_url" /> | `string` |  |
| <CopyableCode code="has_discussions" /> | `boolean` |  |
| <CopyableCode code="has_downloads" /> | `boolean` |  |
| <CopyableCode code="has_issues" /> | `boolean` |  |
| <CopyableCode code="has_pages" /> | `boolean` |  |
| <CopyableCode code="has_projects" /> | `boolean` |  |
| <CopyableCode code="has_wiki" /> | `boolean` |  |
| <CopyableCode code="homepage" /> | `string` |  |
| <CopyableCode code="hooks_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="is_template" /> | `boolean` |  |
| <CopyableCode code="issue_comment_url" /> | `string` |  |
| <CopyableCode code="issue_events_url" /> | `string` |  |
| <CopyableCode code="issues_url" /> | `string` |  |
| <CopyableCode code="keys_url" /> | `string` |  |
| <CopyableCode code="labels_url" /> | `string` |  |
| <CopyableCode code="language" /> | `string` |  |
| <CopyableCode code="languages_url" /> | `string` |  |
| <CopyableCode code="license" /> | `object` |  |
| <CopyableCode code="merges_url" /> | `string` |  |
| <CopyableCode code="milestones_url" /> | `string` |  |
| <CopyableCode code="mirror_url" /> | `string` |  |
| <CopyableCode code="network_count" /> | `integer` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notifications_url" /> | `string` |  |
| <CopyableCode code="open_issues" /> | `integer` |  |
| <CopyableCode code="open_issues_count" /> | `integer` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="private" /> | `boolean` |  |
| <CopyableCode code="pulls_url" /> | `string` |  |
| <CopyableCode code="pushed_at" /> | `string` |  |
| <CopyableCode code="releases_url" /> | `string` |  |
| <CopyableCode code="role_name" /> | `string` |  |
| <CopyableCode code="security_and_analysis" /> | `object` |  |
| <CopyableCode code="size" /> | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| <CopyableCode code="ssh_url" /> | `string` |  |
| <CopyableCode code="stargazers_count" /> | `integer` |  |
| <CopyableCode code="stargazers_url" /> | `string` |  |
| <CopyableCode code="statuses_url" /> | `string` |  |
| <CopyableCode code="subscribers_count" /> | `integer` |  |
| <CopyableCode code="subscribers_url" /> | `string` |  |
| <CopyableCode code="subscription_url" /> | `string` |  |
| <CopyableCode code="svn_url" /> | `string` |  |
| <CopyableCode code="tags_url" /> | `string` |  |
| <CopyableCode code="teams_url" /> | `string` |  |
| <CopyableCode code="temp_clone_token" /> | `string` |  |
| <CopyableCode code="topics" /> | `array` |  |
| <CopyableCode code="trees_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="visibility" /> | `string` |  |
| <CopyableCode code="watchers" /> | `integer` |  |
| <CopyableCode code="watchers_count" /> | `integer` |  |
| <CopyableCode code="web_commit_signoff_required" /> | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_for_org" /> | `SELECT` | <CopyableCode code="org" /> | Lists repositories for the specified organization.<br /><br />**Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| <CopyableCode code="list_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user. |
| <CopyableCode code="list_public" /> | `SELECT` |  | Lists all public repositories in the order that they were created.<br /><br />Note:<br />- For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise.<br />- Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of repositories. |
| <CopyableCode code="create_in_org" /> | `INSERT` | <CopyableCode code="org, data__name" /> | Creates a new repository in the specified organization. The authenticated user must be a member of the organization.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="owner, repo" /> | Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.<br /><br />If an organization owner has configured the organization to prevent members from deleting organization-owned<br />repositories, you will get a `403 Forbidden` response. |
| <CopyableCode code="check_vulnerability_alerts" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Shows whether dependency alerts are enabled or disabled for a repository. The authenticated user must have admin read access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)". |
| <CopyableCode code="codeowners_errors" /> | `EXEC` | <CopyableCode code="owner, repo" /> | List any syntax errors that are detected in the CODEOWNERS<br />file.<br /><br />For more information about the correct CODEOWNERS syntax,<br />see "[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)." |
| <CopyableCode code="create_dispatch_event" /> | `EXEC` | <CopyableCode code="owner, repo, data__event_type" /> | You can use this endpoint to trigger a webhook event called `repository_dispatch` when you want activity that happens outside of GitHub to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the `repository_dispatch` event occurs. For an example `repository_dispatch` webhook payload, see "[RepositoryDispatchEvent](https://docs.github.com/webhooks/event-payloads/#repository_dispatch)."<br /><br />The `client_payload` parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the `client_payload` can include a message that a user would like to send using a GitHub Actions workflow. Or the `client_payload` can be used as a test to debug your workflow.<br /><br />This endpoint requires write access to the repository by providing either:<br /><br />  - Personal access tokens with `repo` scope. For more information, see "[Creating a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line)" in the GitHub Help documentation.<br />  - GitHub Apps with both `metadata:read` and `contents:read&write` permissions.<br /><br />This input example shows how you can use the `client_payload` as a test to debug your workflow. |
| <CopyableCode code="create_using_template" /> | `EXEC` | <CopyableCode code="template_owner, template_repo, data__name" /> | Creates a new repository using a repository template. Use the `template_owner` and `template_repo` route parameters to specify the repository to use as the template. If the repository is not public, the authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository's information using the [Get a repository](https://docs.github.com/rest/repos/repos#get-a-repository) endpoint and check that the `is_template` key is `true`.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| <CopyableCode code="disable_private_vulnerability_reporting" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Disables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)". |
| <CopyableCode code="disable_vulnerability_alerts" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Disables dependency alerts and the dependency graph for a repository.<br />The authenticated user must have admin access to the repository. For more information,<br />see "[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)". |
| <CopyableCode code="enable_private_vulnerability_reporting" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Enables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)." |
| <CopyableCode code="enable_vulnerability_alerts" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Enables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/articles/about-security-alerts-for-vulnerable-dependencies)". |
| <CopyableCode code="list_languages" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language. |
| <CopyableCode code="transfer" /> | `EXEC` | <CopyableCode code="owner, repo, data__new_owner" /> | A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original `owner`, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).<br />You must use a personal access token (classic) or an OAuth token for this endpoint. An installation access token or a fine-grained personal access token cannot be used because they are only granted access to a single account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="owner, repo" /> | **Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) endpoint. |
