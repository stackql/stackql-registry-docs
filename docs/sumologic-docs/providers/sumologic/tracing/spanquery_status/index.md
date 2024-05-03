---
title: spanquery_status
hide_title: false
hide_table_of_contents: false
keywords:
  - spanquery_status
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
<tr><td><b>Name</b></td><td><code>spanquery_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.tracing.spanquery_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="queryRows" /> | `array` | A list of span analytics queries. |
| <CopyableCode code="status" /> | `string` | Status of the query. Possible values: `Processing`, `Finished`, `Error`, `Paused` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSpanQueryStatus" /> | `SELECT` | <CopyableCode code="queryId, region" /> |
