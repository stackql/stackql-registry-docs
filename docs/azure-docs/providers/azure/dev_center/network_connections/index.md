---
title: network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connections
  - dev_center
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
<tr><td><b>Name</b></td><td><code>network_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.network_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets a network connection resource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` |  | Lists network connections in a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` |  | Lists network connections in a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates a Network Connections resource |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes a Network Connections resource |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` |  | Lists network connections in a resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` |  | Lists network connections in a subscription |
| <CopyableCode code="run_health_checks" /> | `EXEC` | <CopyableCode code="networkConnectionName, resourceGroupName, subscriptionId" /> | Triggers a new health check run. The execution and health check result can be tracked via the network Connection health check details |
| <CopyableCode code="update" /> | `EXEC` |  | Partially updates a Network Connection |
