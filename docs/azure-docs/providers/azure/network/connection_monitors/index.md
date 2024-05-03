---
title: connection_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitors
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
<tr><td><b>Name</b></td><td><code>connection_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.connection_monitors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the connection monitor. |
| <CopyableCode code="name" /> | `string` | Name of the connection monitor. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Connection monitor location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a connection monitor. |
| <CopyableCode code="tags" /> | `object` | Connection monitor tags. |
| <CopyableCode code="type" /> | `string` | Connection monitor type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Gets a connection monitor by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all connection monitors for the specified Network Watcher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a connection monitor. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Deletes the specified connection monitor. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all connection monitors for the specified Network Watcher. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Query a snapshot of the most recent connection states. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Starts the specified connection monitor. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Stops the specified connection monitor. |
