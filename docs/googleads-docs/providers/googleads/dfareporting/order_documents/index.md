---
title: order_documents
hide_title: false
hide_table_of_contents: false
keywords:
  - order_documents
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
<tr><td><b>Name</b></td><td><code>order_documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.order_documents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this order document. |
| `lastSentRecipients` | `array` | List of email addresses that received the last sent document. |
| `orderId` | `string` | ID of the order from which this order document is created. |
| `cancelled` | `boolean` | Whether this order document is cancelled. |
| `approvedByUserProfileIds` | `array` | IDs of users who have approved this order document. |
| `type` | `string` | Type of this order document |
| `createdInfo` | `object` | Modification timestamp. |
| `accountId` | `string` | Account ID of this order document. |
| `title` | `string` | Title of this order document. |
| `lastSentTime` | `string` |  |
| `effectiveDate` | `string` |  |
| `advertiserId` | `string` | Advertiser ID of this order document. |
| `amendedOrderDocumentId` | `string` | The amended order document ID of this order document. An order document can be created by optionally amending another order document so that the change history can be preserved. |
| `projectId` | `string` | Project ID of this order document. |
| `subaccountId` | `string` | Subaccount ID of this order document. |
| `signed` | `boolean` | Whether this order document has been signed. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#orderDocument". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `orderDocuments_get` | `SELECT` | `id, profileId, projectId` | Gets one order document by ID. |
| `orderDocuments_list` | `SELECT` | `profileId, projectId` | Retrieves a list of order documents, possibly filtered. This method supports paging. |
