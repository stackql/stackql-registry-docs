---
title: geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - geo_backup_policies
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

Creates, updates, deletes, gets or lists a <code>geo_backup_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.geo_backup_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_geo_backup_policies', value: 'view', },
        { label: 'geo_backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="geoBackupPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of geo backup policy.  This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `text` | Backup policy location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, geoBackupPolicyName, resourceGroupName, serverName, subscriptionId" /> | Gets a geo backup policy. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Returns a list of geo backup policies. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, geoBackupPolicyName, resourceGroupName, serverName, subscriptionId, data__properties" /> | Updates a database geo backup policy. |

## `SELECT` examples

Returns a list of geo backup policies.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_geo_backup_policies', value: 'view', },
        { label: 'geo_backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
geoBackupPolicyName,
kind,
location,
resourceGroupName,
serverName,
state,
storage_type,
subscriptionId
FROM azure.sql.vw_geo_backup_policies
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.sql.geo_backup_policies
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>geo_backup_policies</code> resource.

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
INSERT INTO azure.sql.geo_backup_policies (
databaseName,
geoBackupPolicyName,
resourceGroupName,
serverName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ databaseName }}',
'{{ geoBackupPolicyName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
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
