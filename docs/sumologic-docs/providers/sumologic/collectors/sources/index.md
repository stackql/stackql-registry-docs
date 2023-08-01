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
| `multilineProcessingEnabled` | `boolean` | Source multilineProcessingEnabled. |
| `messagePerRequest` | `boolean` | Source messagePerRequest. |
| `automaticDateParsing` | `boolean` | Source automaticDateParsing. |
| `fields` | `object` | Source fields. |
| `pathExpression` | `string` | Source pathExpression. |
| `hostName` | `string` | Source hostName. |
| `cutoffTimestamp` | `integer` | Source cutoffTimestamp. |
| `denylist` | `array` | Source denylist. |
| `forceTimeZone` | `boolean` | Source forceTimeZone. |
| `encoding` | `string` | Source encoding. |
| `sourceType` | `string` | Source sourceType. |
| `url` | `string` | Source url. |
| `useAutolineMatching` | `boolean` | Source useAutolineMatching. |
| `filters` | `array` | Source filters. |
| `alive` | `boolean` | Source alive. |
| `category` | `string` | Source category. |
| `hashAlgorithm` | `string` | Source hashAlgorithm. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_source_by_id` | `SELECT` | `collectorId, sourceId, region` | Gets information about a specified Collector and Source. |
| `list_sources` | `SELECT` | `collectorId, region` | Gets information about all Sources for a specified Collector. |
| `create_source` | `INSERT` | `collectorId, region` | Creates a new Source for a Collector. See Use JSON to Configure Sources for required fields for the request JSON file. |
| `delete_source` | `DELETE` | `collectorId, sourceId, region` | Delete Source by ID |
| `update_source` | `EXEC` | `collectorId, sourceId, region` | Update a source |
