---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - activity
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.activity.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="actor" /> | `object` | Actor |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="org" /> | `object` | Actor |
| <CopyableCode code="payload" /> | `object` |  |
| <CopyableCode code="public" /> | `boolean` |  |
| <CopyableCode code="repo" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_events_for_authenticated_user" /> | `SELECT` | <CopyableCode code="username" /> | If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events. |
| <CopyableCode code="list_org_events_for_authenticated_user" /> | `SELECT` | <CopyableCode code="org, username" /> | This is the user's organization dashboard. You must be authenticated as the user to view this. |
| <CopyableCode code="list_repo_events" /> | `SELECT` | <CopyableCode code="owner, repo" /> | **Note**: This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.<br /> |
