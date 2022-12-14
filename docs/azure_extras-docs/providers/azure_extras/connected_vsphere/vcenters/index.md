---
title: vcenters
hide_title: false
hide_table_of_contents: false
keywords:
  - vcenters
  - connected_vsphere
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
<tr><td><b>Name</b></td><td><code>vcenters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.vcenters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `type` | `string` | Gets or sets the type of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | Gets or sets the location. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `properties` | `object` | Defines the resource properties. |
| `extendedLocation` | `object` | The extended location. |
| `tags` | `object` | Gets or sets the Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VCenters_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vcenterName` | Implements vCenter GET method. |
| `VCenters_List` | `SELECT` | `api-version, subscriptionId` | List of vCenters in a subscription. |
| `VCenters_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of vCenters in a resource group. |
| `VCenters_Create` | `INSERT` | `api-version, resourceGroupName, subscriptionId, vcenterName, data__location, data__properties` | Create Or Update vCenter. |
| `VCenters_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, vcenterName` | Implements vCenter DELETE method. |
| `VCenters_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vcenterName` | API to update certain properties of the vCenter resource. |
