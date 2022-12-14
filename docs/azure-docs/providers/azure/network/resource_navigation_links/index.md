---
title: resource_navigation_links
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_navigation_links
  - network
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
<tr><td><b>Name</b></td><td><code>resource_navigation_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.resource_navigation_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Properties of ResourceNavigationLink. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ResourceNavigationLinks_List` | `SELECT` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` |
