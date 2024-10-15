---
title: data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sets
  - data_share
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

Creates, updates, deletes, gets or lists a <code>data_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.data_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="kind" /> | `string` | Kind of data set. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, dataSetName, resourceGroupName, shareName, subscriptionId" /> | Get a DataSet in a share |
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | List DataSets in a share |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, dataSetName, resourceGroupName, shareName, subscriptionId, data__kind" /> | Create a DataSet  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, dataSetName, resourceGroupName, shareName, subscriptionId" /> | Delete a DataSet in a share |

## `SELECT` examples

List DataSets in a share


```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.data_share.data_sets
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_sets</code> resource.

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
INSERT INTO azure.data_share.data_sets (
accountName,
dataSetName,
resourceGroupName,
shareName,
subscriptionId,
data__kind,
kind
)
SELECT 
'{{ accountName }}',
'{{ dataSetName }}',
'{{ resourceGroupName }}',
'{{ shareName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ kind }}'
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
    - name: systemData
      value:
        - name: createdAt
          value: string
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: lastModifiedAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
    - name: type
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_share.data_sets
WHERE accountName = '{{ accountName }}'
AND dataSetName = '{{ dataSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
