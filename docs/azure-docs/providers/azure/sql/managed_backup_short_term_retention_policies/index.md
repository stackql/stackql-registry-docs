---
title: managed_backup_short_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_backup_short_term_retention_policies
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

Creates, updates, deletes, gets or lists a <code>managed_backup_short_term_retention_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_backup_short_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_backup_short_term_retention_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_backup_short_term_retention_policies', value: 'view', },
        { label: 'managed_backup_short_term_retention_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a short term retention policy |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId" /> | Gets a managed database's short term retention policy. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed database's short term retention policy list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId" /> | Updates a managed database's short term retention policy. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId" /> | Updates a managed database's short term retention policy. |

## `SELECT` examples

Gets a managed database's short term retention policy list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_backup_short_term_retention_policies', value: 'view', },
        { label: 'managed_backup_short_term_retention_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
managedInstanceName,
policyName,
resourceGroupName,
retention_days,
subscriptionId
FROM azure.sql.vw_managed_backup_short_term_retention_policies
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_backup_short_term_retention_policies
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_backup_short_term_retention_policies</code> resource.

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
INSERT INTO azure.sql.managed_backup_short_term_retention_policies (
databaseName,
managedInstanceName,
policyName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ databaseName }}',
'{{ managedInstanceName }}',
'{{ policyName }}',
'{{ resourceGroupName }}',
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
        - name: retentionDays
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_backup_short_term_retention_policies</code> resource.

```sql
/*+ update */
UPDATE azure.sql.managed_backup_short_term_retention_policies
SET 
properties = '{{ properties }}'
WHERE 
databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
