---
title: component_quota_status
hide_title: false
hide_table_of_contents: false
keywords:
  - component_quota_status
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>component_quota_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_quota_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.component_quota_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="AppId" /> | `string` | The Application ID for the Application Insights component. |
| <CopyableCode code="ExpirationTime" /> | `string` | Date and time when the daily data volume cap will be reset, and data ingestion will resume. |
| <CopyableCode code="ShouldBeThrottled" /> | `boolean` | The daily data volume cap is met, and data ingestion will be stopped. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns daily data volume cap (quota) status for an Application Insights component. |

## `SELECT` examples

Returns daily data volume cap (quota) status for an Application Insights component.


```sql
SELECT
AppId,
ExpirationTime,
ShouldBeThrottled
FROM azure.application_insights.component_quota_status
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```