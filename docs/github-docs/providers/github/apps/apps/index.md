---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `access_tokens_url` | `string` |  |
| `contact_email` | `string` |  |
| `repositories_url` | `string` |  |
| `single_file_name` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `account` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `suspended_by` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `permissions` | `object` | The permissions granted to the user access token. |
| `events` | `array` |  |
| `app_slug` | `string` |  |
| `has_multiple_single_files` | `boolean` |  |
| `target_type` | `string` |  |
| `suspended_at` | `string` |  |
| `updated_at` | `string` |  |
| `single_file_paths` | `array` |  |
| `app_id` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_installation` | `SELECT` | `installation_id` | Enables an authenticated GitHub App to find an installation's information using the installation id.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `get_org_installation` | `SELECT` | `org` | Enables an authenticated GitHub App to find the organization's installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `get_repo_installation` | `SELECT` | `owner, repo` | Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `get_user_installation` | `SELECT` | `username` | Enables an authenticated GitHub App to find the user’s installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `list_installations` | `SELECT` |  | You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.<br /><br />The permissions the installation has are included under the `permissions` key. |
| `create_from_manifest` | `INSERT` | `code` | Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary `code` used to retrieve the GitHub App's `id`, `pem` (private key), and `webhook_secret`. |
| `create_installation_access_token` | `INSERT` | `installation_id` | Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of `401 - Unauthorized`, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the `repository_ids` when creating the token. When you omit `repository_ids`, the response does not contain the `repositories` key.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `delete_installation` | `DELETE` | `installation_id` | Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://docs.github.com/rest/apps/apps#suspend-an-app-installation)" endpoint.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `scope_token` | `EXEC` | `client_id, data__access_token` | Use a non-scoped user access token to create a repository scoped and/or permission scoped user access token. You can specify which repositories the token can access and which permissions are granted to the token. You must use [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the `client_id` and `client_secret` of the GitHub App as the username and password. Invalid tokens will return `404 NOT FOUND`. |
| `suspend_installation` | `EXEC` | `installation_id` | Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `unsuspend_installation` | `EXEC` | `installation_id` | Removes a GitHub App installation suspension.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
