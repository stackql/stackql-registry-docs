---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the database |
| <CopyableCode code="location" /> | `string` | Resource location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns a database. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of databases of the given Kusto cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__kind" /> | Creates or updates a database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Deletes the database with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__kind" /> | Updates a database. |
| <CopyableCode code="add_principals" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Add Database principals permissions. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the databases resource name is valid and is not already in use. |
| <CopyableCode code="invite_follower" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__inviteeEmail" /> | Generates an invitation token that allows attaching a follower database to this database. |
| <CopyableCode code="remove_principals" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Remove Database principals permissions. |

## `SELECT` examples

Returns the list of databases of the given Kusto cluster.


```sql
SELECT
kind,
location
FROM azure.data_explorer.databases
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

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
INSERT INTO azure.data_explorer.databases (
clusterName,
databaseName,
resourceGroupName,
subscriptionId,
data__kind,
location,
kind
)
SELECT 
'{{ clusterName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE azure.data_explorer.databases
SET 
location = '{{ location }}',
kind = '{{ kind }}'
WHERE 
clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__kind = '{{ data__kind }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.databases
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
