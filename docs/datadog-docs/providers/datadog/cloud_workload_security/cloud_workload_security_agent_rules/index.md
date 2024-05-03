---
title: cloud_workload_security_agent_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_workload_security_agent_rules
  - cloud_workload_security
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
<tr><td><b>Name</b></td><td><code>cloud_workload_security_agent_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.cloud_workload_security.cloud_workload_security_agent_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the Agent rule. |
| <CopyableCode code="attributes" /> | `object` | A Cloud Workload Security Agent rule returned by the API. |
| <CopyableCode code="type" /> | `string` | The type of the resource. The value should always be `agent_rule`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cloud_workload_security_agent_rule" /> | `SELECT` | <CopyableCode code="agent_rule_id, dd_site" /> | Get the details of a specific Agent rule. |
| <CopyableCode code="list_cloud_workload_security_agent_rules" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get the list of Agent rules. |
| <CopyableCode code="create_cloud_workload_security_agent_rule" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a new Agent rule with the given parameters. |
| <CopyableCode code="delete_cloud_workload_security_agent_rule" /> | `DELETE` | <CopyableCode code="agent_rule_id, dd_site" /> | Delete a specific Agent rule. |
| <CopyableCode code="_get_cloud_workload_security_agent_rule" /> | `EXEC` | <CopyableCode code="agent_rule_id, dd_site" /> | Get the details of a specific Agent rule. |
| <CopyableCode code="_list_cloud_workload_security_agent_rules" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get the list of Agent rules. |
| <CopyableCode code="update_cloud_workload_security_agent_rule" /> | `EXEC` | <CopyableCode code="agent_rule_id, data__data, dd_site" /> | Update a specific Agent rule.<br />Returns the Agent rule object when the request is successful. |
