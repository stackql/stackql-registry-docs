---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Properties of alert |
| <CopyableCode code="type" /> | `string` | The type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the alerts in a manager. |
| <CopyableCode code="clear" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId, data__alerts" /> | Clear the alerts. |
| <CopyableCode code="send_test_email" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, data__emailList" /> | Sends a test alert email. |

## `SELECT` examples

Retrieves all the alerts in a manager.


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.storsimple_1200_series.alerts
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```