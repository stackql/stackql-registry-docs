---
title: spanquery_fields_values
hide_title: false
hide_table_of_contents: false
keywords:
  - spanquery_fields_values
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
<tr><td><b>Name</b></td><td><code>spanquery_fields_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.tracing.spanquery_fields_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="fieldValues" /> | `array` | List of filter field values. |
| <CopyableCode code="next" /> | `string` | Next continuation token. |
| <CopyableCode code="totalCount" /> | `integer` | Total number of values for a field matching the query. Can be approximated when it's above 3000. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSpanQueryFieldValues" /> | `SELECT` | <CopyableCode code="field, region" /> |
