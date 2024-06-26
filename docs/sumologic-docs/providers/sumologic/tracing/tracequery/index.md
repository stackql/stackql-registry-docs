---
title: tracequery
hide_title: false
hide_table_of_contents: false
keywords:
  - tracequery
  - tracing
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
<tr><td><b>Name</b></td><td><code>tracequery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.tracing.tracequery" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createTraceQuery" /> | `INSERT` | <CopyableCode code="data__queryRows, data__timeRange, region" /> | Execute a trace search query and get the id to fetch its status and results. Use the [Trace Query Status](#operation/getTraceQueryStatus) endpoint to check a query status. When the query has been completed, use the [Trace Query Result](#operation/getTraceQueryResult) endpoint to get the result of the asynchronous query. |
| <CopyableCode code="cancelTraceQuery" /> | `EXEC` | <CopyableCode code="queryId, region" /> | Cancel a currently processed trace search query with the given id. |
