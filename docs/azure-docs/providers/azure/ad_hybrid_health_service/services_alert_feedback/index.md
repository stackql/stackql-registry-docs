---
title: services_alert_feedback
hide_title: false
hide_table_of_contents: false
keywords:
  - services_alert_feedback
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
<tr><td><b>Name</b></td><td><code>services_alert_feedback</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_alert_feedback" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="comment" /> | `string` | Additional comments related to the alert. |
| <CopyableCode code="consentedToShare" /> | `boolean` | Indicates if the alert feedback can be shared from product team. |
| <CopyableCode code="createdDate" /> | `string` | The date and time,in UTC,when the alert was created. |
| <CopyableCode code="feedback" /> | `string` | The feedback for the alert which indicates if the customer likes or dislikes the alert. |
| <CopyableCode code="level" /> | `string` | The alert level which indicates the severity of the alert. |
| <CopyableCode code="serviceMemberId" /> | `string` | The server Id of the alert. |
| <CopyableCode code="shortName" /> | `string` | The alert short name. |
| <CopyableCode code="state" /> | `string` | The alert state which can be either active or resolved with multiple resolution types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName, shortName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="serviceName, shortName" /> |
