---
title: request
hide_title: false
hide_table_of_contents: false
keywords:
  - request
  - teams
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
<tr><td><b>Name</b></td><td><code>request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.teams.request" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessRequestedAt" /> | `number` | Timestamp in milliseconds when the user requested access to the team. |
| <CopyableCode code="bitbucket" /> | `object` | Map of the connected Bitbucket account. |
| <CopyableCode code="confirmed" /> | `boolean` | Current status of the membership. Will be `true` if confirmed, if pending it'll be `false`. |
| <CopyableCode code="github" /> | `object` | Map of the connected GitHub account. |
| <CopyableCode code="gitlab" /> | `object` | Map of the connected GitLab account. |
| <CopyableCode code="joinedFrom" /> | `object` | A map that describes the origin from where the user joined. |
| <CopyableCode code="teamName" /> | `string` | The name of the team. |
| <CopyableCode code="teamSlug" /> | `string` | The slug of the team. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team_access_request" /> | `SELECT` | <CopyableCode code="teamId, userId" /> | Check the status of a join request. It'll respond with a 404 if the request has been declined. If no `userId` path segment was provided, this endpoint will instead return the status of the authenticated user. |
| <CopyableCode code="request_access_to_team" /> | `EXEC` | <CopyableCode code="teamId, data__joinedFrom" /> | Request access to a team as a member. An owner has to approve the request. Only 10 users can request access to a team at the same time. |
