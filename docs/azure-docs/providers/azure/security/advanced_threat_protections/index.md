---
title: advanced_threat_protections
hide_title: false
hide_table_of_contents: false
keywords:
  - advanced_threat_protections
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

Creates, updates, deletes, gets or lists a <code>advanced_threat_protections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>advanced_threat_protections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.advanced_threat_protections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_advanced_threat_protections', value: 'view', },
        { label: 'advanced_threat_protections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="settingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The Advanced Threat Protection settings. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceId, settingName" /> | Gets the Advanced Threat Protection settings for the specified resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceId, settingName" /> | Creates or updates the Advanced Threat Protection settings on a specified resource. |

## `SELECT` examples

Gets the Advanced Threat Protection settings for the specified resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_advanced_threat_protections', value: 'view', },
        { label: 'advanced_threat_protections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
is_enabled,
resourceId,
settingName,
type
FROM azure.security.vw_advanced_threat_protections
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
FROM azure.security.advanced_threat_protections
WHERE resourceId = '{{ resourceId }}'
AND settingName = '{{ settingName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>advanced_threat_protections</code> resource.

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
INSERT INTO azure.security.advanced_threat_protections (
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

```
</TabItem>
</Tabs>
