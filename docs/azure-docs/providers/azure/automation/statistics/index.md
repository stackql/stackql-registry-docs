---
title: statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - statistics
  - automation
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

Creates, updates, deletes, gets or lists a <code>statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.statistics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the id. |
| <CopyableCode code="counterProperty" /> | `string` | Gets the property value of the statistic. |
| <CopyableCode code="counterValue" /> | `integer` | Gets the value of the statistic. |
| <CopyableCode code="endTime" /> | `string` | Gets the endTime of the statistic. |
| <CopyableCode code="startTime" /> | `string` | Gets the startTime of the statistic. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve the statistics for the account. |

## `SELECT` examples

Retrieve the statistics for the account.


```sql
SELECT
id,
counterProperty,
counterValue,
endTime,
startTime
FROM azure.automation.statistics
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```