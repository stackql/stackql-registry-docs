---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - fleet
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.fleet.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| `properties` | `object` | A member of the Fleet. It contains a reference to an existing Kubernetes cluster on Azure. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` | Get a FleetMember |
| `list_by_fleet` | `SELECT` | `fleetName, resourceGroupName, subscriptionId` | List FleetMember resources by Fleet |
| `create` | `INSERT` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` | Create a FleetMember |
| `delete` | `DELETE` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` | Delete a FleetMember |
| `_list_by_fleet` | `EXEC` | `fleetName, resourceGroupName, subscriptionId` | List FleetMember resources by Fleet |
| `update` | `EXEC` | `fleetMemberName, fleetName, resourceGroupName, subscriptionId` | Update a FleetMember |
