---
title: user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles
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
<tr><td><b>Name</b></td><td><code>user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.user_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `userName` | `string` | The user name. |
| `accountId` | `string` | The account ID to which this profile belongs. |
| `accountName` | `string` | The account name this profile belongs to. |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#userProfile". |
| `profileId` | `string` | The unique ID of the user profile. |
| `subAccountId` | `string` | The sub account ID this profile belongs to if applicable. |
| `subAccountName` | `string` | The sub account name this profile belongs to if applicable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `userProfiles_get` | `SELECT` | `profileId` | Gets one user profile by ID. |
| `userProfiles_list` | `SELECT` |  | Retrieves list of user profiles for a user. |
