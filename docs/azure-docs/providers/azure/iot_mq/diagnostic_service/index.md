---
title: diagnostic_service
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_service
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>diagnostic_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.diagnostic_service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MQ Diagnostic Services Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diagnosticServiceName, mqName, resourceGroupName, subscriptionId` | Get a DiagnosticServiceResource |
| `list_by_mq_resource` | `SELECT` | `mqName, resourceGroupName, subscriptionId` | List DiagnosticServiceResource resources by MqResource |
| `create_or_update` | `INSERT` | `diagnosticServiceName, mqName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a DiagnosticServiceResource |
| `delete` | `DELETE` | `diagnosticServiceName, mqName, resourceGroupName, subscriptionId` | Delete a DiagnosticServiceResource |
| `_list_by_mq_resource` | `EXEC` | `mqName, resourceGroupName, subscriptionId` | List DiagnosticServiceResource resources by MqResource |
| `update` | `EXEC` | `diagnosticServiceName, mqName, resourceGroupName, subscriptionId` | Update a DiagnosticServiceResource |
