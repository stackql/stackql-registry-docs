---
title: fetch_cross_region_restore_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - fetch_cross_region_restore_jobs
  - data_protection
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
<tr><td><b>Name</b></td><td><code>fetch_cross_region_restore_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.fetch_cross_region_restore_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The uri to fetch the next page of resources. Call ListNext() fetches next page of resources. |
| `value` | `array` | List of resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId, data__sourceBackupVaultId, data__sourceRegion` |
