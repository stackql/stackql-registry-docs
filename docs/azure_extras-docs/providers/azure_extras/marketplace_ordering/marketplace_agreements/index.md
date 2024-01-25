---
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - marketplace_ordering
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
<tr><td><b>Name</b></td><td><code>marketplace_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.marketplace_ordering.marketplace_agreements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Agreement Terms definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `offerId, offerType, planId, publisherId, subscriptionId` | Get marketplace terms. |
| `list` | `SELECT` | `subscriptionId` | List marketplace agreements in the subscription. |
| `create` | `INSERT` | `offerId, offerType, planId, publisherId, subscriptionId` | Save marketplace terms. |
| `_list` | `EXEC` | `subscriptionId` | List marketplace agreements in the subscription. |
| `cancel` | `EXEC` | `offerId, planId, publisherId, subscriptionId` | Cancel marketplace terms. |
| `sign` | `EXEC` | `offerId, planId, publisherId, subscriptionId` | Sign marketplace terms. |
