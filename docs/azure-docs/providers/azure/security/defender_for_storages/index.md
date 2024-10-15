---
title: defender_for_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - defender_for_storages
  - security
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

Creates, updates, deletes, gets or lists a <code>defender_for_storages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>defender_for_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.defender_for_storages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_defender_for_storages', value: 'view', },
        { label: 'defender_for_storages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="malware_scanning" /> | `text` | field from the `properties` object |
| <CopyableCode code="override_subscription_level_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sensitive_data_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="settingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Defender for Storage resource properties. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceId, settingName" /> | Gets the Defender for Storage settings for the specified storage account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceId, settingName" /> | Creates or updates the Defender for Storage settings on a specified storage account. |

## `SELECT` examples

Gets the Defender for Storage settings for the specified storage account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_defender_for_storages', value: 'view', },
        { label: 'defender_for_storages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
is_enabled,
malware_scanning,
override_subscription_level_settings,
resourceId,
sensitive_data_discovery,
settingName,
type
FROM azure.security.vw_defender_for_storages
WHERE resourceId = '{{ resourceId }}'
AND settingName = '{{ settingName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.defender_for_storages
WHERE resourceId = '{{ resourceId }}'
AND settingName = '{{ settingName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>defender_for_storages</code> resource.

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
INSERT INTO azure.security.defender_for_storages (
resourceId,
settingName,
properties
)
SELECT 
'{{ resourceId }}',
'{{ settingName }}',
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
        - name: isEnabled
          value: boolean
        - name: malwareScanning
          value:
            - name: onUpload
              value:
                - name: isEnabled
                  value: boolean
                - name: capGBPerMonth
                  value: integer
            - name: scanResultsEventGridTopicResourceId
              value: string
            - name: operationStatus
              value:
                - name: code
                  value: string
                - name: message
                  value: string
        - name: sensitiveDataDiscovery
          value:
            - name: isEnabled
              value: boolean
        - name: overrideSubscriptionLevelSettings
          value: boolean

```
</TabItem>
</Tabs>
