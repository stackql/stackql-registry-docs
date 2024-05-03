---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - orgs
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
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.memberships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="organization" /> | `object` | A GitHub organization. |
| <CopyableCode code="organization_url" /> | `string` |  |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="role" /> | `string` | The user's membership type in the organization. |
| <CopyableCode code="state" /> | `string` | The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation. |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_membership_for_authenticated_user" /> | `SELECT` | <CopyableCode code="org" /> | If the authenticated user is an active or pending member of the organization, this endpoint will return the user's membership. If the authenticated user is not affiliated with the organization, a `404` is returned. This endpoint will return a `403` if the request is made by a GitHub App that is blocked by the organization. |
| <CopyableCode code="get_membership_for_user" /> | `SELECT` | <CopyableCode code="org, username" /> | In order to get a user's membership with an organization, the authenticated user must be an organization member. The `state` parameter in the response can be used to identify the user's membership status. |
| <CopyableCode code="list_memberships_for_authenticated_user" /> | `SELECT` |  | Lists all of the authenticated user's organization memberships. |
| <CopyableCode code="remove_membership_for_user" /> | `DELETE` | <CopyableCode code="org, username" /> | In order to remove a user's membership with an organization, the authenticated user must be an organization owner.<br /><br />If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases. |
| <CopyableCode code="check_membership_for_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Check if a user is, publicly or privately, a member of the organization. |
| <CopyableCode code="check_public_membership_for_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Check if the provided user is a public member of the organization. |
| <CopyableCode code="remove_public_membership_for_authenticated_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Removes the public membership for the authenticated user from the specified organization, unless public visibility is enforced by default. |
| <CopyableCode code="set_membership_for_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Only authenticated organization owners can add a member to the organization or update the member's role.<br /><br />*   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user's [membership status](https://docs.github.com/rest/orgs/members#get-organization-membership-for-a-user) will be `pending` until they accept the invitation.<br />    <br />*   Authenticated users can _update_ a user's membership by passing the `role` parameter. If the authenticated user changes a member's role to `admin`, the affected user will receive an email notifying them that they've been made an organization owner. If the authenticated user changes an owner's role to `member`, no email will be sent.<br /><br />**Rate limits**<br /><br />To prevent abuse, the authenticated user is limited to 50 organization invitations per 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period. |
| <CopyableCode code="set_public_membership_for_authenticated_user" /> | `EXEC` | <CopyableCode code="org, username" /> | The user can publicize their own membership. (A user cannot publicize the membership for another user.)<br /><br />Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| <CopyableCode code="update_membership_for_authenticated_user" /> | `EXEC` | <CopyableCode code="org, data__state" /> | Converts the authenticated user to an active member of the organization, if that user has a pending invitation from the organization. |
