---
title: incident_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_workflows
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
<tr><td><b>Name</b></td><td><code>incident_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incident_workflows.incident_workflows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | A descriptive name for the Incident Workflow |
| `description` | `string` | A description of what the Incident Workflow does |
| `_type` | `string` |  |
| `created_at` | `string` | The timestamp this Incident Workflow was created |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `self` | `string` | the API show URL at which the object is accessible |
| `steps` | `array` | The ordered list of steps that execute sequentially as part of the workflow |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `team` | `object` | If specified then workflow edit permissions will be scoped to members of this team |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_workflow` | `SELECT` | `id` | Get an existing Incident Workflow<br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `list_incident_workflows` | `SELECT` |  | List existing Incident Workflows.<br /><br />This is the best method to use to list all Incident Workflows in your account. If your use case requires listing Incident Workflows associated with a particular Service, you can use the "listIncidentWorkflowsByService" endpoint.<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `create_incident_workflow_instance` | `INSERT` | `id, data__incident_workflow_instance` | Start an Instance of an Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows:instances.write`<br /> |
| `delete_incident_workflow` | `DELETE` | `id` | Delete an existing Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| `_get_incident_workflow` | `EXEC` | `id` | Get an existing Incident Workflow<br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `_list_incident_workflows` | `EXEC` |  | List existing Incident Workflows.<br /><br />This is the best method to use to list all Incident Workflows in your account. If your use case requires listing Incident Workflows associated with a particular Service, you can use the "listIncidentWorkflowsByService" endpoint.<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| `post_incident_workflow` | `EXEC` | `data__incident_workflow` | Create a new Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| `put_incident_workflow` | `EXEC` | `id, data__incident_workflow` | Update an Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
