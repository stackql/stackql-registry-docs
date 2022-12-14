---
title: maintenance_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_configurations
  - container_service
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
<tr><td><b>Name</b></td><td><code>maintenance_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.maintenance_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `type` | `string` | Resource type |
| `properties` | `object` | Properties used to configure planned maintenance for a Managed Cluster. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MaintenanceConfigurations_Get` | `SELECT` | `configName, resourceGroupName, resourceName, subscriptionId` |
| `MaintenanceConfigurations_ListByManagedCluster` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `MaintenanceConfigurations_CreateOrUpdate` | `INSERT` | `configName, resourceGroupName, resourceName, subscriptionId` |
| `MaintenanceConfigurations_Delete` | `DELETE` | `configName, resourceGroupName, resourceName, subscriptionId` |
