---
title: synchronization_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_settings
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

Creates, updates, deletes, gets or lists a <code>synchronization_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>synchronization_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.synchronization_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="kind" /> | `string` | Kind of synchronization setting. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId, synchronizationSettingName" /> | Get a synchronizationSetting in a share |
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | List synchronizationSettings in a share |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId, synchronizationSettingName, data__kind" /> | Create a synchronizationSetting |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId, synchronizationSettingName" /> | Delete a synchronizationSetting in a share |

## `SELECT` examples

List synchronizationSettings in a share


```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.data_share.synchronization_settings
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>synchronization_settings</code> resource.

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
INSERT INTO azure.data_share.synchronization_settings (
accountName,
resourceGroupName,
shareName,
subscriptionId,
synchronizationSettingName,
data__kind,
kind
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ shareName }}',
'{{ subscriptionId }}',
'{{ synchronizationSettingName }}',
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

Deletes the specified <code>synchronization_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_share.synchronization_settings
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND synchronizationSettingName = '{{ synchronizationSettingName }}';
```
