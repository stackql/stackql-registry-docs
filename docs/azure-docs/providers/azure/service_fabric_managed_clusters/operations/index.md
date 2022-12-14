---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the operation. |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
| `nextLink` | `string` | The URL to use for getting the next set of results. |
| `origin` | `string` | Origin result |
| `display` | `object` | Operation supported by the Service Fabric resource provider |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` | `api-version` |
