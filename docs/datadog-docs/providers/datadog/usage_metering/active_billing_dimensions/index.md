---
title: active_billing_dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - active_billing_dimensions
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
<tr><td><b>Name</b></td><td><code>active_billing_dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.usage_metering.active_billing_dimensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID of the response. |
| <CopyableCode code="attributes" /> | `object` | List of active billing dimensions. |
| <CopyableCode code="type" /> | `string` | Type of active billing dimensions data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_active_billing_dimensions" /> | `SELECT` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="_get_active_billing_dimensions" /> | `EXEC` | <CopyableCode code="dd_site" /> |
