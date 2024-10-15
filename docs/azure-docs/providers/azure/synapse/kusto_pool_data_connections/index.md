---
title: kusto_pool_data_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_data_connections
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

Creates, updates, deletes, gets or lists a <code>kusto_pool_data_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pool_data_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_data_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the endpoint for the data connection |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns a data connection. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the list of data connections of the given Kusto pool database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Creates or updates a data connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the data connection with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Updates a data connection. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type" /> | Checks that the data connection name is valid and is not already in use. |
| <CopyableCode code="data_connection_validation" /> | `EXEC` | <CopyableCode code="databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Checks that the data connection parameters are valid. |

## `SELECT` examples

Returns the list of data connections of the given Kusto pool database.


```sql
SELECT
kind,
location,
systemData
FROM azure.synapse.kusto_pool_data_connections
WHERE databaseName = '{{ databaseName }}'
AND kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kusto_pool_data_connections</code> resource.

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
INSERT INTO azure.synapse.kusto_pool_data_connections (
dataConnectionName,
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
'{{ dataConnectionName }}',
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

Updates a <code>kusto_pool_data_connections</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.kusto_pool_data_connections
SET 
location = '{{ location }}',
kind = '{{ kind }}'
WHERE 
dataConnectionName = '{{ dataConnectionName }}'
AND databaseName = '{{ databaseName }}'
AND kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}'
AND data__kind = '{{ data__kind }}';
```

## `DELETE` example

Deletes the specified <code>kusto_pool_data_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.kusto_pool_data_connections
WHERE dataConnectionName = '{{ dataConnectionName }}'
AND databaseName = '{{ databaseName }}'
AND kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
