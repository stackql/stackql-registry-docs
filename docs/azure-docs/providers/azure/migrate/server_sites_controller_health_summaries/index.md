---
title: server_sites_controller_health_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - server_sites_controller_health_summaries
  - migrate
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

Creates, updates, deletes, gets or lists a <code>server_sites_controller_health_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_sites_controller_health_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_sites_controller_health_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="affectedObjectsCount" /> | `integer` | Gets or sets the count of affected objects. |
| <CopyableCode code="affectedResourceType" /> | `string` | Gets the affected resource type. |
| <CopyableCode code="affectedResources" /> | `array` | Gets or sets the affected resources. |
| <CopyableCode code="applianceName" /> | `string` | Gets the appliance name. |
| <CopyableCode code="errorCode" /> | `string` | Gets the error code. |
| <CopyableCode code="errorId" /> | `integer` | Gets the error Id. |
| <CopyableCode code="errorMessage" /> | `string` | Gets the error message. |
| <CopyableCode code="fabricLayoutUpdateSources" /> | `array` | Gets or sets sources of the exception. |
| <CopyableCode code="hitCount" /> | `integer` | Gets or sets the hit count of the error. |
| <CopyableCode code="remediationGuidance" /> | `string` | Gets the remediation guidance. |
| <CopyableCode code="severity" /> | `string` | Gets the severity of error. |
| <CopyableCode code="summaryMessage" /> | `string` | Gets the summary message. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site health summary. |

## `SELECT` examples

Method to get site health summary.


```sql
SELECT
affectedObjectsCount,
affectedResourceType,
affectedResources,
applianceName,
errorCode,
errorId,
errorMessage,
fabricLayoutUpdateSources,
hitCount,
remediationGuidance,
severity,
summaryMessage
FROM azure.migrate.server_sites_controller_health_summaries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```