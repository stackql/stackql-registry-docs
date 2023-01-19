---
title: datafeedstatuses
hide_title: false
hide_table_of_contents: false
keywords:
  - datafeedstatuses
  - content
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
<tr><td><b>Name</b></td><td><code>datafeedstatuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.datafeedstatuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `datafeedId` | `string` | The ID of the feed for which the status is reported. |
| `warnings` | `array` | The list of errors occurring in the feed. |
| `itemsTotal` | `string` | The number of items in the feed that were processed. |
| `itemsValid` | `string` | The number of items in the feed that were valid. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#datafeedStatus`" |
| `language` | `string` | The two-letter ISO 639-1 language for which the status is reported. |
| `processingStatus` | `string` | The processing status of the feed. Acceptable values are: - "`"`failure`": The feed could not be processed or all items had errors.`" - "`in progress`": The feed is being processed. - "`none`": The feed has not yet been processed. For example, a feed that has never been uploaded will have this processing status. - "`success`": The feed was processed successfully, though some items might have had errors.  |
| `lastUploadDate` | `string` | The last date at which the feed was uploaded. |
| `errors` | `array` | The list of errors occurring in the feed. |
| `country` | `string` | The country for which the status is reported, represented as a CLDR territory code. |
| `feedLabel` | `string` | The feed label status is reported for. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datafeedId, merchantId` | Retrieves the status of a datafeed from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the statuses of the datafeeds in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Gets multiple Merchant Center datafeed statuses in a single request. |
