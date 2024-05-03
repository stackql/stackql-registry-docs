---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - storsimple_1200_series
  - azure_extras    
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
| <CopyableCode code="_list_by_manager" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the alerts in a manager. |
| <CopyableCode code="clear" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId, data__alerts" /> | Clear the alerts. |
| <CopyableCode code="send_test_email" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, data__emailList" /> | Sends a test alert email. |
