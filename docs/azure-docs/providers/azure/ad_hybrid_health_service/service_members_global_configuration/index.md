---
title: service_members_global_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_global_configuration
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
<tr><td><b>Name</b></td><td><code>service_members_global_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.service_members_global_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `featureSet` | `array` | The list of additional feature sets. |
| `numSavedPwdEvent` | `integer` | The number of saved password events. |
| `passwordSyncEnabled` | `boolean` | Indicates if password sync is enabled or not. |
| `schemaXml` | `string` | The schema for the configuration. |
| `version` | `integer` | The version for the global configuration. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceMemberId, serviceName` |
| `_list` | `EXEC` | `serviceMemberId, serviceName` |
