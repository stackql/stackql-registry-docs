---
title: locations_capability
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_capability
  - data_lake_analytics
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
<tr><td><b>Name</b></td><td><code>locations_capability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_analytics.locations_capability</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountCount` | `integer` | The current number of accounts under this subscription. |
| `maxAccountCount` | `integer` | The maximum supported number of accounts under this subscription. |
| `migrationState` | `boolean` | The Boolean value of true or false to indicate the maintenance state. |
| `state` | `string` | The subscription state. |
| `subscriptionId` | `string` | The subscription credentials that uniquely identifies the subscription. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `location, subscriptionId` |
