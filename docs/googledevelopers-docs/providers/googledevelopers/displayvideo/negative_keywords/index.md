---
title: negative_keywords
hide_title: false
hide_table_of_contents: false
keywords:
  - negative_keywords
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
<tr><td><b>Name</b></td><td><code>negative_keywords</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.negative_keywords</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `negativeKeywords` | `array` | The list of negative keywords. This list will be absent if empty. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the page_token field in the subsequent call to `ListNegativeKeywords` method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_negativeKeywordLists_negativeKeywords_list` | `SELECT` | `advertisersId, negativeKeywordListsId` | Lists negative keywords in a negative keyword list. |
| `advertisers_negativeKeywordLists_negativeKeywords_create` | `INSERT` | `advertiserId, negativeKeywordListsId` | Creates a negative keyword in a negative keyword list. |
| `advertisers_negativeKeywordLists_negativeKeywords_delete` | `DELETE` | `advertiserId, negativeKeywordListsId, negativeKeywordsId` | Deletes a negative keyword from a negative keyword list. |
| `advertisers_negativeKeywordLists_negativeKeywords_bulkEdit` | `EXEC` | `advertiserId, negativeKeywordListsId` | Bulk edits negative keywords in a single negative keyword list. The operation will delete the negative keywords provided in BulkEditNegativeKeywordsRequest.deleted_negative_keywords and then create the negative keywords provided in BulkEditNegativeKeywordsRequest.created_negative_keywords. This operation is guaranteed to be atomic and will never result in a partial success or partial failure. |
| `advertisers_negativeKeywordLists_negativeKeywords_replace` | `EXEC` | `advertiserId, negativeKeywordListsId` | Replaces all negative keywords in a single negative keyword list. The operation will replace the keywords in a negative keyword list with keywords provided in ReplaceNegativeKeywordsRequest.new_negative_keywords. |
