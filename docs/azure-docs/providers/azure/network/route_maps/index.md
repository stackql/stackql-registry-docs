---
title: route_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - route_maps
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
<tr><td><b>Name</b></td><td><code>route_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of RouteMap resource |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeMapName, subscriptionId, virtualHubName" /> | Retrieves the details of a RouteMap. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RouteMaps. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeMapName, subscriptionId, virtualHubName" /> | Creates a RouteMap if it doesn't exist else updates the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeMapName, subscriptionId, virtualHubName" /> | Deletes a RouteMap. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RouteMaps. |
