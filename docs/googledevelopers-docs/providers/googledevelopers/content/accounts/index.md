---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required. 64-bit Merchant Center account ID. |
| `name` | `string` | Required. Display name for the account. |
| `automaticImprovements` | `object` | The automatic improvements of the account can be used to automatically update items, improve images and shipping. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#account`". |
| `accountManagement` | `string` | Output only. How the account is managed. Acceptable values are: - "`manual`" - "`automatic`"  |
| `adsLinks` | `array` | Linked Ads accounts that are active or pending approval. To create a new link request, add a new link with status `active` to the list. It will remain in a `pending` state until approved or rejected either in the Ads interface or through the AdWords API. To delete an active link, or to cancel a link request, remove it from the list. |
| `businessInformation` | `object` |  |
| `youtubeChannelLinks` | `array` | Linked YouTube channels that are active or pending approval. To create a new link request, add a new link with status `active` to the list. It will remain in a `pending` state until approved or rejected in the YT Creator Studio interface. To delete an active link, or to cancel a link request, remove it from the list. |
| `sellerId` | `string` | Client-specific, locally-unique, internal ID for the child account. |
| `adultContent` | `boolean` | Indicates whether the merchant sells adult content. |
| `labelIds` | `array` | Manually created label IDs that are assigned to the account by CSS. |
| `googleMyBusinessLink` | `object` |  |
| `websiteUrl` | `string` | The merchant's website. |
| `cssId` | `string` | ID of CSS the account belongs to. |
| `automaticLabelIds` | `array` | Automatically created label IDs that are assigned to the account by CSS Center. |
| `users` | `array` | Users with access to the account. Every account (except for subaccounts) must have at least one admin user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves a Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the sub-accounts in your Merchant Center account. |
| `insert` | `INSERT` | `merchantId` | Creates a Merchant Center sub-account. |
| `delete` | `DELETE` | `accountId, merchantId` | Deletes a Merchant Center sub-account. |
| `authinfo` | `EXEC` |  | Returns information about the authenticated user. |
| `claimwebsite` | `EXEC` | `accountId, merchantId` | Claims the website of a Merchant Center sub-account. |
| `custombatch` | `EXEC` |  | Retrieves, inserts, updates, and deletes multiple Merchant Center (sub-)accounts in a single request. |
| `link` | `EXEC` | `accountId, merchantId` | Performs an action on a link between two Merchant Center accounts, namely accountId and linkedAccountId. |
| `requestphoneverification` | `EXEC` | `accountId, merchantId` | Request verification code to start phone verification. |
| `update` | `EXEC` | `accountId, merchantId` | Updates a Merchant Center account. Any fields that are not provided are deleted from the resource. |
| `updatelabels` | `EXEC` | `accountId, merchantId` | Updates labels that are assigned to the Merchant Center account by CSS user. |
| `verifyphonenumber` | `EXEC` | `accountId, merchantId` | Validates verification code to verify phone number for the account. If successful this will overwrite the value of `accounts.businessinformation.phoneNumber`. Only verified phone number will replace an existing verified phone number. |
