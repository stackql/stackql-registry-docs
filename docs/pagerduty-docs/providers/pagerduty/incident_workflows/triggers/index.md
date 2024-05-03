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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incident_workflows.triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="condition" /> | `string` | A PCL condition string.<br /><br />If specified, the trigger will execute when the condition is met on an incident.<br /><br />If unspecified, the trigger will execute on incident creation.<br /><br />Required if trigger_type is “conditional”, not allowed if trigger_type is “manual”.<br /> |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="is_subscribed_to_all_services" /> | `boolean` | Indicates that the Trigger should be associated with All Services |
| <CopyableCode code="permissions" /> | `object` | An object detailing who can start this Trigger. Applicable only to manual Triggers. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="services" /> | `array` | An optional array of Services associated with this workflow. Incidents in any of the listed Services are eligible to fire this Trigger |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="trigger_type" /> | `string` |  |
| <CopyableCode code="trigger_type_name" /> | `string` | Human readable name for the trigger type |
| <CopyableCode code="trigger_url" /> | `string` |  |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="workflow" /> | `object` | Workflow to start when this trigger is invoked |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_workflow_trigger" /> | `SELECT` | <CopyableCode code="id" /> | Retrieve an existing Incident Workflows Trigger<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="list_incident_workflow_triggers" /> | `SELECT` |  | List existing Incident Workflow Triggers<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="create_incident_workflow_trigger" /> | `INSERT` | <CopyableCode code="data__trigger" /> | Create new Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| <CopyableCode code="delete_incident_workflow_trigger" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| <CopyableCode code="delete_service_from_incident_workflow_trigger" /> | `DELETE` | <CopyableCode code="service_id, trigger_id" /> | Remove a an existing Service from an Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| <CopyableCode code="_get_incident_workflow_trigger" /> | `EXEC` | <CopyableCode code="id" /> | Retrieve an existing Incident Workflows Trigger<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="_list_incident_workflow_triggers" /> | `EXEC` |  | List existing Incident Workflow Triggers<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="associate_service_to_incident_workflow_trigger" /> | `EXEC` | <CopyableCode code="id, data__service" /> | Associate a Service with an existing Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| <CopyableCode code="update_incident_workflow_trigger" /> | `EXEC` | <CopyableCode code="id, data__trigger" /> | Update an existing Incident Workflow Trigger<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
