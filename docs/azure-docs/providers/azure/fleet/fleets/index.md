---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
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
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.fleet.fleets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Fleet properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fleetName, resourceGroupName, subscriptionId` | Gets a Fleet. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists fleets in the specified subscription and resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists fleets in the specified subscription. |
| `create_or_update` | `INSERT` | `fleetName, resourceGroupName, subscriptionId` | Creates or updates a Fleet. |
| `delete` | `DELETE` | `fleetName, resourceGroupName, subscriptionId` | Delete a Fleet |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists fleets in the specified subscription and resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists fleets in the specified subscription. |
| `update` | `EXEC` | `fleetName, resourceGroupName, subscriptionId` | Update a Fleet |
