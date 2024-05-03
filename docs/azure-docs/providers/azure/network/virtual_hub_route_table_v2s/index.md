---
title: virtual_hub_route_table_v2s
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_route_table_v2s
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
<tr><td><b>Name</b></td><td><code>virtual_hub_route_table_v2s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_route_table_v2s" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VirtualHubRouteTableV2. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Retrieves the details of a VirtualHubRouteTableV2. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all VirtualHubRouteTableV2s. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Creates a VirtualHubRouteTableV2 resource if it doesn't exist else updates the existing VirtualHubRouteTableV2. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Deletes a VirtualHubRouteTableV2. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all VirtualHubRouteTableV2s. |
