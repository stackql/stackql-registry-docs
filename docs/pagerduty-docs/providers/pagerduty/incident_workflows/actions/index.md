---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - incident_workflows
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
<tr><td><b>Id</b></td><td><code>pagerduty.incident_workflows.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The descriptive name of the Action |
| `description` | `string` | A description of the Action |
| `_type` | `string` |  |
| `action_type` | `string` | The type of Action |
| `created_at` | `string` | The date-time at which this Action was created |
| `created_by_user_id` | `string` | The obfuscated Id of the User who created this Action |
| `domain_name` | `string` | The Verified Domain of the account that created the action |
| `function_name` | `string` | The Function Name describing the specific functionality of the Action |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `inputs` | `array` | Inputs whose values used during Action execution |
| `metadata` | `string` | JSON-formatted string of metadata pertaining to the Action |
| `outputs` | `array` | Outputs whose values set during Action execution |
| `package_name` | `string` | The Package Name corresponding to the broad category of the Action |
| `search_keywords` | `array` | A set of search keywords to apply to this action. |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `tags` | `array` | A set of tags to apply to this action. |
| `trigger_type` | `string` | The type of Trigger this Action is, if action_type is trigger |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `version` | `number` | The version of the Action |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_workflow_action` | `SELECT` | `id` | Get an Incident Workflow Action<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `list_incident_workflow_actions` | `SELECT` |  | List Incident Workflow Actions<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `_get_incident_workflow_action` | `EXEC` | `id` | Get an Incident Workflow Action<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `_list_incident_workflow_actions` | `EXEC` |  | List Incident Workflow Actions<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
