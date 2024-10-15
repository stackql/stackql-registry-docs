---
title: host_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - host_keys
  - app_service
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

Creates, updates, deletes, gets or lists a <code>host_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.host_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="functionKeys" /> | `object` | Host level function keys. |
| <CopyableCode code="masterKey" /> | `string` | Secret key. |
| <CopyableCode code="systemKeys" /> | `object` | System keys. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get host secrets for a function app. |

## `SELECT` examples

Description for Get host secrets for a function app.


```sql
SELECT
functionKeys,
masterKey,
systemKeys
FROM azure.app_service.host_keys
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```