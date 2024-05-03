---
title: routing_intent
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_intent
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
<tr><td><b>Name</b></td><td><code>routing_intent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.routing_intent" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | The properties of a RoutingIntent resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routingIntentName, subscriptionId, virtualHubName" /> | Retrieves the details of a RoutingIntent. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RoutingIntent child resources of the VirtualHub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routingIntentName, subscriptionId, virtualHubName" /> | Creates a RoutingIntent resource if it doesn't exist else updates the existing RoutingIntent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routingIntentName, subscriptionId, virtualHubName" /> | Deletes a RoutingIntent. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RoutingIntent child resources of the VirtualHub. |
