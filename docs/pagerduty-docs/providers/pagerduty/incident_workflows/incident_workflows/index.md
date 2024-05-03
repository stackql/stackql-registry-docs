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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incident_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incident_workflows.incident_workflows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | A descriptive name for the Incident Workflow |
| <CopyableCode code="description" /> | `string` | A description of what the Incident Workflow does |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` | The timestamp this Incident Workflow was created |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="steps" /> | `array` | The ordered list of steps that execute sequentially as part of the workflow |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="team" /> | `object` | If specified then workflow edit permissions will be scoped to members of this team |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_workflow" /> | `SELECT` | <CopyableCode code="id" /> | Get an existing Incident Workflow<br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="list_incident_workflows" /> | `SELECT` |  | List existing Incident Workflows.<br /><br />This is the best method to use to list all Incident Workflows in your account. If your use case requires listing Incident Workflows associated with a particular Service, you can use the "listIncidentWorkflowsByService" endpoint.<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="create_incident_workflow_instance" /> | `INSERT` | <CopyableCode code="id, data__incident_workflow_instance" /> | Start an Instance of an Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows:instances.write`<br /> |
| <CopyableCode code="delete_incident_workflow" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| <CopyableCode code="_get_incident_workflow" /> | `EXEC` | <CopyableCode code="id" /> | Get an existing Incident Workflow<br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="_list_incident_workflows" /> | `EXEC` |  | List existing Incident Workflows.<br /><br />This is the best method to use to list all Incident Workflows in your account. If your use case requires listing Incident Workflows associated with a particular Service, you can use the "listIncidentWorkflowsByService" endpoint.<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="post_incident_workflow" /> | `EXEC` | <CopyableCode code="data__incident_workflow" /> | Create a new Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
| <CopyableCode code="put_incident_workflow" /> | `EXEC` | <CopyableCode code="id, data__incident_workflow" /> | Update an Incident Workflow<br /><br />An Incident Workflow is a sequence of configurable Steps and associated Triggers that can execute automated Actions for a given Incident.<br /><br />Scoped OAuth requires: `incident_workflows.write`<br /> |
