---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - mysql
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Properties to configure Identity for Bring your Own Keys |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a server. |
| <CopyableCode code="sku" /> | `object` | Billing information related properties of a server. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets information about a server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the servers in a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the servers in a given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Creates a new server or updates an existing server. The update action will overwrite the existing server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Deletes a server. |
| <CopyableCode code="detach_v_net" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Detach VNet on a server. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Manual failover a server. |
| <CopyableCode code="reset_gtid" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Resets GTID on a server. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Restarts a server. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Starts a server. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Stops a server. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
| <CopyableCode code="validate_estimate_high_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Validate a deployment of high availability. |
