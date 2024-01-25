---
title: iot_dps_resource_keys_for_key_name
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_keys_for_key_name
  - iot_hub_device_provisioning
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource_keys_for_key_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub_device_provisioning.iot_dps_resource_keys_for_key_name</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keyName` | `string` | Name of the key. |
| `primaryKey` | `string` | Primary SAS key value. |
| `rights` | `string` | Rights that this key has. |
| `secondaryKey` | `string` | Secondary SAS key value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, keyName, provisioningServiceName, resourceGroupName, subscriptionId` |
