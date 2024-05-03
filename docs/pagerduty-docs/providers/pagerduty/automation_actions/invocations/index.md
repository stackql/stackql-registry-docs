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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.automation_actions.invocations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="action_id" /> | `string` |  |
| <CopyableCode code="action_snapshot" /> | `object` |  |
| <CopyableCode code="duration" /> | `integer` | The duration of the invocation's execution time. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="runner_id" /> | `string` |  |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="state" /> | `string` | prepared -- the invocation exists and can be referenced, but is NOT available to a Runner &lt;br&gt; created -- the invocation exists and is waiting for a Runner &lt;br&gt; sent -- invocation sent to a Runner &lt;br&gt; queued -- invocation queued by a Runner &lt;br&gt; running -- invocation is being ran by a Runner &lt;br&gt; aborted -- invocation was aborted on a Runner &lt;br&gt; completed -- invocation completed on a Runner &lt;br&gt; error -- invocation encountered an error on a Runner |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="timing" /> | `array` | A list of state transitions with timestamps. Only the 'created' transition is guaranteed to exist at any time. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_automation_actions_invocation" /> | `SELECT` | <CopyableCode code="id" /> | Get an Automation Action Invocation<br /> |
| <CopyableCode code="list_automation_action_invocations" /> | `SELECT` | <CopyableCode code="incident_id" /> | List Invocations<br /> |
| <CopyableCode code="_get_automation_actions_invocation" /> | `EXEC` | <CopyableCode code="id" /> | Get an Automation Action Invocation<br /> |
| <CopyableCode code="_list_automation_action_invocations" /> | `EXEC` | <CopyableCode code="incident_id" /> | List Invocations<br /> |
