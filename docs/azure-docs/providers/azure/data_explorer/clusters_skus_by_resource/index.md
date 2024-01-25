---
title: clusters_skus_by_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_skus_by_resource
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>clusters_skus_by_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.clusters_skus_by_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | Azure capacity definition. |
| `resourceType` | `string` | Resource Namespace and Type. |
| `sku` | `object` | Azure SKU definition. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` |
