---
title: account_permission_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - account_permission_groups
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
<tr><td><b>Name</b></td><td><code>account_permission_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.account_permission_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this account permission group. |
| `name` | `string` | Name of this account permission group. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#accountPermissionGroup". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accountPermissionGroups_get` | `SELECT` | `id, profileId` | Gets one account permission group by ID. |
| `accountPermissionGroups_list` | `SELECT` | `profileId` | Retrieves the list of account permission groups. |
