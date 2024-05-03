---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - teams
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
<tr><td><b>Id</b></td><td><CopyableCode code="github.teams.invitations" /></td></tr>
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
| <CopyableCode code="list_pending_invitations_in_org" /> | `SELECT` | <CopyableCode code="org, team_slug" /> | The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/invitations`. |
| <CopyableCode code="list_pending_invitations_legacy" /> | `SELECT` | <CopyableCode code="team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List pending team invitations`](https://docs.github.com/rest/teams/members#list-pending-team-invitations) endpoint.<br /><br />The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`. |
