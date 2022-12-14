---
title: power_bi_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - power_bi_resources
  - powerbi_privatelinks
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
<tr><td><b>Name</b></td><td><code>power_bi_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_privatelinks.power_bi_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource identifier of the resource. |
| `name` | `string` | Specifies the name of the resource. |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Specifies the tags of the resource. |
| `type` | `string` | Specifies the type of the resource. |
| `location` | `string` | Specifies the location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PowerBIResources_ListByResourceName` | `SELECT` | `azureResourceName, resourceGroupName, subscriptionId` | Gets all the private link resources for the given Azure resource. |
| `PowerBIResources_Create` | `INSERT` | `azureResourceName, resourceGroupName, subscriptionId` | Creates or updates a Private Link Service Resource for Power BI. |
| `PowerBIResources_Delete` | `DELETE` | `azureResourceName, resourceGroupName, subscriptionId` | Deletes a Private Link Service Resource for Power BI. |
| `PowerBIResources_Update` | `EXEC` | `azureResourceName, resourceGroupName, subscriptionId` | Creates or updates a Private Link Service Resource for Power BI. |
