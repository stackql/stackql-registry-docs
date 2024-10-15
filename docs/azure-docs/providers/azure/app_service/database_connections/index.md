---
title: database_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - database_connections
  - app_service
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

Creates, updates, deletes, gets or lists a <code>database_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.database_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DatabaseConnection resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseConnectionName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseConnectionName, name, resourceGroupName, subscriptionId" /> | Description for Create or update a database connection for a static site |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseConnectionName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseConnectionName, name, resourceGroupName, subscriptionId" /> | Description for Create or update a database connection for a static site |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.database_connections
WHERE databaseConnectionName = '{{ databaseConnectionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_connections</code> resource.

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
INSERT INTO azure.app_service.database_connections (
databaseConnectionName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ databaseConnectionName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: resourceId
          value: string
        - name: connectionIdentity
          value: string
        - name: connectionString
          value: string
        - name: region
          value: string
        - name: configurationFiles
          value:
            - - name: fileName
                value: string
              - name: contents
                value: string
              - name: type
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>database_connections</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.database_connections
SET 
properties = '{{ properties }}'
WHERE 
databaseConnectionName = '{{ databaseConnectionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>database_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.database_connections
WHERE databaseConnectionName = '{{ databaseConnectionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
