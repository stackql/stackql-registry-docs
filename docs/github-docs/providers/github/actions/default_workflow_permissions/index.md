---
title: default_workflow_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - default_workflow_permissions
  - actions
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
<tr><td><b>Name</b></td><td><code>default_workflow_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.default_workflow_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `can_approve_pull_request_reviews` | `boolean` | Whether GitHub Actions can approve pull requests. Enabling this can be a security risk. |
| `default_workflow_permissions` | `string` | The default workflow permissions granted to the GITHUB_TOKEN when running workflows. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_github_actions_default_workflow_permissions_organization` | `SELECT` | `org` | Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization,<br />as well as whether GitHub Actions can submit approving pull request reviews. For more information, see<br />"[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `get_github_actions_default_workflow_permissions_repository` | `SELECT` | `owner, repo` | Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a repository,<br />as well as if GitHub Actions can submit approving pull request reviews.<br />For more information, see "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the repository `administration` permission to use this API. |
| `set_github_actions_default_workflow_permissions_organization` | `EXEC` | `org` | Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization, and sets if GitHub Actions<br />can submit approving pull request reviews. For more information, see<br />"[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `set_github_actions_default_workflow_permissions_repository` | `EXEC` | `owner, repo` | Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a repository, and sets if GitHub Actions<br />can submit approving pull request reviews.<br />For more information, see "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the repository `administration` permission to use this API. |
