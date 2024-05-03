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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incident_workflows.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The descriptive name of the Action |
| <CopyableCode code="description" /> | `string` | A description of the Action |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="action_type" /> | `string` | The type of Action |
| <CopyableCode code="created_at" /> | `string` | The date-time at which this Action was created |
| <CopyableCode code="created_by_user_id" /> | `string` | The obfuscated Id of the User who created this Action |
| <CopyableCode code="domain_name" /> | `string` | The Verified Domain of the account that created the action |
| <CopyableCode code="function_name" /> | `string` | The Function Name describing the specific functionality of the Action |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="inputs" /> | `array` | Inputs whose values used during Action execution |
| <CopyableCode code="metadata" /> | `string` | JSON-formatted string of metadata pertaining to the Action |
| <CopyableCode code="outputs" /> | `array` | Outputs whose values set during Action execution |
| <CopyableCode code="package_name" /> | `string` | The Package Name corresponding to the broad category of the Action |
| <CopyableCode code="search_keywords" /> | `array` | A set of search keywords to apply to this action. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="tags" /> | `array` | A set of tags to apply to this action. |
| <CopyableCode code="trigger_type" /> | `string` | The type of Trigger this Action is, if action_type is trigger |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="version" /> | `number` | The version of the Action |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_workflow_action" /> | `SELECT` | <CopyableCode code="id" /> | Get an Incident Workflow Action<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="list_incident_workflow_actions" /> | `SELECT` |  | List Incident Workflow Actions<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="_get_incident_workflow_action" /> | `EXEC` | <CopyableCode code="id" /> | Get an Incident Workflow Action<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
| <CopyableCode code="_list_incident_workflow_actions" /> | `EXEC` |  | List Incident Workflow Actions<br /><br />Scoped OAuth requires: `incident_workflows.read`<br /> |
