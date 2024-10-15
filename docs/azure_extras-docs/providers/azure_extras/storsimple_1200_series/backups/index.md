---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Class represents Backup properties |
| <CopyableCode code="type" /> | `string` | The type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backups in a device. Can be used to get the backups for failover also. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the backups in a manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the backup. |
| <CopyableCode code="clone" /> | `EXEC` | <CopyableCode code="backupName, deviceName, elementName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Clones the given backup element to a new disk or share with given details. |

## `SELECT` examples

Retrieves all the backups in a manager.


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.storsimple_1200_series.backups
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.backups
WHERE backupName = '{{ backupName }}'
AND deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
