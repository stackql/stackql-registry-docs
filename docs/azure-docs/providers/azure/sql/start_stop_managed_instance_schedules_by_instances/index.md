---
title: start_stop_managed_instance_schedules_by_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - start_stop_managed_instance_schedules_by_instances
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

Creates, updates, deletes, gets or lists a <code>start_stop_managed_instance_schedules_by_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>start_stop_managed_instance_schedules_by_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.start_stop_managed_instance_schedules_by_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of managed instance's Start/Stop schedule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Lists the managed instance's Start/Stop schedules. |

## `SELECT` examples

Lists the managed instance's Start/Stop schedules.


```sql
SELECT
properties,
systemData
FROM azure.sql.start_stop_managed_instance_schedules_by_instances
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```