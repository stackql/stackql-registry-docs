---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - resource_graph
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_graph.resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="$skipToken" /> | `string` | When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data. |
| <CopyableCode code="count" /> | `integer` | Number of records returned in the current response. In the case of paging, this is the number of records in the current page. |
| <CopyableCode code="data" /> | `object` | Query output in JObject array or Table format. |
| <CopyableCode code="facets" /> | `array` | Query facets. |
| <CopyableCode code="resultTruncated" /> | `string` | Indicates whether the query results are truncated. |
| <CopyableCode code="totalRecords" /> | `integer` | Number of total records matching the query. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="resources" /> | `SELECT` | <CopyableCode code="data__query" /> |
