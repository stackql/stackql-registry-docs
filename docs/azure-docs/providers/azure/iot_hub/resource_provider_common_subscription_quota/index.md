---
title: resource_provider_common_subscription_quota
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_provider_common_subscription_quota
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
<tr><td><b>Name</b></td><td><code>resource_provider_common_subscription_quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_provider_common_subscription_quota</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | IotHub type id |
| `name` | `object` | Name of Iot Hub type |
| `currentValue` | `integer` | Current number of IotHub type |
| `limit` | `integer` | Numerical limit on IotHub type |
| `type` | `string` | Response type |
| `unit` | `string` | Unit of IotHub type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, subscriptionId` |
| `_get` | `EXEC` | `api-version, subscriptionId` |
