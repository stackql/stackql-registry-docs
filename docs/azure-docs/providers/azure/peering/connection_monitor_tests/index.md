---
title: connection_monitor_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitor_tests
  - peering
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
<tr><td><b>Name</b></td><td><code>connection_monitor_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.connection_monitor_tests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a Connection Monitor Test. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId" /> | Gets an existing connection monitor test with the specified name under the given subscription, resource group and peering service. |
| <CopyableCode code="list_by_peering_service" /> | `SELECT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Lists all connection monitor tests under the given subscription, resource group and peering service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId" /> | Creates or updates a connection monitor test with the specified name under the given subscription, resource group and peering service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId" /> | Deletes an existing connection monitor test with the specified name under the given subscription, resource group and peering service. |
