---
title: adds_services_replication_status
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_replication_status
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>adds_services_replication_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.adds_services_replication_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `errorDcCount` | `integer` | The total number of domain controllers with error in a given forest. |
| `forestName` | `string` | The forest name. |
| `totalDcCount` | `integer` | The total number of domain controllers for a given forest. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `serviceName` |
