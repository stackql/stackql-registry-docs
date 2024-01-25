---
title: adds_services_forest_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_forest_summary
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
<tr><td><b>Name</b></td><td><code>adds_services_forest_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.adds_services_forest_summary</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `domainCount` | `integer` | The domain count. |
| `domains` | `array` | The list of domain controller names. |
| `forestName` | `string` | The forest name. |
| `monitoredDcCount` | `integer` | The number of domain controllers that are monitored by Azure Active Directory Connect Health. |
| `siteCount` | `integer` | The site count. |
| `sites` | `array` | The list of site names. |
| `totalDcCount` | `integer` | The total domain controllers. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `serviceName` |
