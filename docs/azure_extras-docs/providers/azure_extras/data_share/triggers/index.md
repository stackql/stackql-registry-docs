---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - data_share
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `kind` | `string` | Kind of synchronization on trigger. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Triggers_Get` | `SELECT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, triggerName` | Get a Trigger in a shareSubscription |
| `Triggers_ListByShareSubscription` | `SELECT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | List Triggers in a share subscription |
| `Triggers_Create` | `INSERT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, triggerName, data__kind` | Create a Trigger  |
| `Triggers_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId, triggerName` | Delete a Trigger in a shareSubscription |
