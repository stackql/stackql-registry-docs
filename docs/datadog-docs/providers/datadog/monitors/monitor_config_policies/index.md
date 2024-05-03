---
title: monitor_config_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_config_policies
  - monitors
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitor_config_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.monitors.monitor_config_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of this monitor configuration policy. |
| <CopyableCode code="attributes" /> | `object` | Policy and policy type for a monitor configuration policy. |
| <CopyableCode code="type" /> | `string` | Monitor configuration policy resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_monitor_config_policy" /> | `SELECT` | <CopyableCode code="policy_id, dd_site" /> | Get a monitor configuration policy by `policy_id`. |
| <CopyableCode code="list_monitor_config_policies" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get all monitor configuration policies. |
| <CopyableCode code="create_monitor_config_policy" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a monitor configuration policy. |
| <CopyableCode code="delete_monitor_config_policy" /> | `DELETE` | <CopyableCode code="policy_id, dd_site" /> | Delete a monitor configuration policy. |
| <CopyableCode code="_get_monitor_config_policy" /> | `EXEC` | <CopyableCode code="policy_id, dd_site" /> | Get a monitor configuration policy by `policy_id`. |
| <CopyableCode code="_list_monitor_config_policies" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get all monitor configuration policies. |
| <CopyableCode code="update_monitor_config_policy" /> | `EXEC` | <CopyableCode code="policy_id, data__data, dd_site" /> | Edit a monitor configuration policy. |
