---
title: sql_pool_geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_geo_backup_policies
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_geo_backup_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_geo_backup_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_geo_backup_policies', value: 'view', },
        { label: 'sql_pool_geo_backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="geoBackupPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of geo backup policy.  This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `text` | Backup policy location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of geo backup policy.  This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Backup policy location. |
| <CopyableCode code="properties" /> | `object` | The properties of the geo backup policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get the specified SQL pool geo backup policy |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get list of SQL pool geo backup policies |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__properties" /> | Updates a SQL Pool geo backup policy. |

## `SELECT` examples

Get list of SQL pool geo backup policies

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_geo_backup_policies', value: 'view', },
        { label: 'sql_pool_geo_backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
geoBackupPolicyName,
kind,
location,
resourceGroupName,
sqlPoolName,
state,
storage_type,
subscriptionId,
workspaceName
FROM azure.synapse.vw_sql_pool_geo_backup_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.synapse.sql_pool_geo_backup_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_geo_backup_policies</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.synapse.sql_pool_geo_backup_policies (
geoBackupPolicyName,
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ geoBackupPolicyName }}',
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: state
          value: string
        - name: storageType
          value: string
    - name: kind
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>
