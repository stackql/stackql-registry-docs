---
title: received_public_events
hide_title: false
hide_table_of_contents: false
keywords:
  - received_public_events
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
<tr><td><b>Name</b></td><td><code>received_public_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.activity.received_public_events" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_received_public_events_for_user" /> | `SELECT` | <CopyableCode code="username" /> |
