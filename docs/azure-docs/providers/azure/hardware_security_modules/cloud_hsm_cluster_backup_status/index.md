---
title: cloud_hsm_cluster_backup_status
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_cluster_backup_status
  - hardware_security_modules
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

Creates, updates, deletes, gets or lists a <code>cloud_hsm_cluster_backup_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_hsm_cluster_backup_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.cloud_hsm_cluster_backup_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_hsm_cluster_backup_status', value: 'view', },
        { label: 'cloud_hsm_cluster_backup_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_storage_blob_container_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudHsmClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobId" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Cloud HSM Cluster |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudHsmClusterName, jobId, resourceGroupName, subscriptionId" /> | Gets the backup operation status of the specified Cloud HSM Cluster |

## `SELECT` examples

Gets the backup operation status of the specified Cloud HSM Cluster

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_hsm_cluster_backup_status', value: 'view', },
        { label: 'cloud_hsm_cluster_backup_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_storage_blob_container_uri,
backup_id,
cloudHsmClusterName,
end_time,
error,
jobId,
job_id,
resourceGroupName,
start_time,
status,
status_details,
subscriptionId
FROM azure.hardware_security_modules.vw_cloud_hsm_cluster_backup_status
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND jobId = '{{ jobId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.hardware_security_modules.cloud_hsm_cluster_backup_status
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND jobId = '{{ jobId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

