---
title: guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_agents
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
<tr><td><b>Name</b></td><td><code>guest_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.guest_agents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GuestAgents_Get` | `SELECT` | `api-version, name, resourceGroupName, subscriptionId, virtualMachineName` | Implements GuestAgent GET method. |
| `GuestAgents_ListByVm` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Returns the list of GuestAgent of the given vm. |
| `GuestAgents_Create` | `INSERT` | `api-version, name, resourceGroupName, subscriptionId, virtualMachineName, data__properties` | Create Or Update GuestAgent. |
| `GuestAgents_Delete` | `DELETE` | `api-version, name, resourceGroupName, subscriptionId, virtualMachineName` | Implements GuestAgent DELETE method. |
