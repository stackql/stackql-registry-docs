---
title: hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - hosts
  - connected_vsphere
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.connected_vsphere.hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `extendedLocation` | `object` | The extended location. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Describes the properties of a Host. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, hostName, resourceGroupName, subscriptionId` | Implements host GET method. |
| `list` | `SELECT` | `api-version, subscriptionId` | List of hosts in a subscription. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of hosts in a resource group. |
| `create` | `INSERT` | `api-version, hostName, resourceGroupName, subscriptionId, data__location, data__properties` | Create Or Update host. |
| `delete` | `DELETE` | `api-version, hostName, resourceGroupName, subscriptionId` | Implements host DELETE method. |
| `_list` | `EXEC` | `api-version, subscriptionId` | List of hosts in a subscription. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List of hosts in a resource group. |
| `update` | `EXEC` | `api-version, hostName, resourceGroupName, subscriptionId` | API to update certain properties of the host resource. |
