---
title: on_demand_concurrency_caps
hide_title: false
hide_table_of_contents: false
keywords:
  - on_demand_concurrency_caps
  - synthetics
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
<tr><td><b>Name</b></td><td><code>on_demand_concurrency_caps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.synthetics.on_demand_concurrency_caps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attributes" /> | `object` | On-demand concurrency cap attributes. |
| <CopyableCode code="type" /> | `string` | On-demand concurrency cap type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_on_demand_concurrency_cap" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get the on-demand concurrency cap. |
| <CopyableCode code="_get_on_demand_concurrency_cap" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get the on-demand concurrency cap. |
| <CopyableCode code="set_on_demand_concurrency_cap" /> | `EXEC` | <CopyableCode code="dd_site" /> | Save new value for on-demand concurrency cap. |
