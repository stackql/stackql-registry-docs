---
title: blocking
hide_title: false
hide_table_of_contents: false
keywords:
  - blocking
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
<tr><td><b>Name</b></td><td><code>blocking</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.blocking" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="avatar_url" /> | `string` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="events_url" /> | `string` |
| <CopyableCode code="followers_url" /> | `string` |
| <CopyableCode code="following_url" /> | `string` |
| <CopyableCode code="gists_url" /> | `string` |
| <CopyableCode code="gravatar_id" /> | `string` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="organizations_url" /> | `string` |
| <CopyableCode code="received_events_url" /> | `string` |
| <CopyableCode code="repos_url" /> | `string` |
| <CopyableCode code="site_admin" /> | `boolean` |
| <CopyableCode code="starred_at" /> | `string` |
| <CopyableCode code="starred_url" /> | `string` |
| <CopyableCode code="subscriptions_url" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_blocked_users" /> | `SELECT` | <CopyableCode code="org" /> | List the users blocked by an organization. |
| <CopyableCode code="block_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Blocks the given user on behalf of the specified organization and returns a 204. If the organization cannot block the given user a 422 is returned. |
| <CopyableCode code="check_blocked_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Returns a 204 if the given user is blocked by the given organization. Returns a 404 if the organization is not blocking the user, or if the user account has been identified as spam by GitHub. |
| <CopyableCode code="unblock_user" /> | `EXEC` | <CopyableCode code="org, username" /> | Unblocks the given user on behalf of the specified organization. |
