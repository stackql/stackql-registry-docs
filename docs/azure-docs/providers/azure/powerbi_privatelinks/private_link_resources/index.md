---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_privatelinks.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of a private link resource. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureResourceName, privateLinkResourceName, resourceGroupName, subscriptionId` | Get properties of a private link resource. |
| `list_by_resource` | `SELECT` | `azureResourceName, resourceGroupName, subscriptionId` | List private link resources under a specific Power BI resource. |
| `_list_by_resource` | `EXEC` | `azureResourceName, resourceGroupName, subscriptionId` | List private link resources under a specific Power BI resource. |
