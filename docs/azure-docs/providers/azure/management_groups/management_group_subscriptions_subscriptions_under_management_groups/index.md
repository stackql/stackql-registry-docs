---
title: management_group_subscriptions_subscriptions_under_management_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_subscriptions_subscriptions_under_management_groups
  - management_groups
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

Creates, updates, deletes, gets or lists a <code>management_group_subscriptions_subscriptions_under_management_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_group_subscriptions_subscriptions_under_management_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.management_group_subscriptions_subscriptions_under_management_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the subscription.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/subscriptions/0000000-0000-0000-0000-000000000001 |
| <CopyableCode code="name" /> | `string` | The stringified id of the subscription. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="properties" /> | `object` | The generic properties of subscription under a management group. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups/subscriptions |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId" /> | Retrieves details about all subscriptions which are associated with the management group.
 |

## `SELECT` examples

Retrieves details about all subscriptions which are associated with the management group.



```sql
SELECT
id,
name,
properties,
type
FROM azure.management_groups.management_group_subscriptions_subscriptions_under_management_groups
WHERE groupId = '{{ groupId }}';
```