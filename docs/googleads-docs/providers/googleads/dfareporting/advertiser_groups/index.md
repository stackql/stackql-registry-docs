---
title: advertiser_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - advertiser_groups
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
<tr><td><b>Name</b></td><td><code>advertiser_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.advertiser_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this advertiser group. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this advertiser group. This is a required field and must be less than 256 characters long and unique among advertiser groups of the same account. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#advertiserGroup". |
| `accountId` | `string` | Account ID of this advertiser group. This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertiserGroups_get` | `SELECT` | `id, profileId` | Gets one advertiser group by ID. |
| `advertiserGroups_list` | `SELECT` | `profileId` | Retrieves a list of advertiser groups, possibly filtered. This method supports paging. |
| `advertiserGroups_delete` | `DELETE` | `id, profileId` | Deletes an existing advertiser group. |
| `advertiserGroups_insert` | `EXEC` | `profileId` | Inserts a new advertiser group. |
| `advertiserGroups_patch` | `EXEC` | `id, profileId` | Updates an existing advertiser group. This method supports patch semantics. |
| `advertiserGroups_update` | `EXEC` | `profileId` | Updates an existing advertiser group. |
