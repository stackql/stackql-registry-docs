---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_manager.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that define a service in a service topology. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `resourceGroupName, serviceName, serviceTopologyName, subscriptionId` |  |
| `Services_List` | `SELECT` | `resourceGroupName, serviceTopologyName, subscriptionId` |  |
| `Services_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, serviceTopologyName, subscriptionId, data__properties` | Synchronously creates a new service or updates an existing service. |
| `Services_Delete` | `DELETE` | `resourceGroupName, serviceName, serviceTopologyName, subscriptionId` |  |
