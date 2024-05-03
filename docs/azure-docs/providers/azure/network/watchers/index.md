---
title: watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers
  - network
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
<tr><td><b>Name</b></td><td><code>watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The network watcher properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Gets the specified network watcher by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all network watchers by resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Creates or updates a network watcher in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Deletes the specified network watcher resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all network watchers by resource group. |
| <CopyableCode code="check_connectivity" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__destination, data__source" /> | Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server. |
| <CopyableCode code="set_flow_log_configuration" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId" /> | Configures flow log and traffic analytics (optional) on a specified resource. |
| <CopyableCode code="verify_ip_flow" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__direction, data__localIPAddress, data__localPort, data__protocol, data__remoteIPAddress, data__remotePort, data__targetResourceId" /> | Verify IP flow from the specified VM to a location given the currently configured NSG rules. |
