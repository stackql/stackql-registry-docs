---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - mobile_network
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Service properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId` | Gets information about the specified service. |
| `Services_ListByMobileNetwork` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Gets all the services in a mobile network. |
| `Services_CreateOrUpdate` | `INSERT` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId, data__properties` | Creates or updates a service. |
| `Services_Delete` | `DELETE` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId` | Deletes the specified service. |
| `Services_UpdateTags` | `EXEC` | `mobileNetworkName, resourceGroupName, serviceName, subscriptionId` | Updates service tags. |
