---
title: invocations
hide_title: false
hide_table_of_contents: false
keywords:
  - invocations
  - automation_actions
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
<tr><td><b>Name</b></td><td><code>invocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.automation_actions.invocations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `action_id` | `string` |  |
| `action_snapshot` | `object` |  |
| `duration` | `integer` | The duration of the invocation's execution time. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `metadata` | `object` |  |
| `runner_id` | `string` |  |
| `self` | `string` | the API show URL at which the object is accessible |
| `state` | `string` | prepared -- the invocation exists and can be referenced, but is NOT available to a Runner &lt;br&gt; created -- the invocation exists and is waiting for a Runner &lt;br&gt; sent -- invocation sent to a Runner &lt;br&gt; queued -- invocation queued by a Runner &lt;br&gt; running -- invocation is being ran by a Runner &lt;br&gt; aborted -- invocation was aborted on a Runner &lt;br&gt; completed -- invocation completed on a Runner &lt;br&gt; error -- invocation encountered an error on a Runner |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `timing` | `array` | A list of state transitions with timestamps. Only the 'created' transition is guaranteed to exist at any time. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_automation_actions_invocation` | `SELECT` | `id` | Get an Automation Action Invocation<br /> |
| `list_automation_action_invocations` | `SELECT` | `incident_id` | List Invocations<br /> |
| `_get_automation_actions_invocation` | `EXEC` | `id` | Get an Automation Action Invocation<br /> |
| `_list_automation_action_invocations` | `EXEC` | `incident_id` | List Invocations<br /> |
