---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - authorization
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

Creates, updates, deletes, gets or lists a <code>permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `array` | Allowed actions. |
| <CopyableCode code="dataActions" /> | `array` | Allowed Data actions. |
| <CopyableCode code="notActions" /> | `array` | Denied actions. |
| <CopyableCode code="notDataActions" /> | `array` | Denied Data actions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_for_resource" /> | `SELECT` | <CopyableCode code="parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Gets all permissions the caller has for a resource. |
| <CopyableCode code="list_for_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all permissions the caller has for a resource group. |

## `SELECT` examples

Gets all permissions the caller has for a resource group.


```sql
SELECT
actions,
dataActions,
notActions,
notDataActions
FROM azure.authorization.permissions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```