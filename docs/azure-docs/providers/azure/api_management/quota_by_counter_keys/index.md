---
title: quota_by_counter_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_by_counter_keys
  - api_management
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
<tr><td><b>Name</b></td><td><code>quota_by_counter_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.quota_by_counter_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `counterKey` | `string` | The Key value of the Counter. Must not be empty. |
| `periodEndTime` | `string` | The date of the end of Counter Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `periodKey` | `string` | Identifier of the Period for which the counter was collected. Must not be empty. |
| `periodStartTime` | `string` | The date of the start of Counter Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `value` | `object` | Quota counter value details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `QuotaByCounterKeys_ListByService` | `SELECT` | `quotaCounterKey, resourceGroupName, serviceName, subscriptionId` | Lists a collection of current quota counter periods associated with the counter-key configured in the policy on the specified service instance. The api does not support paging yet. |
| `QuotaByCounterKeys_Update` | `EXEC` | `quotaCounterKey, resourceGroupName, serviceName, subscriptionId` | Updates all the quota counter values specified with the existing quota counter key to a value in the specified service instance. This should be used for reset of the quota counter values. |
