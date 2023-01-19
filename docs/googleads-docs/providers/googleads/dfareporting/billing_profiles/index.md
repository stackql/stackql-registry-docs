---
title: billing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_profiles
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.billing_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this billing profile. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this billing profile. This is a required field and must be less than 256 characters long and must be unique among billing profile in the same account. |
| `paymentsAccountId` | `string` | The ID of the payment account the billing profile belongs to. This is a read-only field. |
| `status` | `string` | Status of this billing profile.This is a read-only field. |
| `purchaseOrder` | `string` | Purchase order (PO) for this billing profile. This PO number is used in the invoices for all of the advertisers in this billing profile. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#billingProfile". |
| `countryCode` | `string` | Country code of this billing profile.This is a read-only field. |
| `currencyCode` | `string` | Billing currency code in ISO 4217 format.This is a read-only field. |
| `invoiceLevel` | `string` | Invoice level for this billing profile. Used to group fees into separate invoices by account, advertiser, or campaign. |
| `secondaryPaymentsCustomerId` | `string` | The ID of the secondary payment customer the billing profile belongs to. This is a read-only field. |
| `paymentsCustomerId` | `string` | The ID of the payment customer the billing profile belongs to. This is a read-only field. |
| `isDefault` | `boolean` | True if the billing profile is the account default profile. This is a read-only field. |
| `consolidatedInvoice` | `boolean` | Consolidated invoice option for this billing profile. Used to get a single, consolidated invoice across the chosen invoice level. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingProfiles_get` | `SELECT` | `id, profileId` | Gets one billing profile by ID. |
| `billingProfiles_list` | `SELECT` | `profileId` | Retrieves a list of billing profiles, possibly filtered. This method supports paging. |
| `billingProfiles_update` | `EXEC` | `profileId` | Updates an existing billing profile. |
