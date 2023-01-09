---
title: collectionstatuses
hide_title: false
hide_table_of_contents: false
keywords:
  - collectionstatuses
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
<tr><td><b>Name</b></td><td><code>collectionstatuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.collectionstatuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required. The ID of the collection for which status is reported. |
| `creationDate` | `string` | Date on which the collection has been created in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format: Date, time, and offset, for example "2020-01-02T09:00:00+01:00" or "2020-01-02T09:00:00Z" |
| `destinationStatuses` | `array` | The intended destinations for the collection. |
| `lastUpdateDate` | `string` | Date on which the collection has been last updated in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format: Date, time, and offset, for example "2020-01-02T09:00:00+01:00" or "2020-01-02T09:00:00Z" |
| `collectionLevelIssuses` | `array` | A list of all issues associated with the collection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `collectionId, merchantId` | Gets the status of a collection from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the statuses of the collections in your Merchant Center account. |
