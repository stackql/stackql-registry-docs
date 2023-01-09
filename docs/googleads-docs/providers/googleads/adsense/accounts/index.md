---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - adsense
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the account. Format: accounts/pub-[0-9]+ |
| `displayName` | `string` | Output only. Display name of this account. |
| `pendingTasks` | `array` | Output only. Outstanding tasks that need to be completed as part of the sign-up process for a new account. e.g. "billing-profile-creation", "phone-pin-verification". |
| `premium` | `boolean` | Output only. Whether this account is premium. |
| `state` | `string` | Output only. State of the account. |
| `timeZone` | `object` | Represents a time zone from the [IANA Time Zone Database](https://www.iana.org/time-zones). |
| `createTime` | `string` | Output only. Creation time of the account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountsId` | Gets information about the selected AdSense account. |
| `list` | `SELECT` |  | Lists all accounts available to this user. |
