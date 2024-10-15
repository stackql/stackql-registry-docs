---
title: backup_workload_items
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_workload_items
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

Creates, updates, deletes, gets or lists a <code>backup_workload_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_workload_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_workload_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Base class for backup item. Workload-specific backup items are derived from this class. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerName, fabricName, resourceGroupName, subscriptionId, vaultName" /> | Provides a pageable list of workload item of a specific container according to the query filter and the pagination
parameters. |

## `SELECT` examples

Provides a pageable list of workload item of a specific container according to the query filter and the pagination
parameters.


```sql
SELECT
id,
name,
properties,
type
FROM azure.recovery_services_backup.backup_workload_items
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```