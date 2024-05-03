---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.automation_actions.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_action_classification" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_action_data_reference" /> | `object` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_action_type" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_creation_time" /> | `string` | The date/time |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_description" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_id" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_last_run" /> | `string` | The date/time |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_last_run_by" /> | `` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_metadata" /> | `object` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_modify_time" /> | `string` | The date/time |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_name" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_privileges" /> | `object` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_runner" /> | `string` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_runner_type" /> | `string` | sidecar -- The runner is backed by an external sidecar that polls for invocations.<br />runbook -- The runner communicates directly with a runbook instance.<br /> |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_services" /> | `array` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_teams" /> | `array` |  |
| <CopyableCode code="AutomationActionsProcessAutomationJobActionWithTeams_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="action_classification" /> | `string` |  |
| <CopyableCode code="action_data_reference" /> | `object` |  |
| <CopyableCode code="action_type" /> | `string` |  |
| <CopyableCode code="creation_time" /> | `string` | The date/time |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="last_run" /> | `string` | The date/time |
| <CopyableCode code="last_run_by" /> | `` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="modify_time" /> | `string` | The date/time |
| <CopyableCode code="privileges" /> | `object` |  |
| <CopyableCode code="runner" /> | `string` |  |
| <CopyableCode code="runner_type" /> | `string` | sidecar -- The runner is backed by an external sidecar that polls for invocations.<br />runbook -- The runner communicates directly with a runbook instance.<br /> |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="services" /> | `array` |  |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="teams" /> | `array` |  |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_automation_actions" /> | `SELECT` |  | Lists Automation Actions matching provided query params.<br /><br />The returned records are sorted by action name in alphabetical order.<br /><br />See [`Cursor-based pagination`](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for instructions on how to paginate through the result set.<br /> |
| <CopyableCode code="get_automation_action" /> | `SELECT` | <CopyableCode code="id" /> | Get an Automation Action<br /> |
| <CopyableCode code="create_automation_action" /> | `INSERT` | <CopyableCode code="data__action" /> | Create a Script, Process Automation, or Runbook Automation action<br /> |
| <CopyableCode code="create_automation_action_invocation" /> | `INSERT` | <CopyableCode code="id, data__invocation" /> | Invokes an Action<br /> |
| <CopyableCode code="delete_automation_action" /> | `DELETE` | <CopyableCode code="id" /> | Delete an Automation Action<br /> |
| <CopyableCode code="_get_all_automation_actions" /> | `EXEC` |  | Lists Automation Actions matching provided query params.<br /><br />The returned records are sorted by action name in alphabetical order.<br /><br />See [`Cursor-based pagination`](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for instructions on how to paginate through the result set.<br /> |
| <CopyableCode code="_get_automation_action" /> | `EXEC` | <CopyableCode code="id" /> | Get an Automation Action<br /> |
| <CopyableCode code="update_automation_action" /> | `EXEC` | <CopyableCode code="id, data__action" /> | Updates an Automation Action<br /> |
