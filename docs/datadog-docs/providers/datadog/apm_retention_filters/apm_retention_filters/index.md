---
title: apm_retention_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - apm_retention_filters
  - apm_retention_filters
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
<tr><td><b>Name</b></td><td><code>apm_retention_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.apm_retention_filters.apm_retention_filters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the retention filter. |
| <CopyableCode code="attributes" /> | `object` | The attributes of the retention filter. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_apm_retention_filter" /> | `SELECT` | <CopyableCode code="filter_id, dd_site" /> | Get an APM retention filter. |
| <CopyableCode code="list_apm_retention_filters" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get the list of APM retention filters. |
| <CopyableCode code="create_apm_retention_filter" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a retention filter to index spans in your organization.<br />Returns the retention filter definition when the request is successful. |
| <CopyableCode code="delete_apm_retention_filter" /> | `DELETE` | <CopyableCode code="filter_id, dd_site" /> | Delete a specific retention filter from your organization. |
| <CopyableCode code="_get_apm_retention_filter" /> | `EXEC` | <CopyableCode code="filter_id, dd_site" /> | Get an APM retention filter. |
| <CopyableCode code="_list_apm_retention_filters" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get the list of APM retention filters. |
| <CopyableCode code="reorder_apm_retention_filters" /> | `EXEC` | <CopyableCode code="data__data, dd_site" /> | Re-order the execution order of retention filters. |
| <CopyableCode code="update_apm_retention_filter" /> | `EXEC` | <CopyableCode code="filter_id, data__data, dd_site" /> | Update a retention filter from your organization. |
