---
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
  - billing
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
<tr><td><b>Name</b></td><td><code>reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the reservation. |
| `name` | `string` | The name of the reservation. |
| `sku` | `object` | The property of reservation sku object. |
| `type` | `string` | The type of the reservation. |
| `location` | `string` | The location of the reservation. |
| `properties` | `object` | The property of reservation object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Reservations_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the reservations for a billing account and the roll up counts of reservations group by provisioning states. |
| `Reservations_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the reservations for a billing profile and the roll up counts of reservations group by provisioning state. |
