---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - lab_services
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
<tr><td><b>Name</b></td><td><code>operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.lab_services.operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `error` | `object` | The error detail. |
| `percentComplete` | `number` | Percent completion |
| `startTime` | `string` | Start time |
| `status` | `string` | The operation status |
| `endTime` | `string` | End time |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationResults_Get` | `SELECT` |  |
