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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.user.user" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The User's unique identifier. |
| <CopyableCode code="name" /> | `string` | Name associated with the User account, or `null` if none has been provided. |
| <CopyableCode code="AuthUserLimited_avatar" /> | `string` | SHA1 hash of the avatar for the User account. Can be used in conjuction with the ... endpoint to retrieve the avatar image. |
| <CopyableCode code="AuthUserLimited_email" /> | `string` | Email address associated with the User account. |
| <CopyableCode code="AuthUserLimited_id" /> | `string` | The User's unique identifier. |
| <CopyableCode code="AuthUserLimited_name" /> | `string` | Name associated with the User account, or `null` if none has been provided. |
| <CopyableCode code="AuthUserLimited_username" /> | `string` | Unique username associated with the User account. |
| <CopyableCode code="AuthUserLimited_version" /> | `string` | The user's version. Will either be unset or `northstar`. |
| <CopyableCode code="activeDashboardViews" /> | `array` | set of dashboard view preferences (cards or list) per scopeId |
| <CopyableCode code="avatar" /> | `string` | SHA1 hash of the avatar for the User account. Can be used in conjuction with the ... endpoint to retrieve the avatar image. |
| <CopyableCode code="billing" /> | `object` | An object containing billing infomation associated with the User account. |
| <CopyableCode code="createdAt" /> | `number` | UNIX timestamp (in milliseconds) when the User account was created. |
| <CopyableCode code="dataCache" /> | `object` | data cache settings |
| <CopyableCode code="defaultTeamId" /> | `string` | The user's default team. Only applies if the user's `version` is `'northstar'`. |
| <CopyableCode code="dismissedToasts" /> | `array` | A record of when, under a certain scopeId, a toast was dismissed |
| <CopyableCode code="email" /> | `string` | Email address associated with the User account. |
| <CopyableCode code="favoriteProjectsAndSpaces" /> | `array` | A list of projects and spaces across teams that a user has marked as a favorite. |
| <CopyableCode code="featureBlocks" /> | `object` | Feature blocks for the user |
| <CopyableCode code="hasTrialAvailable" /> | `boolean` | Whether the user has a trial available for a paid plan subscription. |
| <CopyableCode code="importFlowGitNamespace" /> | `` |  |
| <CopyableCode code="importFlowGitNamespaceId" /> | `` |  |
| <CopyableCode code="importFlowGitProvider" /> | `string` |  |
| <CopyableCode code="limited" /> | `boolean` | Property indicating that this User data contains only limited information, due to the authentication token missing privileges to read the full User data. Re-login with email, GitHub, GitLab or Bitbucket in order to upgrade the authentication token with the necessary privileges. |
| <CopyableCode code="preferredScopesAndGitNamespaces" /> | `array` |  |
| <CopyableCode code="remoteCaching" /> | `object` | remote caching settings |
| <CopyableCode code="resourceConfig" /> | `object` | An object containing infomation related to the amount of platform resources may be allocated to the User account. |
| <CopyableCode code="softBlock" /> | `object` | When the User account has been "soft blocked", this property will contain the date when the restriction was enacted, and the identifier for why. |
| <CopyableCode code="stagingPrefix" /> | `string` | Prefix that will be used in the URL of "Preview" deployments created by the User account. |
| <CopyableCode code="username" /> | `string` | Unique username associated with the User account. |
| <CopyableCode code="version" /> | `string` | The user's version. Will either be unset or `northstar`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_auth_user" /> | `SELECT` |  | Retrieves information related to the currently authenticated User. |
| <CopyableCode code="request_delete" /> | `DELETE` |  | Initiates the deletion process for the currently authenticated User, by sending a deletion confirmation email. The email contains a link that the user needs to visit in order to proceed with the deletion process. |
| <CopyableCode code="_get_auth_user" /> | `EXEC` |  | Retrieves information related to the currently authenticated User. |
