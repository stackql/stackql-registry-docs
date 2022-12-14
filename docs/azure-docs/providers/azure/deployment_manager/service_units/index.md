---
title: service_units
hide_title: false
hide_table_of_contents: false
keywords:
  - service_units
  - deployment_manager
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_manager.service_units</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that define the service unit. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceUnits_Get` | `SELECT` | `resourceGroupName, serviceName, serviceTopologyName, serviceUnitName, subscriptionId` |  |
| `ServiceUnits_List` | `SELECT` | `resourceGroupName, serviceName, serviceTopologyName, subscriptionId` |  |
| `ServiceUnits_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, serviceTopologyName, serviceUnitName, subscriptionId, data__properties` | This is an asynchronous operation and can be polled to completion using the operation resource returned by this operation. |
| `ServiceUnits_Delete` | `DELETE` | `resourceGroupName, serviceName, serviceTopologyName, serviceUnitName, subscriptionId` |  |
