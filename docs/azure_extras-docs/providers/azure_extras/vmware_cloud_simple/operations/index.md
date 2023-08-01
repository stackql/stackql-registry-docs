---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - vmware_cloud_simple
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Operation Id |
| `name` | `string` | Operation ID |
| `error` | `object` | Operation error model |
| `startTime` | `string` | Start time of the operation |
| `status` | `string` | Operation status |
| `endTime` | `string` | End time of the operation |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Operations_Get` | `SELECT` | `Referer, api-version, operationId, regionId, subscriptionId` | Return an async operation |
| `Operations_List` | `SELECT` | `api-version` | Return list of operations |
