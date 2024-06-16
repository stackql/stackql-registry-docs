---
title: log_analytics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics
  - compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_analytics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.log_analytics" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="export_request_rate_by_interval" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__intervalLength" /> | Export logs that show Api requests made by this subscription in the given time window to show throttling activities. |
| <CopyableCode code="export_throttled_requests" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Export logs that show total throttled Api requests for this subscription in the given time window. |
