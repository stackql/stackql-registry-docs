---
title: adds_service_members_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_service_members_credentials
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
<tr><td><b>Name</b></td><td><code>adds_service_members_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.adds_service_members_credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `credentialData` | `array` | The credential data. |
| `identifier` | `string` | The credential identifier. |
| `type` | `string` | The type of credential. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceMemberId, serviceName` |
| `_list` | `EXEC` | `serviceMemberId, serviceName` |
