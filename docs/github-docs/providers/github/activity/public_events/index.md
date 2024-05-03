---
title: public_events
hide_title: false
hide_table_of_contents: false
keywords:
  - public_events
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
<tr><td><b>Name</b></td><td><code>public_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.activity.public_events" /></td></tr>
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
| <CopyableCode code="list_public_events" /> | `SELECT` |  | We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago. |
| <CopyableCode code="list_public_events_for_repo_network" /> | `SELECT` | <CopyableCode code="owner, repo" /> |  |
| <CopyableCode code="list_public_events_for_user" /> | `SELECT` | <CopyableCode code="username" /> |  |
| <CopyableCode code="list_public_org_events" /> | `SELECT` | <CopyableCode code="org" /> |  |
