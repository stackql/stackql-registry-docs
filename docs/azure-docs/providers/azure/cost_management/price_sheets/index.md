---
title: price_sheets
hide_title: false
hide_table_of_contents: false
keywords:
  - price_sheets
  - cost_management
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>price_sheets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>price_sheets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.price_sheets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="download_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountId, billingPeriodName" /> | Generates the pricesheet for the provided billing period asynchronously based on the Enrollment ID. This is for Enterprise Agreement customers. 
 You can use the new 2023-09-01 API version at '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingPeriods/{billingPeriodName}/providers/Microsoft.CostManagement/pricesheets/default/download' for billing periods January 2023 onwards. With a new schema detailed below, the new price sheet provides more information and includes prices for Azure Reserved Instances (RI) for the current billing period.
 
 We recommend downloading an Azure Price Sheet for when entering a new billing period if you would maintain a record of past Azure Reserved Instance (RI) pricing. Due to Azure product growth, the Azure price sheet download experience in this preview version will be updated from a single .csv file to a zip file containing multiple csv files, each with max size of 75MB. |
| <CopyableCode code="download_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName" /> | Gets a URL to download the current month's pricesheet for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.
 
 You can use the new 2023-09-01 API version for billing periods January 2023 onwards. Azure Reserved Instance (RI) pricing is only available through the new version of the API. 
 
 Due to Azure product growth, the Azure price sheet download experience in this preview version will be updated from a single csv/json file to a Zip file containing multiple csv/json files, each with max size of 75MB. |
| <CopyableCode code="download_by_invoice" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceName" /> | Gets a URL to download the pricesheet for an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
