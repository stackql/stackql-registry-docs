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
| `license` | `object` |  |
| `notifications_url` | `string` |  |
| `hooks_url` | `string` |  |
| `visibility` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `statuses_url` | `string` |  |
| `fork` | `boolean` |  |
| `merges_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `created_at` | `string` |  |
| `deployments_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `compare_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `teams_url` | `string` |  |
| `assignees_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `node_id` | `string` |  |
| `subscribers_count` | `integer` |  |
| `has_downloads` | `boolean` |  |
| `labels_url` | `string` |  |
| `trees_url` | `string` |  |
| `archived` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `language` | `string` |  |
| `blobs_url` | `string` |  |
| `downloads_url` | `string` |  |
| `ssh_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `issues_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `git_url` | `string` |  |
| `forks_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `html_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `events_url` | `string` |  |
| `watchers` | `integer` |  |
| `commits_url` | `string` |  |
| `languages_url` | `string` |  |
| `topics` | `array` |  |
| `stargazers_url` | `string` |  |
| `owner` | `object` | Simple User |
| `role_name` | `string` |  |
| `pulls_url` | `string` |  |
| `releases_url` | `string` |  |
| `branches_url` | `string` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `full_name` | `string` |  |
| `private` | `boolean` |  |
| `contributors_url` | `string` |  |
| `permissions` | `object` |  |
| `clone_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `contents_url` | `string` |  |
| `is_template` | `boolean` |  |
| `keys_url` | `string` |  |
| `tags_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `svn_url` | `string` |  |
| `homepage` | `string` |  |
| `open_issues` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `pushed_at` | `string` |  |
| `default_branch` | `string` |  |
| `has_issues` | `boolean` |  |
| `disabled` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `subscription_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `forks_url` | `string` |  |
| `archive_url` | `string` |  |
| `size` | `integer` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `milestones_url` | `string` |  |
| `forks` | `integer` |  |
| `network_count` | `integer` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `owner, repo` | The `parent` and `source` objects are present when the repository is a fork. `parent` is the repository this repository was forked from, `source` is the ultimate source for the network. |
| `list_for_authenticated_user` | `SELECT` |  | Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership. |
| `list_for_org` | `SELECT` | `org` | Lists repositories for the specified organization. |
| `list_for_user` | `SELECT` | `username` | Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user. |
| `create_for_authenticated_user` | `INSERT` | `data__name` | Creates a new repository for the authenticated user.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository. |
| `create_in_org` | `INSERT` | `org, data__name` | Creates a new repository in the specified organization. The authenticated user must be a member of the organization.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| `create_using_template` | `INSERT` | `template_owner, template_repo, data__name` | Creates a new repository using a repository template. Use the `template_owner` and `template_repo` route parameters to specify the repository to use as the template. The authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository's information using the [Get a repository](https://docs.github.com/rest/reference/repos#get-a-repository) endpoint and check that the `is_template` key is `true`.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
| `delete` | `DELETE` | `owner, repo` | Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.<br /><br />If an organization owner has configured the organization to prevent members from deleting organization-owned<br />repositories, you will get a `403 Forbidden` response. |
| `check_vulnerability_alerts` | `EXEC` | `owner, repo` | Shows whether dependency alerts are enabled or disabled for a repository. The authenticated user must have admin access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies)". |
| `codeowners_errors` | `EXEC` | `owner, repo` | List any syntax errors that are detected in the CODEOWNERS<br />file.<br /><br />For more information about the correct CODEOWNERS syntax,<br />see "[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)." |
| `create_dispatch_event` | `EXEC` | `owner, repo, data__event_type` | You can use this endpoint to trigger a webhook event called `repository_dispatch` when you want activity that happens outside of GitHub to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the `repository_dispatch` event occurs. For an example `repository_dispatch` webhook payload, see "[RepositoryDispatchEvent](https://docs.github.com/webhooks/event-payloads/#repository_dispatch)."<br /><br />The `client_payload` parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the `client_payload` can include a message that a user would like to send using a GitHub Actions workflow. Or the `client_payload` can be used as a test to debug your workflow.<br /><br />This endpoint requires write access to the repository by providing either:<br /><br />  - Personal access tokens with `repo` scope. For more information, see "[Creating a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line)" in the GitHub Help documentation.<br />  - GitHub Apps with both `metadata:read` and `contents:read&write` permissions.<br /><br />This input example shows how you can use the `client_payload` as a test to debug your workflow. |
| `disable_automated_security_fixes` | `EXEC` | `owner, repo` | Disables automated security fixes for a repository. The authenticated user must have admin access to the repository. For more information, see "[Configuring automated security fixes](https://docs.github.com/en/articles/configuring-automated-security-fixes)". |
| `disable_vulnerability_alerts` | `EXEC` | `owner, repo` | Disables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies)". |
| `enable_automated_security_fixes` | `EXEC` | `owner, repo` | Enables automated security fixes for a repository. The authenticated user must have admin access to the repository. For more information, see "[Configuring automated security fixes](https://docs.github.com/en/articles/configuring-automated-security-fixes)". |
| `enable_vulnerability_alerts` | `EXEC` | `owner, repo` | Enables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/en/articles/about-security-alerts-for-vulnerable-dependencies)". |
| `transfer` | `EXEC` | `owner, repo, data__new_owner` | A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original `owner`, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://docs.github.com/articles/about-repository-transfers/). |
| `update` | `EXEC` | `owner, repo` | **Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/reference/repos#replace-all-repository-topics) endpoint. |
