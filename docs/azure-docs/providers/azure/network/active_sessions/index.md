---
title: active_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - active_sessions
  - network
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

Creates, updates, deletes, gets or lists a <code>active_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>active_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.active_sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="protocol" /> | `string` | The protocol used to connect to the target. |
| <CopyableCode code="resourceType" /> | `string` | The type of the resource. |
| <CopyableCode code="sessionDurationInMins" /> | `number` | Duration in mins the session has been active. |
| <CopyableCode code="sessionId" /> | `string` | A unique id for the session. |
| <CopyableCode code="startTime" /> | `object` | The time when the session started. |
| <CopyableCode code="targetHostName" /> | `string` | The host name of the target. |
| <CopyableCode code="targetIpAddress" /> | `string` | The IP Address of the target. |
| <CopyableCode code="targetResourceGroup" /> | `string` | The resource group of the target. |
| <CopyableCode code="targetResourceId" /> | `string` | The resource id of the target. |
| <CopyableCode code="targetSubscriptionId" /> | `string` | The subscription id for the target virtual machine. |
| <CopyableCode code="userName" /> | `string` | The user name who is active on this session. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Returns the list of currently active sessions on the Bastion. |

## `SELECT` examples

Returns the list of currently active sessions on the Bastion.


```sql
SELECT
protocol,
resourceType,
sessionDurationInMins,
sessionId,
startTime,
targetHostName,
targetIpAddress,
targetResourceGroup,
targetResourceId,
targetSubscriptionId,
userName
FROM azure.network.active_sessions
WHERE bastionHostName = '{{ bastionHostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```