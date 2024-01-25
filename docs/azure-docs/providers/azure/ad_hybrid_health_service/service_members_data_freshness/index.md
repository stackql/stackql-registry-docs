---
title: service_members_data_freshness
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_data_freshness
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
<tr><td><b>Name</b></td><td><code>service_members_data_freshness</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.service_members_data_freshness</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `key` | `string` | The key for the property. |
| `value` | `string` | The value for the key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceMemberId, serviceName` |
| `_list` | `EXEC` | `serviceMemberId, serviceName` |
