---
title: service_members_service_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_service_configuration
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
<tr><td><b>Name</b></td><td><code>service_members_service_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.service_members_service_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `serviceAccount` | `string` | The service account. |
| `serviceType` | `integer` | The service type of the server. |
| `sqlDatabaseName` | `string` | The SQL database. |
| `sqlDatabaseSize` | `integer` | The SQL database size. |
| `sqlEdition` | `string` | The SQL edition |
| `sqlInstance` | `string` | The SQL instance details. |
| `sqlServer` | `string` | The SQL server information. |
| `sqlVersion` | `string` | The SQL version. |
| `version` | `string` | The version of the sync service. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `serviceMemberId, serviceName` |
