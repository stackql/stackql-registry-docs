---
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>data_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.data_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="kind" /> | `string` | The kind of the data connector |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataConnectorId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a data connector. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all data connectors. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataConnectorId, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Creates or updates the data connector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataConnectorId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the data connector. |

## `SELECT` examples

Gets all data connectors.


```sql
SELECT
etag,
kind
FROM azure.sentinel.data_connectors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_connectors</code> resource.

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
INSERT INTO azure.sentinel.data_connectors (
dataConnectorId,
resourceGroupName,
subscriptionId,
workspaceName,
data__kind,
etag,
kind
)
SELECT 
'{{ dataConnectorId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__kind }}',
'{{ etag }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: kind
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.data_connectors
WHERE dataConnectorId = '{{ dataConnectorId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
