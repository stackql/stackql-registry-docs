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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oncalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.on_calls.oncalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `end` | `string` | The end of the on-call. If `null`, the user does not go off-call. |
| `escalation_level` | `integer` | The escalation level for the on-call. |
| `escalation_policy` | `object` |  |
| `schedule` | `object` |  |
| `start` | `string` | The start of the on-call. If `null`, the on-call is a permanent user on-call. |
| `user` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_on_calls` | `SELECT` |  |
| `_list_on_calls` | `EXEC` |  |
