---
title: monthly_cost_attributions
hide_title: false
hide_table_of_contents: false
keywords:
  - monthly_cost_attributions
  - usage_metering
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monthly_cost_attributions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.usage_metering.monthly_cost_attributions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID of the response. |
| <CopyableCode code="attributes" /> | `object` | Cost Attribution by Tag for a given organization. |
| <CopyableCode code="type" /> | `string` | Type of cost attribution data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_monthly_cost_attribution" /> | `SELECT` | <CopyableCode code="end_month, fields, start_month, dd_site" /> |
| <CopyableCode code="_get_monthly_cost_attribution" /> | `EXEC` | <CopyableCode code="end_month, fields, start_month, dd_site" /> |
