---
title: fetch_cross_region_restore_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - fetch_cross_region_restore_jobs
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>fetch_cross_region_restore_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fetch_cross_region_restore_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.fetch_cross_region_restore_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | AzureBackup Job Class |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__jobId, data__sourceBackupVaultId, data__sourceRegion" /> | Fetches the Cross Region Restore Job |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__sourceBackupVaultId, data__sourceRegion" /> | Fetches list of Cross Region Restore job belonging to the vault |

## `SELECT` examples

Fetches list of Cross Region Restore job belonging to the vault


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_protection.fetch_cross_region_restore_jobs
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__sourceBackupVaultId = '{{ data__sourceBackupVaultId }}'
AND data__sourceRegion = '{{ data__sourceRegion }}';
```