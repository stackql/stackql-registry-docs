---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incident_workflows.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `_type` | `string` |  |
| `condition` | `string` | A PCL condition string.<br /><br />If specified, the trigger will execute when the condition is met on an incident.<br /><br />If unspecified, the trigger will execute on incident creation.<br /><br />Required if trigger_type is “conditional”, not allowed if trigger_type is “manual”.<br /> |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `is_subscribed_to_all_services` | `boolean` | Indicates that the Trigger should be associated with All Services |
| `permissions` | `object` | An object detailing who can start this Trigger. Applicable only to manual Triggers. |
| `self` | `string` | the API show URL at which the object is accessible |
| `services` | `array` | An optional array of Services associated with this workflow. Incidents in any of the listed Services are eligible to fire this Trigger |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `trigger_type` | `string` |  |
| `trigger_type_name` | `string` | Human readable name for the trigger type |
| `trigger_url` | `string` |  |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `workflow` | `object` | Workflow to start when this trigger is invoked |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_workflow_trigger` | `SELECT` | `id` | Retrieve an existing Incident Workflows Trigger<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `list_incident_workflow_triggers` | `SELECT` |  | List existing Incident Workflow Triggers<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `create_incident_workflow_trigger` | `INSERT` | `data__trigger` | Create new Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| `delete_incident_workflow_trigger` | `DELETE` | `id` | Delete an existing Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| `delete_service_from_incident_workflow_trigger` | `DELETE` | `service_id, trigger_id` | Remove a an existing Service from an Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| `_get_incident_workflow_trigger` | `EXEC` | `id` | Retrieve an existing Incident Workflows Trigger<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `_list_incident_workflow_triggers` | `EXEC` |  | List existing Incident Workflow Triggers<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `associate_service_to_incident_workflow_trigger` | `EXEC` | `id, data__service` | Associate a Service with an existing Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| `update_incident_workflow_trigger` | `EXEC` | `id, data__trigger` | Update an existing Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
