---
title: usage_application_security_monitorings
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_application_security_monitorings
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
<tr><td><b>Name</b></td><td><code>usage_application_security_monitorings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.usage_metering.usage_application_security_monitorings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID of the response. |
| <CopyableCode code="attributes" /> | `object` | Usage attributes data. |
| <CopyableCode code="type" /> | `string` | Type of usage data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_usage_application_security_monitoring" /> | `SELECT` | <CopyableCode code="start_hr, dd_site" /> |
| <CopyableCode code="_get_usage_application_security_monitoring" /> | `EXEC` | <CopyableCode code="start_hr, dd_site" /> |
