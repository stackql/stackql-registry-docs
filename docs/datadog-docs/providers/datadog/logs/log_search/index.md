---
title: log_search
hide_title: false
hide_table_of_contents: false
keywords:
  - log_search
  - logs
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
<tr><td><b>Name</b></td><td><code>log_search</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.logs.log_search" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID of the Log. |
| <CopyableCode code="attributes" /> | `object` | JSON object containing all log attributes and their associated values. |
| <CopyableCode code="type" /> | `string` | Type of the event. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_logs_get" /> | `SELECT` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="_list_logs_get" /> | `EXEC` | <CopyableCode code="dd_site" /> |
