---
title: hybrid_container_service
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_container_service
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>hybrid_container_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.hybrid_container_service</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridContainerService_ListOrchestrators` | `EXEC` | `customLocationResourceUri` | Lists the available orchestrators in a custom location for HybridAKS |
| `HybridContainerService_ListVMSkus` | `EXEC` | `customLocationResourceUri` | Lists the available VM SKUs in a custom location for HybridAKS |
