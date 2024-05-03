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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.collectors.sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Source identifer. |
| <CopyableCode code="name" /> | `string` | Source name. |
| <CopyableCode code="alive" /> | `boolean` | Source alive. |
| <CopyableCode code="automaticDateParsing" /> | `boolean` | Source automaticDateParsing. |
| <CopyableCode code="category" /> | `string` | Source category. |
| <CopyableCode code="cutoffTimestamp" /> | `integer` | Source cutoffTimestamp. |
| <CopyableCode code="denylist" /> | `array` | Source denylist. |
| <CopyableCode code="encoding" /> | `string` | Source encoding. |
| <CopyableCode code="fields" /> | `object` | Source fields. |
| <CopyableCode code="filters" /> | `array` | Source filters. |
| <CopyableCode code="forceTimeZone" /> | `boolean` | Source forceTimeZone. |
| <CopyableCode code="hashAlgorithm" /> | `string` | Source hashAlgorithm. |
| <CopyableCode code="hostName" /> | `string` | Source hostName. |
| <CopyableCode code="messagePerRequest" /> | `boolean` | Source messagePerRequest. |
| <CopyableCode code="multilineProcessingEnabled" /> | `boolean` | Source multilineProcessingEnabled. |
| <CopyableCode code="pathExpression" /> | `string` | Source pathExpression. |
| <CopyableCode code="sourceType" /> | `string` | Source sourceType. |
| <CopyableCode code="url" /> | `string` | Source url. |
| <CopyableCode code="useAutolineMatching" /> | `boolean` | Source useAutolineMatching. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_source_by_id" /> | `SELECT` | <CopyableCode code="collectorId, sourceId, region" /> | Gets information about a specified Collector and Source. |
| <CopyableCode code="list_sources" /> | `SELECT` | <CopyableCode code="collectorId, region" /> | Gets information about all Sources for a specified Collector. |
| <CopyableCode code="create_source" /> | `INSERT` | <CopyableCode code="collectorId, region" /> | Creates a new Source for a Collector. See Use JSON to Configure Sources for required fields for the request JSON file. |
| <CopyableCode code="delete_source" /> | `DELETE` | <CopyableCode code="collectorId, sourceId, region" /> | Delete Source by ID |
| <CopyableCode code="update_source" /> | `EXEC` | <CopyableCode code="collectorId, sourceId, region" /> | Update a source |
