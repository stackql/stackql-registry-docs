---
title: region
hide_title: false
hide_table_of_contents: false
keywords:
  - region
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
<tr><td><b>Name</b></td><td><code>region</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.region</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Region name. |
| `isDeleted` | `boolean` | whether Region is deleted. |
| `isMasterRegion` | `boolean` | whether Region is the master region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Region_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
