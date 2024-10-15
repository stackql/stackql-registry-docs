---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - notification_hubs
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="keyName" /> | `string` | Gets or sets keyName of the created AuthorizationRule |
| <CopyableCode code="primaryConnectionString" /> | `string` | Gets or sets primaryConnectionString of the AuthorizationRule. |
| <CopyableCode code="primaryKey" /> | `string` | Gets or sets primaryKey of the created AuthorizationRule. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Gets or sets secondaryConnectionString of the created
AuthorizationRule |
| <CopyableCode code="secondaryKey" /> | `string` | Gets or sets secondaryKey of the created AuthorizationRule |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
keyName,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.notification_hubs.keys
WHERE authorizationRuleName = '{{ authorizationRuleName }}'
AND namespaceName = '{{ namespaceName }}'
AND notificationHubName = '{{ notificationHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```