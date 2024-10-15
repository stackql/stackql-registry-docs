---
title: monitors_app_services
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_app_services
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

Creates, updates, deletes, gets or lists a <code>monitors_app_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_app_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_app_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="autoUpdateSetting" /> | `string` | Update settings of OneAgent. |
| <CopyableCode code="availabilityState" /> | `string` | The availability state of OneAgent. |
| <CopyableCode code="hostGroup" /> | `string` | The name of the host group |
| <CopyableCode code="hostName" /> | `string` | The name of the host |
| <CopyableCode code="logModule" /> | `string` | Tells whether log modules are enabled or not |
| <CopyableCode code="monitoringType" /> | `string` | The monitoring mode of OneAgent |
| <CopyableCode code="resourceId" /> | `string` | App service resource ID |
| <CopyableCode code="updateStatus" /> | `string` | The current update status of OneAgent. |
| <CopyableCode code="version" /> | `string` | Version of the Dynatrace agent installed on the App Service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
autoUpdateSetting,
availabilityState,
hostGroup,
hostName,
logModule,
monitoringType,
resourceId,
updateStatus,
version
FROM azure_isv.dynatrace.monitors_app_services
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```