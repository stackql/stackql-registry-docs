---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Policies_GetByBillingProfile` | `EXEC` | `billingAccountName, billingProfileName` | Lists the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Policies_GetByCustomer` | `EXEC` | `billingAccountName, customerName` | Lists the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| `Policies_Update` | `EXEC` | `billingAccountName, billingProfileName` | Updates the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Policies_UpdateCustomer` | `EXEC` | `billingAccountName, customerName` | Updates the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
