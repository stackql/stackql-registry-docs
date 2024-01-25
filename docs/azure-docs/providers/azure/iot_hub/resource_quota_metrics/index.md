---
title: resource_quota_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_quota_metrics
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>resource_quota_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_quota_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the quota metric. |
| `currentValue` | `integer` | The current value for the quota metric. |
| `maxValue` | `integer` | The maximum value of the quota metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` |
| `_get` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` |
