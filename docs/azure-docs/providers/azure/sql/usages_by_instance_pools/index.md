---
title: usages_by_instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - usages_by_instance_pools
  - sql
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

Creates, updates, deletes, gets or lists a <code>usages_by_instance_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages_by_instance_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.usages_by_instance_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `object` | ARM Usage Name |
| <CopyableCode code="currentValue" /> | `integer` | Usage current value. |
| <CopyableCode code="limit" /> | `integer` | Usage limit. |
| <CopyableCode code="requestedLimit" /> | `integer` | Usage requested limit. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="unit" /> | `string` | Usage unit. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Gets all instance pool usage metrics |

## `SELECT` examples

Gets all instance pool usage metrics


```sql
SELECT
id,
name,
currentValue,
limit,
requestedLimit,
type,
unit
FROM azure.sql.usages_by_instance_pools
WHERE instancePoolName = '{{ instancePoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```