---
title: vpn_link_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_link_connections
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
<tr><td><b>Name</b></td><td><code>vpn_link_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_link_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnConnection. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_vpn_connection" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, resourceGroupName, subscriptionId" /> | Retrieves all vpn site link connections for a particular virtual wan vpn gateway vpn connection. |
| <CopyableCode code="_list_by_vpn_connection" /> | `EXEC` | <CopyableCode code="connectionName, gatewayName, resourceGroupName, subscriptionId" /> | Retrieves all vpn site link connections for a particular virtual wan vpn gateway vpn connection. |
| <CopyableCode code="reset_connection" /> | `EXEC` | <CopyableCode code="connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId" /> | Resets the VpnLink connection specified. |
