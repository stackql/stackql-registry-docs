---
title: monitors_default_key
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_default_key
  - datadog
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_default_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.datadog.monitors_default_key</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the API key. |
| `created` | `string` | The time of creation of the API key. |
| `createdBy` | `string` | The user that created the API key. |
| `key` | `string` | The value of the API key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
