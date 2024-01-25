---
title: accounts_invoice_sections_by_create_subscription_permission
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_invoice_sections_by_create_subscription_permission
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
<tr><td><b>Name</b></td><td><code>accounts_invoice_sections_by_create_subscription_permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.accounts_invoice_sections_by_create_subscription_permission</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The link (url) to the next page of results. |
| `value` | `array` | The list of invoice section properties with create subscription permission. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `billingAccountName` |
