---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.components</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `componentName, networkFunctionName, resourceGroupName, subscriptionId` | Gets information about the specified application instance resource. |
| `list_by_network_function` | `SELECT` | `networkFunctionName, resourceGroupName, subscriptionId` | Lists all the component resources in a network function. |
| `_list_by_network_function` | `EXEC` | `networkFunctionName, resourceGroupName, subscriptionId` | Lists all the component resources in a network function. |
