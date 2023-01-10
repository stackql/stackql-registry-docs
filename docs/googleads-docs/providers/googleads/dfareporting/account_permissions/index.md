---
title: account_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - account_permissions
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
<tr><td><b>Name</b></td><td><code>account_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.account_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this account permission. |
| `name` | `string` | Name of this account permission. |
| `accountProfiles` | `array` | Account profiles associated with this account permission. Possible values are: - "ACCOUNT_PROFILE_BASIC" - "ACCOUNT_PROFILE_STANDARD"  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#accountPermission". |
| `level` | `string` | Administrative level required to enable this account permission. |
| `permissionGroupId` | `string` | Permission group of this account permission. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accountPermissions_get` | `SELECT` | `id, profileId` | Gets one account permission by ID. |
| `accountPermissions_list` | `SELECT` | `profileId` | Retrieves the list of account permissions. |
