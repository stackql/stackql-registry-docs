---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - analyticsadmin
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of this account. Format: accounts/&#123;account&#125; Example: "accounts/100" |
| `displayName` | `string` | Required. Human-readable display name for this account. |
| `regionCode` | `string` | Country of business. Must be a Unicode CLDR region code. |
| `updateTime` | `string` | Output only. Time when account payload fields were last updated. |
| `createTime` | `string` | Output only. Time when this account was originally created. |
| `deleted` | `boolean` | Output only. Indicates whether this Account is soft-deleted or not. Deleted accounts are excluded from List results unless specifically requested. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountsId` | Lookup for a single Account. |
| `list` | `SELECT` |  | Returns all accounts accessible by the caller. Note that these accounts might not currently have GA4 properties. Soft-deleted (ie: "trashed") accounts are excluded by default. Returns an empty list if no relevant accounts are found. |
| `delete` | `DELETE` | `accountsId` | Marks target Account as soft-deleted (ie: "trashed") and returns it. This API does not have a method to restore soft-deleted accounts. However, they can be restored using the Trash Can UI. If the accounts are not restored before the expiration time, the account and all child resources (eg: Properties, GoogleAdsLinks, Streams, UserLinks) will be permanently purged. https://support.google.com/analytics/answer/6154772 Returns an error if the target is not found. |
| `patch` | `EXEC` | `accountsId` | Updates an account. |
| `provisionAccountTicket` | `EXEC` |  | Requests a ticket for creating an account. |
| `searchChangeHistoryEvents` | `EXEC` | `accountsId` | Searches through all changes to an account or its children given the specified set of filters. |
