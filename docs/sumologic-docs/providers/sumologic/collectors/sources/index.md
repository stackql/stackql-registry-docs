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
| `category` | `string` | Source category. |
| `encoding` | `string` | Source encoding. |
| `fields` | `object` | Source fields. |
| `hashAlgorithm` | `string` | Source hashAlgorithm. |
| `sourceType` | `string` | Source sourceType. |
| `forceTimeZone` | `boolean` | Source forceTimeZone. |
| `useAutolineMatching` | `boolean` | Source useAutolineMatching. |
| `cutoffTimestamp` | `integer` | Source cutoffTimestamp. |
| `alive` | `boolean` | Source alive. |
| `filters` | `array` | Source filters. |
| `pathExpression` | `string` | Source pathExpression. |
| `messagePerRequest` | `boolean` | Source messagePerRequest. |
| `url` | `string` | Source url. |
| `denylist` | `array` | Source denylist. |
| `hostName` | `string` | Source hostName. |
| `automaticDateParsing` | `boolean` | Source automaticDateParsing. |
| `multilineProcessingEnabled` | `boolean` | Source multilineProcessingEnabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_source_by_id` | `SELECT` | `collectorId, sourceId` | Gets information about a specified Collector and Source. |
| `list_sources` | `SELECT` | `collectorId` | Gets information about all Sources for a specified Collector. |
| `create_source` | `INSERT` | `collectorId` | Creates a new Source for a Collector. See Use JSON to Configure Sources for required fields for the request JSON file. |
| `delete_source` | `DELETE` | `collectorId, sourceId` | Delete Source by ID |
| `update_source` | `EXEC` | `collectorId, sourceId` | Update a source |
