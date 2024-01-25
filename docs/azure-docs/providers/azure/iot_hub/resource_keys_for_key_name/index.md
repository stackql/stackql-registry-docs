---
title: resource_keys_for_key_name
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_keys_for_key_name
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
<tr><td><b>Name</b></td><td><code>resource_keys_for_key_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_keys_for_key_name</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keyName` | `string` | The name of the shared access policy. |
| `primaryKey` | `string` | The primary key. |
| `rights` | `string` | The permissions assigned to the shared access policy. |
| `secondaryKey` | `string` | The secondary key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, keyName, resourceGroupName, resourceName, subscriptionId` |
