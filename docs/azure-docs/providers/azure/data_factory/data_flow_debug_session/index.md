---
title: data_flow_debug_session
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flow_debug_session
  - data_factory
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_flow_debug_session</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.data_flow_debug_session" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Creates a data flow debug session. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Deletes a data flow debug session. |
| <CopyableCode code="add_data_flow" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Add a data flow into debug session. |
| <CopyableCode code="execute_command" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Execute a data flow debug command. |
| <CopyableCode code="query_by_factory" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Query all active data flow debug sessions. |
