---
title: sub_account_monitored_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account_monitored_resources
  - logz
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

Creates, updates, deletes, gets or lists a <code>sub_account_monitored_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sub_account_monitored_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.logz.sub_account_monitored_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ARM id of the resource. |
| <CopyableCode code="reasonForLogsStatus" /> | `string` | Reason for why the resource is sending logs (or why it is not sending). |
| <CopyableCode code="reasonForMetricsStatus" /> | `string` | Reason for why the resource is sending metrics (or why it is not sending). |
| <CopyableCode code="sendingLogs" /> | `boolean` | Flag indicating if resource is sending logs to Logz. |
| <CopyableCode code="sendingMetrics" /> | `boolean` | Flag indicating if resource is sending metrics to Logz. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
reasonForLogsStatus,
reasonForMetricsStatus,
sendingLogs,
sendingMetrics,
systemData
FROM azure_isv.logz.sub_account_monitored_resources
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subAccountName = '{{ subAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```