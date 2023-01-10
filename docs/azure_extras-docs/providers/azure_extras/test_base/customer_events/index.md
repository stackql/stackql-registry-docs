---
title: customer_events
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_events
  - test_base
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
<tr><td><b>Name</b></td><td><code>customer_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.customer_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A notification events subscribed to be received by customer. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomerEvents_Get` | `SELECT` | `customerEventName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a Test Base CustomerEvent. |
| `CustomerEvents_ListByTestBaseAccount` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all notification events subscribed under a Test Base Account. |
| `CustomerEvents_Create` | `INSERT` | `customerEventName, resourceGroupName, subscriptionId, testBaseAccountName` | Create or replace a Test Base Customer Event. |
| `CustomerEvents_Delete` | `DELETE` | `customerEventName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a Test Base Customer Event. |
