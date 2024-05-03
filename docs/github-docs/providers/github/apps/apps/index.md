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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.apps.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The ID of the installation. |
| <CopyableCode code="access_tokens_url" /> | `string` |  |
| <CopyableCode code="account" /> | `object` | A GitHub user. |
| <CopyableCode code="app_id" /> | `integer` |  |
| <CopyableCode code="app_slug" /> | `string` |  |
| <CopyableCode code="contact_email" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="events" /> | `array` |  |
| <CopyableCode code="has_multiple_single_files" /> | `boolean` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="permissions" /> | `object` | The permissions granted to the user access token. |
| <CopyableCode code="repositories_url" /> | `string` |  |
| <CopyableCode code="repository_selection" /> | `string` | Describe whether all repositories have been selected or there's a selection involved |
| <CopyableCode code="single_file_name" /> | `string` |  |
| <CopyableCode code="single_file_paths" /> | `array` |  |
| <CopyableCode code="suspended_at" /> | `string` |  |
| <CopyableCode code="suspended_by" /> | `object` | A GitHub user. |
| <CopyableCode code="target_id" /> | `integer` | The ID of the user or organization this token is being scoped to. |
| <CopyableCode code="target_type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_installation" /> | `SELECT` | <CopyableCode code="installation_id" /> | Enables an authenticated GitHub App to find an installation's information using the installation id.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="get_org_installation" /> | `SELECT` | <CopyableCode code="org" /> | Enables an authenticated GitHub App to find the organization's installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="get_repo_installation" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="get_user_installation" /> | `SELECT` | <CopyableCode code="username" /> | Enables an authenticated GitHub App to find the user’s installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="list_installations" /> | `SELECT` |  | You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.<br /><br />The permissions the installation has are included under the `permissions` key. |
| <CopyableCode code="create_from_manifest" /> | `INSERT` | <CopyableCode code="code" /> | Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary `code` used to retrieve the GitHub App's `id`, `pem` (private key), and `webhook_secret`. |
| <CopyableCode code="create_installation_access_token" /> | `INSERT` | <CopyableCode code="installation_id" /> | Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of `401 - Unauthorized`, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the `repository_ids` when creating the token. When you omit `repository_ids`, the response does not contain the `repositories` key.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="delete_installation" /> | `DELETE` | <CopyableCode code="installation_id" /> | Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://docs.github.com/rest/apps/apps#suspend-an-app-installation)" endpoint.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="scope_token" /> | `EXEC` | <CopyableCode code="client_id, data__access_token" /> | Use a non-scoped user access token to create a repository scoped and/or permission scoped user access token. You can specify which repositories the token can access and which permissions are granted to the token. You must use [Basic Authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the `client_id` and `client_secret` of the GitHub App as the username and password. Invalid tokens will return `404 NOT FOUND`. |
| <CopyableCode code="suspend_installation" /> | `EXEC` | <CopyableCode code="installation_id" /> | Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="unsuspend_installation" /> | `EXEC` | <CopyableCode code="installation_id" /> | Removes a GitHub App installation suspension.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
