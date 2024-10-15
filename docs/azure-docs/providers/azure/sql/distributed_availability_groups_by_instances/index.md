---
title: distributed_availability_groups_by_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - distributed_availability_groups_by_instances
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

Creates, updates, deletes, gets or lists a <code>distributed_availability_groups_by_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributed_availability_groups_by_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.distributed_availability_groups_by_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a distributed availability group. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of a distributed availability groups in instance. |

## `SELECT` examples

Gets a list of a distributed availability groups in instance.


```sql
SELECT
properties
FROM azure.sql.distributed_availability_groups_by_instances
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```