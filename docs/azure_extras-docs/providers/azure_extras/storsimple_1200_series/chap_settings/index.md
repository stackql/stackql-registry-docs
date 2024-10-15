---
title: chap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - chap_settings
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>chap_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.chap_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chap_settings', value: 'view', },
        { label: 'chap_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="chapUserName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Chap properties |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="chapUserName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified chap setting name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the chap settings in a device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="chapUserName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the chap setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="chapUserName, deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the chap setting. |

## `SELECT` examples

Retrieves all the chap settings in a device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chap_settings', value: 'view', },
        { label: 'chap_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
chapUserName,
deviceName,
managerName,
password,
resourceGroupName,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_chap_settings
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.storsimple_1200_series.chap_settings
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>chap_settings</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.chap_settings (
chapUserName,
deviceName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ chapUserName }}',
'{{ deviceName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: password
          value:
            - name: value
              value: string
            - name: encryptionCertificateThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>chap_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.chap_settings
WHERE chapUserName = '{{ chapUserName }}'
AND deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
