---
title: monitors_metric_status
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_metric_status
  - dynatrace
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

Creates, updates, deletes, gets or lists a <code>monitors_metric_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_metric_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_metric_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureResourceIds" /> | `array` | Azure resource IDs |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Get metric status |

## `SELECT` examples

Get metric status


```sql
SELECT
azureResourceIds
FROM azure_isv.dynatrace.monitors_metric_status
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```