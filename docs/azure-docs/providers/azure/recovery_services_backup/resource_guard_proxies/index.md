---
title: resource_guard_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guard_proxies
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>resource_guard_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.resource_guard_proxies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The uri to fetch the next page of resources. Call ListNext() fetches next page of resources. |
| `value` | `array` | List of resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ResourceGuardProxies_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` |
