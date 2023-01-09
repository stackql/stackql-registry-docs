---
title: creative_fields
hide_title: false
hide_table_of_contents: false
keywords:
  - creative_fields
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
<tr><td><b>Name</b></td><td><code>creative_fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.creative_fields</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this creative field. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this creative field. This is a required field and must be less than 256 characters long and unique among creative fields of the same advertiser. |
| `advertiserId` | `string` | Advertiser ID of this creative field. This is a required field on insertion. |
| `advertiserIdDimensionValue` | `object` | Represents a DimensionValue resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#creativeField". |
| `subaccountId` | `string` | Subaccount ID of this creative field. This is a read-only field that can be left blank. |
| `accountId` | `string` | Account ID of this creative field. This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `creativeFields_get` | `SELECT` | `id, profileId` | Gets one creative field by ID. |
| `creativeFields_list` | `SELECT` | `profileId` | Retrieves a list of creative fields, possibly filtered. This method supports paging. |
| `creativeFields_delete` | `DELETE` | `id, profileId` | Deletes an existing creative field. |
| `creativeFields_insert` | `EXEC` | `profileId` | Inserts a new creative field. |
| `creativeFields_patch` | `EXEC` | `id, profileId` | Updates an existing creative field. This method supports patch semantics. |
| `creativeFields_update` | `EXEC` | `profileId` | Updates an existing creative field. |
