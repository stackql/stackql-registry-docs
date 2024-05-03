---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.invitations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the repository invitation. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="expired" /> | `boolean` | Whether or not the invitation has expired |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="invitee" /> | `object` | A GitHub user. |
| <CopyableCode code="inviter" /> | `object` | A GitHub user. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="permissions" /> | `string` | The permission associated with the invitation. |
| <CopyableCode code="repository" /> | `object` | Minimal Repository |
| <CopyableCode code="url" /> | `string` | URL for the repository invitation |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_invitations" /> | `SELECT` | <CopyableCode code="owner, repo" /> | When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations. |
| <CopyableCode code="list_invitations_for_authenticated_user" /> | `SELECT` |  | When authenticating as a user, this endpoint will list all currently open repository invitations for that user. |
| <CopyableCode code="delete_invitation" /> | `DELETE` | <CopyableCode code="invitation_id, owner, repo" /> |  |
| <CopyableCode code="accept_invitation_for_authenticated_user" /> | `EXEC` | <CopyableCode code="invitation_id" /> |  |
| <CopyableCode code="decline_invitation_for_authenticated_user" /> | `EXEC` | <CopyableCode code="invitation_id" /> |  |
| <CopyableCode code="update_invitation" /> | `EXEC` | <CopyableCode code="invitation_id, owner, repo" /> |  |
