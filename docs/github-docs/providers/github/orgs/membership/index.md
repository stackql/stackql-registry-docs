---
title: membership
hide_title: false
hide_table_of_contents: false
keywords:
  - membership
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>membership</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.membership</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `permissions` | `object` |  |
| `role` | `string` | The user's membership type in the organization. |
| `state` | `string` | The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation. |
| `url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `organization` | `object` | A GitHub organization. |
| `organization_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_membership_for_user` | `SELECT` | `org, username` | In order to get a user's membership with an organization, the authenticated user must be an organization member. The `state` parameter in the response can be used to identify the user's membership status. |
| `remove_membership_for_user` | `DELETE` | `org, username` | In order to remove a user's membership with an organization, the authenticated user must be an organization owner.<br /><br />If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases. |
| `check_membership_for_user` | `EXEC` | `org, username` | Check if a user is, publicly or privately, a member of the organization. |
| `set_membership_for_user` | `EXEC` | `org, username` | Only authenticated organization owners can add a member to the organization or update the member's role.<br /><br />*   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user's [membership status](https://docs.github.com/rest/orgs/members#get-organization-membership-for-a-user) will be `pending` until they accept the invitation.<br />    <br />*   Authenticated users can _update_ a user's membership by passing the `role` parameter. If the authenticated user changes a member's role to `admin`, the affected user will receive an email notifying them that they've been made an organization owner. If the authenticated user changes an owner's role to `member`, no email will be sent.<br /><br />**Rate limits**<br /><br />To prevent abuse, the authenticated user is limited to 50 organization invitations per 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period. |
