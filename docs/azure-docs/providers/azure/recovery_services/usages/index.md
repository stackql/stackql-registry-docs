---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - recovery_services
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The name of usage. |
| `nextResetTime` | `string` | Next reset time of usage. |
| `quotaPeriod` | `string` | Quota period of usage. |
| `unit` | `string` | Unit of the usage. |
| `currentValue` | `integer` | Current value of usage. |
| `limit` | `integer` | Limit of usage. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_ListByVaults` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` |
