---
title: oncalls
hide_title: false
hide_table_of_contents: false
keywords:
  - oncalls
  - on_calls
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oncalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.on_calls.oncalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="end" /> | `string` | The end of the on-call. If `null`, the user does not go off-call. |
| <CopyableCode code="escalation_level" /> | `integer` | The escalation level for the on-call. |
| <CopyableCode code="escalation_policy" /> | `object` |  |
| <CopyableCode code="schedule" /> | `object` |  |
| <CopyableCode code="start" /> | `string` | The start of the on-call. If `null`, the on-call is a permanent user on-call. |
| <CopyableCode code="user" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_on_calls" /> | `SELECT` |  |
| <CopyableCode code="_list_on_calls" /> | `EXEC` |  |
