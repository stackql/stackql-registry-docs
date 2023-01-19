---
title: advertiser_invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - advertiser_invoices
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
<tr><td><b>Name</b></td><td><code>advertiser_invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.advertiser_invoices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Pagination token to be used for the next list operation. |
| `invoices` | `array` | Invoice collection |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#advertiserInvoicesListResponse". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `advertiserInvoices_list` | `SELECT` | `advertiserId, profileId` |
