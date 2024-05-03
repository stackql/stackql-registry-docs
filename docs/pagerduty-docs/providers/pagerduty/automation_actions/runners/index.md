---
title: runners
hide_title: false
hide_table_of_contents: false
keywords:
  - runners
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
<tr><td><b>Name</b></td><td><code>runners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.automation_actions.runners" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="associated_actions" /> | `object` | References to at most 3 actions associated with the Runner. Use appropriate endpoints to retrieve the full list of associated actions. |
| <CopyableCode code="creation_time" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="last_seen" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` | Additional metadata |
| <CopyableCode code="privileges" /> | `object` |  |
| <CopyableCode code="runbook_base_uri" /> | `string` | The base URI of the Runbook server to connect to. May only contain alphanumeric characters, periods, underscores and dashes. |
| <CopyableCode code="runner_type" /> | `string` | sidecar -- The runner is backed by an external sidecar that polls for invocations.<br />runbook -- The runner communicates directly with a runbook instance.<br /> |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="status" /> | `string` | Configured -- Runner has connected to the backend at least once <br />NotConfigured -- Runner has never connected to backend<br /> |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="teams" /> | `array` | The list of teams associated with the Runner |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_automation_actions_runner" /> | `SELECT` | <CopyableCode code="id" /> | Get an Automation Action runner<br /> |
| <CopyableCode code="get_automation_actions_runners" /> | `SELECT` |  | Lists Automation Action runners matching provided query params.<br />The returned records are sorted by runner name in alphabetical order.<br /><br />See [`Cursor-based pagination`](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for instructions on how to paginate through the result set.<br /> |
| <CopyableCode code="create_automation_actions_runner" /> | `INSERT` | <CopyableCode code="data__runner" /> | Create a Process Automation or a Runbook Automation runner.<br /> |
| <CopyableCode code="delete_automation_actions_runner" /> | `DELETE` | <CopyableCode code="id" /> | Delete an Automation Action runner<br /> |
| <CopyableCode code="_get_automation_actions_runner" /> | `EXEC` | <CopyableCode code="id" /> | Get an Automation Action runner<br /> |
| <CopyableCode code="_get_automation_actions_runners" /> | `EXEC` |  | Lists Automation Action runners matching provided query params.<br />The returned records are sorted by runner name in alphabetical order.<br /><br />See [`Cursor-based pagination`](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for instructions on how to paginate through the result set.<br /> |
| <CopyableCode code="update_automation_actions_runner" /> | `EXEC` | <CopyableCode code="id, data__runner" /> | Update an Automation Action runner<br /> |
