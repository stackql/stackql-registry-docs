---
title: hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - hosts
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
<tr><td><b>Name</b></td><td><code>hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `location` | `string` | Gets or sets the location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | Defines the resource properties. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `type` | `string` | Gets or sets the type of the resource. |
| `extendedLocation` | `object` | The extended location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Hosts_Get` | `SELECT` | `api-version, hostName, resourceGroupName, subscriptionId` | Implements host GET method. |
| `Hosts_List` | `SELECT` | `api-version, subscriptionId` | List of hosts in a subscription. |
| `Hosts_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of hosts in a resource group. |
| `Hosts_Create` | `INSERT` | `api-version, hostName, resourceGroupName, subscriptionId, data__location, data__properties` | Create Or Update host. |
| `Hosts_Delete` | `DELETE` | `api-version, hostName, resourceGroupName, subscriptionId` | Implements host DELETE method. |
| `Hosts_Update` | `EXEC` | `api-version, hostName, resourceGroupName, subscriptionId` | API to update certain properties of the host resource. |
