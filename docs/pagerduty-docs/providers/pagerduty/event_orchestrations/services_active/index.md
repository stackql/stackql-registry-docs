---
title: services_active
hide_title: false
hide_table_of_contents: false
keywords:
  - services_active
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
<tr><td><b>Name</b></td><td><code>services_active</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.event_orchestrations.services_active" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_orch_active_status" /> | `SELECT` | <CopyableCode code="service_id" /> | Get a Service Orchestration's active status.<br /><br />A Service Orchestration allows you to set an active status based on whether an event will be evaluated against a service orchestration path (true) or service ruleset (false).<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="_get_orch_active_status" /> | `EXEC` | <CopyableCode code="service_id" /> | Get a Service Orchestration's active status.<br /><br />A Service Orchestration allows you to set an active status based on whether an event will be evaluated against a service orchestration path (true) or service ruleset (false).<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="update_orch_active_status" /> | `EXEC` | <CopyableCode code="service_id" /> | Update a Service Orchestration's active status.<br /><br />A Service Orchestration allows you to set an active status based on whether an event will be evaluated against a service orchestration path (true) or service ruleset (false).<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `services.write`<br /> |
