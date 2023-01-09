---
title: datafeeds
hide_title: false
hide_table_of_contents: false
keywords:
  - datafeeds
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
<tr><td><b>Name</b></td><td><code>datafeeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.datafeeds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Required for update. The ID of the data feed. |
| `name` | `string` | Required for insert. A descriptive name of the data feed. |
| `format` | `object` |  |
| `targets` | `array` | The targets this feed should apply to (country, language, destinations). |
| `attributeLanguage` | `string` | The two-letter ISO 639-1 language in which the attributes are defined in the data feed. |
| `contentType` | `string` | Required. The type of data feed. For product inventory feeds, only feeds for local stores, not online stores, are supported. Acceptable values are: - "`local products`" - "`product inventory`" - "`products`"  |
| `fileName` | `string` | Required. The filename of the feed. All feeds must have a unique file name. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#datafeed`" |
| `fetchSchedule` | `object` | The required fields vary based on the frequency of fetching. For a monthly fetch schedule, day_of_month and hour are required. For a weekly fetch schedule, weekday and hour are required. For a daily fetch schedule, only hour is required. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datafeedId, merchantId` | Retrieves a datafeed configuration from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the configurations for datafeeds in your Merchant Center account. |
| `insert` | `INSERT` | `merchantId` | Registers a datafeed configuration with your Merchant Center account. |
| `delete` | `DELETE` | `datafeedId, merchantId` | Deletes a datafeed configuration from your Merchant Center account. |
| `custombatch` | `EXEC` |  | Deletes, fetches, gets, inserts and updates multiple datafeeds in a single request. |
| `update` | `EXEC` | `datafeedId, merchantId` | Updates a datafeed configuration of your Merchant Center account. Any fields that are not provided are deleted from the resource. |
