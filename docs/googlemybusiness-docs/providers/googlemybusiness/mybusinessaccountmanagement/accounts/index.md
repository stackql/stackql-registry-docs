---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - mybusinessaccountmanagement
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessaccountmanagement.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name, in the format `accounts/&#123;account_id&#125;`. |
| `primaryOwner` | `string` | Required. Input only. The resource name of the account which will be the primary owner of the account being created. It should be of the form `accounts/&#123;account_id&#125;/`. |
| `verificationState` | `string` | Output only. If verified, future locations that are created are automatically connected to Google Maps, and have Google+ pages created, without requiring moderation. |
| `type` | `string` | Required. Contains the type of account. Accounts of type PERSONAL and ORGANIZATION cannot be created using this API. |
| `vettedState` | `string` | Output only. Indicates whether the account is vetted by Google. A vetted account is able to verify locations via the VETTED_PARTNER method. |
| `organizationInfo` | `object` | Additional information stored for an organization. |
| `permissionLevel` | `string` | Output only. Specifies the permission level the user has for this account. |
| `accountNumber` | `string` | Output only. Account reference number if provisioned. |
| `accountName` | `string` | Required. The name of the account. For an account of type `PERSONAL`, this is the first and last name of the user account. |
| `role` | `string` | Output only. Specifies the AccountRole of this account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountsId` | Gets the specified account. Returns `NOT_FOUND` if the account does not exist or if the caller does not have access rights to it. |
| `list` | `SELECT` |  | Lists all of the accounts for the authenticated user. This includes all accounts that the user owns, as well as any accounts for which the user has management rights. |
| `create` | `INSERT` |  | Creates an account with the specified name and type under the given parent. - Personal accounts and Organizations cannot be created. - User Groups cannot be created with a Personal account as primary owner. - Location Groups cannot be created with a primary owner of a Personal account if the Personal account is in an Organization. - Location Groups cannot own Location Groups. |
| `patch` | `EXEC` | `accountsId` | Updates the specified business account. Personal accounts cannot be updated using this method. |
