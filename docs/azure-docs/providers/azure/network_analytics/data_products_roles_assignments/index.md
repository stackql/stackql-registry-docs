---
title: data_products_roles_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products_roles_assignments
  - network_analytics
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
<tr><td><b>Name</b></td><td><code>data_products_roles_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_analytics.data_products_roles_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `count` | `integer` | Count of role assignments. |
| `roleAssignmentResponse` | `array` | list of role assignments |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `dataProductName, resourceGroupName, subscriptionId` |
