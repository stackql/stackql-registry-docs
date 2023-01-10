---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - collectors
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.collectors.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Source identifer. |
| `name` | `string` | Source name. |
| `cutoffTimestamp` | `integer` | Source cutoffTimestamp. |
| `messagePerRequest` | `boolean` | Source messagePerRequest. |
| `fields` | `object` | Source fields. |
| `alive` | `boolean` | Source alive. |
| `hashAlgorithm` | `string` | Source hashAlgorithm. |
| `denylist` | `array` | Source denylist. |
| `automaticDateParsing` | `boolean` | Source automaticDateParsing. |
| `useAutolineMatching` | `boolean` | Source useAutolineMatching. |
| `sourceType` | `string` | Source sourceType. |
| `forceTimeZone` | `boolean` | Source forceTimeZone. |
| `multilineProcessingEnabled` | `boolean` | Source multilineProcessingEnabled. |
| `category` | `string` | Source category. |
| `filters` | `array` | Source filters. |
| `url` | `string` | Source url. |
| `hostName` | `string` | Source hostName. |
| `encoding` | `string` | Source encoding. |
| `pathExpression` | `string` | Source pathExpression. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_source_by_id` | `SELECT` | `collectorId, sourceId` | Gets information about a specified Collector and Source. |
| `list_sources` | `SELECT` | `collectorId` | Gets information about all Sources for a specified Collector. |
| `create_source` | `INSERT` | `collectorId` | Creates a new Source for a Collector. See Use JSON to Configure Sources for required fields for the request JSON file. |
| `delete_source` | `DELETE` | `collectorId, sourceId` | Delete Source by ID |
| `update_source` | `EXEC` | `collectorId, sourceId` | Update a source |
