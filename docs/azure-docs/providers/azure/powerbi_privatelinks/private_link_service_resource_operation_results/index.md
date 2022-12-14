---
title: private_link_service_resource_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_service_resource_operation_results
  - powerbi_privatelinks
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
<tr><td><b>Name</b></td><td><code>private_link_service_resource_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_privatelinks.private_link_service_resource_operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The operation id. |
| `name` | `string` | The operation name. |
| `error` | `object` | The error detail. |
| `startTime` | `string` | The operation start time. |
| `status` | `string` | The operation status. |
| `endTime` | `string` | The operation end time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkServiceResourceOperationResults_Get` | `SELECT` | `operationId, subscriptionId` |
