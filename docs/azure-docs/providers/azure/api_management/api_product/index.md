---
title: api_product
hide_title: false
hide_table_of_contents: false
keywords:
  - api_product
  - api_management
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
<tr><td><b>Name</b></td><td><code>api_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_product</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_apis` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` |
| `_list_by_apis` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` |
