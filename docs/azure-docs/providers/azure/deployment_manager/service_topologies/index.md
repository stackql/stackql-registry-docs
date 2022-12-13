---
title: service_topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - service_topologies
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
<tr><td><b>Name</b></td><td><code>service_topologies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_manager.service_topologies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that define the service topology. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceTopologies_Get` | `SELECT` | `resourceGroupName, serviceTopologyName, subscriptionId` |  |
| `ServiceTopologies_List` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `ServiceTopologies_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceTopologyName, subscriptionId, data__properties` | Synchronously creates a new service topology or updates an existing service topology. |
| `ServiceTopologies_Delete` | `DELETE` | `resourceGroupName, serviceTopologyName, subscriptionId` |  |
