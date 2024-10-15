---
title: services_export_errors_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - services_export_errors_v2
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

Creates, updates, deletes, gets or lists a <code>services_export_errors_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_export_errors_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_export_errors_v2" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The error Id. |
| <CopyableCode code="attributeName" /> | `string` | The attribute name. |
| <CopyableCode code="attributeValue" /> | `string` | The attribute value. |
| <CopyableCode code="createdDate" /> | `string` | The date and time, in UTC, when the error was created. |
| <CopyableCode code="csObjectId" /> | `string` |  the cs object Id. |
| <CopyableCode code="dn" /> | `string` | the DN of the object. |
| <CopyableCode code="existingObject" /> | `object` | Object that hold sync object details. |
| <CopyableCode code="exportErrorStatus" /> | `integer` | The export error status. |
| <CopyableCode code="incomingObject" /> | `object` | Object that hold sync object details. |
| <CopyableCode code="incomingObjectDisplayName" /> | `string` | The incoming object display name. |
| <CopyableCode code="incomingObjectType" /> | `string` | The incoming object type. |
| <CopyableCode code="mergedEntityId" /> | `string` | The merged entity Id. |
| <CopyableCode code="modifiedOrRemovedAttributeValue" /> | `string` | The modified or removed attribute value. |
| <CopyableCode code="runStepResultId" /> | `string` | The run step result Id. |
| <CopyableCode code="samAccountName" /> | `string` | The sam account name. |
| <CopyableCode code="serverErrorDetail" /> | `string` | The server error details. |
| <CopyableCode code="serviceId" /> | `string` | The service Id. |
| <CopyableCode code="serviceMemberId" /> | `string` | The server Id. |
| <CopyableCode code="timeFirstOccurred" /> | `string` | The time when the error first occurred. |
| <CopyableCode code="timeOccurred" /> | `string` | The date and time when the error occurred. |
| <CopyableCode code="type" /> | `string` | The type of the error. |
| <CopyableCode code="userPrincipalName" /> | `string` | The user principal name |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="errorBucket, serviceName" /> |  Gets the categorized export errors. |

## `SELECT` examples

 Gets the categorized export errors.


```sql
SELECT
id,
attributeName,
attributeValue,
createdDate,
csObjectId,
dn,
existingObject,
exportErrorStatus,
incomingObject,
incomingObjectDisplayName,
incomingObjectType,
mergedEntityId,
modifiedOrRemovedAttributeValue,
runStepResultId,
samAccountName,
serverErrorDetail,
serviceId,
serviceMemberId,
timeFirstOccurred,
timeOccurred,
type,
userPrincipalName
FROM azure.ad_hybrid_health_service.services_export_errors_v2
WHERE errorBucket = '{{ errorBucket }}'
AND serviceName = '{{ serviceName }}';
```