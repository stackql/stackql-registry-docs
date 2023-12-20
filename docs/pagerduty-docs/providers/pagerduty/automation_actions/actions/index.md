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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.automation_actions.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_action_classification` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_action_data_reference` | `object` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_action_type` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_creation_time` | `string` | The date/time |
| `AutomationActionsProcessAutomationJobActionWithTeams_description` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `AutomationActionsProcessAutomationJobActionWithTeams_id` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_last_run` | `string` | The date/time |
| `AutomationActionsProcessAutomationJobActionWithTeams_last_run_by` | `` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_metadata` | `object` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_modify_time` | `string` | The date/time |
| `AutomationActionsProcessAutomationJobActionWithTeams_name` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_privileges` | `object` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_runner` | `string` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_runner_type` | `string` | sidecar -- The runner is backed by an external sidecar that polls for invocations.<br />runbook -- The runner communicates directly with a runbook instance.<br /> |
| `AutomationActionsProcessAutomationJobActionWithTeams_self` | `string` | the API show URL at which the object is accessible |
| `AutomationActionsProcessAutomationJobActionWithTeams_services` | `array` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `AutomationActionsProcessAutomationJobActionWithTeams_teams` | `array` |  |
| `AutomationActionsProcessAutomationJobActionWithTeams_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `action_classification` | `string` |  |
| `action_data_reference` | `object` |  |
| `action_type` | `string` |  |
| `creation_time` | `string` | The date/time |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `last_run` | `string` | The date/time |
| `last_run_by` | `` |  |
| `metadata` | `object` |  |
| `modify_time` | `string` | The date/time |
| `privileges` | `object` |  |
| `runner` | `string` |  |
| `runner_type` | `string` | sidecar -- The runner is backed by an external sidecar that polls for invocations.<br />runbook -- The runner communicates directly with a runbook instance.<br /> |
| `self` | `string` | the API show URL at which the object is accessible |
| `services` | `array` |  |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` |  |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_all_automation_actions` | `SELECT` |  | Lists Automation Actions matching provided query params.<br /><br />The returned records are sorted by action name in alphabetical order.<br /><br />See [`Cursor-based pagination`](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for instructions on how to paginate through the result set.<br /> |
| `get_automation_action` | `SELECT` | `id` | Get an Automation Action<br /> |
| `create_automation_action` | `INSERT` | `data__action` | Create a Script, Process Automation, or Runbook Automation action<br /> |
| `create_automation_action_invocation` | `INSERT` | `id, data__invocation` | Invokes an Action<br /> |
| `delete_automation_action` | `DELETE` | `id` | Delete an Automation Action<br /> |
| `_get_all_automation_actions` | `EXEC` |  | Lists Automation Actions matching provided query params.<br /><br />The returned records are sorted by action name in alphabetical order.<br /><br />See [`Cursor-based pagination`](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for instructions on how to paginate through the result set.<br /> |
| `_get_automation_action` | `EXEC` | `id` | Get an Automation Action<br /> |
| `update_automation_action` | `EXEC` | `id, data__action` | Updates an Automation Action<br /> |
