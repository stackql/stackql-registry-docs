---
title: long_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_policies
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>long_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_term_retention_policies', value: 'view', },
        { label: 'long_term_retention_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backup_storage_access_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="make_backups_immutable" /> | `text` | field from the `properties` object |
| <CopyableCode code="monthly_retention" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="week_of_year" /> | `text` | field from the `properties` object |
| <CopyableCode code="weekly_retention" /> | `text` | field from the `properties` object |
| <CopyableCode code="yearly_retention" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a long term retention policy |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, policyName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's long term retention policy. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's long term retention policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, policyName, resourceGroupName, serverName, subscriptionId" /> | Set or update a database's long term retention policy. |

## `SELECT` examples

Gets a database's long term retention policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_term_retention_policies', value: 'view', },
        { label: 'long_term_retention_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backup_storage_access_tier,
databaseName,
make_backups_immutable,
monthly_retention,
policyName,
resourceGroupName,
serverName,
subscriptionId,
week_of_year,
weekly_retention,
yearly_retention
FROM azure.sql.vw_long_term_retention_policies
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.long_term_retention_policies
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>long_term_retention_policies</code> resource.

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
INSERT INTO azure.sql.long_term_retention_policies (
databaseName,
policyName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ databaseName }}',
'{{ policyName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
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
        - name: makeBackupsImmutable
          value: boolean
        - name: backupStorageAccessTier
          value: string
        - name: weeklyRetention
          value: string
        - name: monthlyRetention
          value: string
        - name: yearlyRetention
          value: string
        - name: weekOfYear
          value: integer

```
</TabItem>
</Tabs>
