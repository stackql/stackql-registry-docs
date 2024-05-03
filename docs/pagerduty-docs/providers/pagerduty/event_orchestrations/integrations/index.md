---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - event_orchestrations
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
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.event_orchestrations.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the Integration. |
| <CopyableCode code="label" /> | `string` | Name of the Integration. |
| <CopyableCode code="parameters" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_orchestration_integration" /> | `SELECT` | <CopyableCode code="id, integration_id" /> | Get an Integration associated with this Event Orchestrations.<br /><br />You can use the Routing Key from this Integration to send events to PagerDuty!<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| <CopyableCode code="list_orchestration_integrations" /> | `SELECT` | <CopyableCode code="id" /> | List the Integrations associated with this Event Orchestrations.<br /><br />You can use a Routing Key from these Integrations to send events to PagerDuty!<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| <CopyableCode code="delete_orchestration_integration" /> | `DELETE` | <CopyableCode code="id, integration_id" /> | Delete an Integration and its associated Routing Key.<br /><br />Once deleted, PagerDuty will drop all future events sent to PagerDuty using the Routing Key.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
| <CopyableCode code="_get_orchestration_integration" /> | `EXEC` | <CopyableCode code="id, integration_id" /> | Get an Integration associated with this Event Orchestrations.<br /><br />You can use the Routing Key from this Integration to send events to PagerDuty!<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| <CopyableCode code="_list_orchestration_integrations" /> | `EXEC` | <CopyableCode code="id" /> | List the Integrations associated with this Event Orchestrations.<br /><br />You can use a Routing Key from these Integrations to send events to PagerDuty!<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| <CopyableCode code="migrate_orchestration_integration" /> | `EXEC` | <CopyableCode code="id, data__integration_id, data__source_id, data__source_type" /> | Move an Integration and its Routing Key from the Event Orchestration specified in the request payload, to the Event Orchestration specified in the request URL.<br /><br />Any future events sent to this Integration's Routing Key will be processed by this Event Orchestration's Rules.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
| <CopyableCode code="post_orchestration_integration" /> | `EXEC` | <CopyableCode code="id, data__integration" /> | Create an Integration associated with this Event Orchestration.<br /><br />You can then use the Routing Key from this new Integration to send events to PagerDuty!<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
| <CopyableCode code="update_orchestration_integration" /> | `EXEC` | <CopyableCode code="id, integration_id, data__integration" /> | Update an Integration associated with this Event Orchestrations.<br /><br />You can use the Routing Key from this Integration to send events to PagerDuty!<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
