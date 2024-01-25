---
title: price_sheet
hide_title: false
hide_table_of_contents: false
keywords:
  - price_sheet
  - cost_management
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
<tr><td><b>Name</b></td><td><code>price_sheet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.price_sheet</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `download_by_billing_account` | `EXEC` | `billingAccountId, billingPeriodName` | Generates the pricesheet for the provided billing period asynchronously based on the Enrollment ID. This is for Enterprise Agreement customers. <br /> You can use the new 2023-09-01 API version at '/providers/Microsoft.Billing/billingAccounts/&#123;billingAccountId&#125;/billingPeriods/&#123;billingPeriodName&#125;/providers/Microsoft.CostManagement/pricesheets/default/download' for billing periods January 2023 onwards. With a new schema detailed below, the new price sheet provides more information and includes prices for Azure Reserved Instances (RI) for the current billing period.<br /> <br /> We recommend downloading an Azure Price Sheet for when entering a new billing period if you would maintain a record of past Azure Reserved Instance (RI) pricing. Due to Azure product growth, the Azure price sheet download experience in this preview version will be updated from a single .csv file to a zip file containing multiple csv files, each with max size of 75MB. |
| `download_by_billing_profile` | `EXEC` | `billingAccountName, billingProfileName` | Gets a URL to download the current month's pricesheet for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.<br /> <br /> You can use the new 2023-09-01 API version for billing periods January 2023 onwards. Azure Reserved Instance (RI) pricing is only available through the new version of the API. <br /> <br /> Due to Azure product growth, the Azure price sheet download experience in this preview version will be updated from a single csv/json file to a Zip file containing multiple csv/json files, each with max size of 75MB. |
| `download_by_invoice` | `EXEC` | `billingAccountName, billingProfileName, invoiceName` | Gets a URL to download the pricesheet for an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
