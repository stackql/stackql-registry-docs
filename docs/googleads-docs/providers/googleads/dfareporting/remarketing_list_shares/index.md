---
title: remarketing_list_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - remarketing_list_shares
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
<tr><td><b>Name</b></td><td><code>remarketing_list_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.remarketing_list_shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#remarketingListShare". |
| `remarketingListId` | `string` | Remarketing list ID. This is a read-only, auto-generated field. |
| `sharedAccountIds` | `array` | Accounts that the remarketing list is shared with. |
| `sharedAdvertiserIds` | `array` | Advertisers that the remarketing list is shared with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `remarketingListShares_get` | `SELECT` | `profileId, remarketingListId` | Gets one remarketing list share by remarketing list ID. |
| `remarketingListShares_patch` | `EXEC` | `id, profileId` | Updates an existing remarketing list share. This method supports patch semantics. |
| `remarketingListShares_update` | `EXEC` | `profileId` | Updates an existing remarketing list share. |
