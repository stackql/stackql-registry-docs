---
title: resource_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_stats
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
<tr><td><b>Name</b></td><td><code>resource_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_stats</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `disabledDeviceCount` | `integer` | The count of disabled devices in the identity registry. |
| `enabledDeviceCount` | `integer` | The count of enabled devices in the identity registry. |
| `totalDeviceCount` | `integer` | The total count of devices in the identity registry. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` |
