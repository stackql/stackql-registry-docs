---
title: services_alert_feedbacks
hide_title: false
hide_table_of_contents: false
keywords:
  - services_alert_feedbacks
  - ad_hybrid_health_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>services_alert_feedbacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_alert_feedbacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_alert_feedbacks" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName, shortName" /> | Gets a list of all alert feedback for a given tenant and alert type. |

## `SELECT` examples

Gets a list of all alert feedback for a given tenant and alert type.


```sql
SELECT
comment,
consentedToShare,
createdDate,
feedback,
level,
serviceMemberId,
shortName,
state
FROM azure.ad_hybrid_health_service.services_alert_feedbacks
WHERE serviceName = '{{ serviceName }}'
AND shortName = '{{ shortName }}';
```