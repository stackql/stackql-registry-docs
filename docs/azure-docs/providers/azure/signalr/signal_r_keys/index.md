---
title: signal_r_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_keys
  - signalr
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
<tr><td><b>Name</b></td><td><code>signal_r_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.signalr.signal_r_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `primaryConnectionString` | `string` | Connection string constructed via the primaryKey |
| `primaryKey` | `string` | The primary access key. |
| `secondaryConnectionString` | `string` | Connection string constructed via the secondaryKey |
| `secondaryKey` | `string` | The secondary access key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
