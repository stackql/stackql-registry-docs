---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.invitations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="email" /> | `string` |  |
| <CopyableCode code="failed_at" /> | `string` |  |
| <CopyableCode code="failed_reason" /> | `string` |  |
| <CopyableCode code="invitation_source" /> | `string` |  |
| <CopyableCode code="invitation_teams_url" /> | `string` |  |
| <CopyableCode code="inviter" /> | `object` | A GitHub user. |
| <CopyableCode code="login" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="role" /> | `string` |  |
| <CopyableCode code="team_count" /> | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_pending_invitations" /> | `SELECT` | <CopyableCode code="org" /> | The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, or `hiring_manager`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`. |
| <CopyableCode code="create_invitation" /> | `INSERT` | <CopyableCode code="org" /> | Invite people to an organization by using their GitHub user ID or their email address. In order to create invitations in an organization, the authenticated user must be an organization owner.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| <CopyableCode code="cancel_invitation" /> | `EXEC` | <CopyableCode code="invitation_id, org" /> | Cancel an organization invitation. In order to cancel an organization invitation, the authenticated user must be an organization owner.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). |
