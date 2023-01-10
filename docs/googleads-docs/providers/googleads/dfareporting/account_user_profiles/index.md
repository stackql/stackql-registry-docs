---
title: account_user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - account_user_profiles
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
<tr><td><b>Name</b></td><td><code>account_user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.account_user_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the user profile. This is a read-only, auto-generated field. |
| `name` | `string` | Name of the user profile. This is a required field. Must be less than 64 characters long, must be globally unique, and cannot contain whitespace or any of the following characters: "&;&lt;&gt;"#%,". |
| `comments` | `string` | Comments for this user profile. |
| `locale` | `string` | Locale of the user profile. This is a required field. Acceptable values are: - "cs" (Czech) - "de" (German) - "en" (English) - "en-GB" (English United Kingdom) - "es" (Spanish) - "fr" (French) - "it" (Italian) - "ja" (Japanese) - "ko" (Korean) - "pl" (Polish) - "pt-BR" (Portuguese Brazil) - "ru" (Russian) - "sv" (Swedish) - "tr" (Turkish) - "zh-CN" (Chinese Simplified) - "zh-TW" (Chinese Traditional)  |
| `subaccountId` | `string` | Subaccount ID of the user profile. This is a read-only field that can be left blank. |
| `siteFilter` | `object` | Object Filter. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#accountUserProfile". |
| `accountId` | `string` | Account ID of the user profile. This is a read-only field that can be left blank. |
| `traffickerType` | `string` | Trafficker type of this user profile. This is a read-only field. |
| `userRoleId` | `string` | User role ID of the user profile. This is a required field. |
| `email` | `string` | Email of the user profile. The email addresss must be linked to a Google Account. This field is required on insertion and is read-only after insertion. |
| `active` | `boolean` | Whether this user profile is active. This defaults to false, and must be set true on insert for the user profile to be usable. |
| `userRoleFilter` | `object` | Object Filter. |
| `userAccessType` | `string` | User type of the user profile. This is a read-only field that can be left blank. |
| `campaignFilter` | `object` | Object Filter. |
| `advertiserFilter` | `object` | Object Filter. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accountUserProfiles_get` | `SELECT` | `id, profileId` | Gets one account user profile by ID. |
| `accountUserProfiles_list` | `SELECT` | `profileId` | Retrieves a list of account user profiles, possibly filtered. This method supports paging. |
| `accountUserProfiles_insert` | `EXEC` | `profileId` | Inserts a new account user profile. |
| `accountUserProfiles_patch` | `EXEC` | `id, profileId` | Updates an existing account user profile. This method supports patch semantics. |
| `accountUserProfiles_update` | `EXEC` | `profileId` | Updates an existing account user profile. |
