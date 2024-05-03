---
title: services_user_bad_password_report
hide_title: false
hide_table_of_contents: false
keywords:
  - services_user_bad_password_report
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>services_user_bad_password_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_user_bad_password_report" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipAddress" /> | `string` | The IP address corresponding to the last error event. |
| <CopyableCode code="lastUpdated" /> | `string` | The date and time when the last error event was logged. |
| <CopyableCode code="totalErrorAttempts" /> | `integer` | The total count of specific error events. |
| <CopyableCode code="uniqueIpAddresses" /> | `string` | The list of unique IP addresses. |
| <CopyableCode code="userId" /> | `string` | The user ID value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="serviceName" /> |
