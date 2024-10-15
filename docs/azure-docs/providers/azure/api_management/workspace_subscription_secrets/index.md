---
title: workspace_subscription_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_subscription_secrets
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_subscription_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_subscription_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_subscription_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryKey" /> | `string` | Subscription primary key. |
| <CopyableCode code="secondaryKey" /> | `string` | Subscription secondary key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Gets the specified Subscription keys. |

## `SELECT` examples

Gets the specified Subscription keys.


```sql
SELECT
primaryKey,
secondaryKey
FROM azure.api_management.workspace_subscription_secrets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND sid = '{{ sid }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```