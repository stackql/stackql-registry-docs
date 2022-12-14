---
title: private_link_scoped_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scoped_resources
  - monitor
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
<tr><td><b>Name</b></td><td><code>private_link_scoped_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.private_link_scoped_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a private link scoped resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkScopedResources_Get` | `SELECT` | `name, resourceGroupName, scopeName, subscriptionId` | Gets a scoped resource in a private link scope. |
| `PrivateLinkScopedResources_ListByPrivateLinkScope` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` | Gets all private endpoint connections on a private link scope. |
| `PrivateLinkScopedResources_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, scopeName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `PrivateLinkScopedResources_Delete` | `DELETE` | `name, resourceGroupName, scopeName, subscriptionId` | Deletes a private endpoint connection with a given name. |
