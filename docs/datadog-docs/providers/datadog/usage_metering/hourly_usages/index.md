---
title: hourly_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - hourly_usages
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
<tr><td><b>Name</b></td><td><code>hourly_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.usage_metering.hourly_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID of the response. |
| <CopyableCode code="attributes" /> | `object` | Attributes of hourly usage for a product family for an org for a time period. |
| <CopyableCode code="type" /> | `string` | Type of usage data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_hourly_usage" /> | `SELECT` | <CopyableCode code="filter[product_families], filter[timestamp][start], dd_site" /> |
| <CopyableCode code="_get_hourly_usage" /> | `EXEC` | <CopyableCode code="filter[product_families], filter[timestamp][start], dd_site" /> |
