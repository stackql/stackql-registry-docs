---
title: fleet_members
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_members
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
<tr><td><b>Name</b></td><td><code>fleet_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.fleet_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | Properties of a Fleet member. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FleetMembers_Get` | `SELECT` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` |  |
| `FleetMembers_ListByFleet` | `SELECT` | `fleetName, resourceGroupName, subscriptionId` |  |
| `FleetMembers_CreateOrUpdate` | `INSERT` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` | A member contains a reference to an existing Kubernetes cluster. Creating a member makes the referenced cluster join the Fleet. |
| `FleetMembers_Delete` | `DELETE` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` | Deleting a Fleet member results in the member cluster leaving fleet. The Member azure resource is deleted upon success. The underlying cluster is not deleted. |
