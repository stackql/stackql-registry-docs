---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - user
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.user.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The User's unique identifier. |
| `name` | `string` | Name associated with the User account, or `null` if none has been provided. |
| `AuthUserLimited_avatar` | `string` | SHA1 hash of the avatar for the User account. Can be used in conjuction with the ... endpoint to retrieve the avatar image. |
| `AuthUserLimited_email` | `string` | Email address associated with the User account. |
| `AuthUserLimited_id` | `string` | The User's unique identifier. |
| `AuthUserLimited_name` | `string` | Name associated with the User account, or `null` if none has been provided. |
| `AuthUserLimited_username` | `string` | Unique username associated with the User account. |
| `AuthUserLimited_version` | `string` | The user's version. Will either be unset or `northstar`. |
| `activeDashboardViews` | `array` | set of dashboard view preferences (cards or list) per scopeId |
| `avatar` | `string` | SHA1 hash of the avatar for the User account. Can be used in conjuction with the ... endpoint to retrieve the avatar image. |
| `billing` | `object` | An object containing billing infomation associated with the User account. |
| `createdAt` | `number` | UNIX timestamp (in milliseconds) when the User account was created. |
| `dataCache` | `object` | data cache settings |
| `defaultTeamId` | `string` | The user's default team. Only applies if the user's `version` is `'northstar'`. |
| `dismissedToasts` | `array` | A record of when, under a certain scopeId, a toast was dismissed |
| `email` | `string` | Email address associated with the User account. |
| `favoriteProjectsAndSpaces` | `array` | A list of projects and spaces across teams that a user has marked as a favorite. |
| `featureBlocks` | `object` | Feature blocks for the user |
| `hasTrialAvailable` | `boolean` | Whether the user has a trial available for a paid plan subscription. |
| `importFlowGitNamespace` | `` |  |
| `importFlowGitNamespaceId` | `` |  |
| `importFlowGitProvider` | `string` |  |
| `limited` | `boolean` | Property indicating that this User data contains only limited information, due to the authentication token missing privileges to read the full User data. Re-login with email, GitHub, GitLab or Bitbucket in order to upgrade the authentication token with the necessary privileges. |
| `preferredScopesAndGitNamespaces` | `array` |  |
| `remoteCaching` | `object` | remote caching settings |
| `resourceConfig` | `object` | An object containing infomation related to the amount of platform resources may be allocated to the User account. |
| `softBlock` | `object` | When the User account has been "soft blocked", this property will contain the date when the restriction was enacted, and the identifier for why. |
| `stagingPrefix` | `string` | Prefix that will be used in the URL of "Preview" deployments created by the User account. |
| `username` | `string` | Unique username associated with the User account. |
| `version` | `string` | The user's version. Will either be unset or `northstar`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_auth_user` | `SELECT` |  | Retrieves information related to the currently authenticated User. |
| `request_delete` | `DELETE` |  | Initiates the deletion process for the currently authenticated User, by sending a deletion confirmation email. The email contains a link that the user needs to visit in order to proceed with the deletion process. |
| `_get_auth_user` | `EXEC` |  | Retrieves information related to the currently authenticated User. |
