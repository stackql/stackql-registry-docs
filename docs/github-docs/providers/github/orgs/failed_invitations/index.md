---
title: failed_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - failed_invitations
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
<tr><td><b>Name</b></td><td><code>failed_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.failed_invitations" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_failed_invitations" /> | `SELECT` | <CopyableCode code="org" /> |
