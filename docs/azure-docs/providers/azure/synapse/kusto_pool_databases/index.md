---
title: kusto_pool_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_databases
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

Creates, updates, deletes, gets or lists a <code>kusto_pool_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pool_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the database |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns a database. |
| <CopyableCode code="list_by_kusto_pool" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the list of databases of the given Kusto pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Creates or updates a database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the database with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Updates a database. |

## `SELECT` examples

Returns the list of databases of the given Kusto pool.


```sql
SELECT
kind,
location,
systemData
FROM azure.synapse.kusto_pool_databases
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kusto_pool_databases</code> resource.

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
INSERT INTO azure.synapse.kusto_pool_databases (
databaseName,
kustoPoolName,
resourceGroupName,
subscriptionId,
workspaceName,
data__kind,
location,
kind
)
SELECT 
'{{ databaseName }}',
'{{ kustoPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__kind }}',
'{{ location }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: kind
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>kusto_pool_databases</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.kusto_pool_databases
SET 
location = '{{ location }}',
kind = '{{ kind }}'
WHERE 
databaseName = '{{ databaseName }}'
AND kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}'
AND data__kind = '{{ data__kind }}';
```

## `DELETE` example

Deletes the specified <code>kusto_pool_databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.kusto_pool_databases
WHERE databaseName = '{{ databaseName }}'
AND kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
