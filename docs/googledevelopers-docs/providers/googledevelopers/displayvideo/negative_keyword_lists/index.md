---
title: negative_keyword_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - negative_keyword_lists
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>negative_keyword_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.negative_keyword_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the negative keyword list. |
| `negativeKeywordListId` | `string` | Output only. The unique ID of the negative keyword list. Assigned by the system. |
| `targetedLineItemCount` | `string` | Output only. Number of line items that are directly targeting this negative keyword list. |
| `advertiserId` | `string` | Output only. The unique ID of the advertiser the negative keyword list belongs to. |
| `displayName` | `string` | Required. The display name of the negative keyword list. Must be UTF-8 encoded with a maximum size of 255 bytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_negativeKeywordLists_get` | `SELECT` | `advertisersId, negativeKeywordListsId` | Gets a negative keyword list given an advertiser ID and a negative keyword list ID. |
| `advertisers_negativeKeywordLists_list` | `SELECT` | `advertisersId` | Lists negative keyword lists based on a given advertiser id. |
| `advertisers_negativeKeywordLists_create` | `INSERT` | `advertisersId` | Creates a new negative keyword list. Returns the newly created negative keyword list if successful. |
| `advertisers_negativeKeywordLists_delete` | `DELETE` | `advertisersId, negativeKeywordListsId` | Deletes a negative keyword list given an advertiser ID and a negative keyword list ID. |
| `advertisers_negativeKeywordLists_patch` | `EXEC` | `advertisersId, negativeKeywordListId` | Updates a negative keyword list. Returns the updated negative keyword list if successful. |
