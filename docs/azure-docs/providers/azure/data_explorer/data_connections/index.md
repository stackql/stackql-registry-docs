---
title: data_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connections
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

Creates, updates, deletes, gets or lists a <code>data_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.data_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the endpoint for the data connection |
| <CopyableCode code="location" /> | `string` | Resource location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId" /> | Returns a data connection. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns the list of data connections of the given Kusto database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId, data__kind" /> | Creates or updates a data connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId" /> | Deletes the data connection with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId, data__kind" /> | Updates a data connection. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the data connection name is valid and is not already in use. |
| <CopyableCode code="data_connection_validation" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Checks that the data connection parameters are valid. |

## `SELECT` examples

Returns the list of data connections of the given Kusto database.


```sql
SELECT
kind,
location
FROM azure.data_explorer.data_connections
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_connections</code> resource.

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
INSERT INTO azure.data_explorer.data_connections (
clusterName,
dataConnectionName,
databaseName,
resourceGroupName,
subscriptionId,
data__kind,
location,
kind
)
SELECT 
'{{ clusterName }}',
'{{ dataConnectionName }}',
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

Updates a <code>data_connections</code> resource.

```sql
/*+ update */
UPDATE azure.data_explorer.data_connections
SET 
location = '{{ location }}',
kind = '{{ kind }}'
WHERE 
clusterName = '{{ clusterName }}'
AND dataConnectionName = '{{ dataConnectionName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__kind = '{{ data__kind }}';
```

## `DELETE` example

Deletes the specified <code>data_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.data_connections
WHERE clusterName = '{{ clusterName }}'
AND dataConnectionName = '{{ dataConnectionName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
