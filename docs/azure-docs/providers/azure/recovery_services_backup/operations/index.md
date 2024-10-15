---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the Operation. |
| <CopyableCode code="display" /> | `object` | Localized display information of an operation. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation;governs the display of the operation in the RBAC UX and the audit logs UX |
| <CopyableCode code="properties" /> | `object` | Class to represent shoebox properties in json client discovery. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Returns the list of available operations. |
| <CopyableCode code="bms_prepare_data_move" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__dataMoveLevel, data__targetRegion, data__targetResourceId" /> | Prepares source vault for Data Move operation |
| <CopyableCode code="bms_trigger_data_move" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__correlationId, data__dataMoveLevel, data__sourceRegion, data__sourceResourceId" /> | Triggers Data Move Operation on target vault |
| <CopyableCode code="move_recovery_point" /> | `EXEC` | <CopyableCode code="containerName, fabricName, protectedItemName, recoveryPointId, resourceGroupName, subscriptionId, vaultName" /> |  |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__id, data__properties" /> | Validate operation for specified backed up item. This is a synchronous operation. |

## `SELECT` examples

Returns the list of available operations.


```sql
SELECT
name,
display,
origin,
properties
FROM azure.recovery_services_backup.operations
;
```