---
title: database_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_extensions
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

Creates, updates, deletes, gets or lists a <code>database_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Contains the operation result properties for import/export operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, extensionName, resourceGroupName, serverName, subscriptionId" /> | Gets a database extension. This will return resource not found as it is not supported. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | List database extension. This will return an empty list as it is not supported. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, extensionName, resourceGroupName, serverName, subscriptionId" /> | Perform a database extension operation, like polybase import |

## `SELECT` examples

List database extension. This will return an empty list as it is not supported.


```sql
SELECT
properties
FROM azure.sql.database_extensions
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_extensions</code> resource.

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
INSERT INTO azure.sql.database_extensions (
databaseName,
extensionName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ databaseName }}',
'{{ extensionName }}',
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
        - name: operationMode
          value: string
        - name: storageKeyType
          value: string
        - name: storageKey
          value: string
        - name: storageUri
          value: string

```
</TabItem>
</Tabs>
