---
title: auto_provisioning_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_provisioning_settings
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

Creates, updates, deletes, gets or lists a <code>auto_provisioning_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_provisioning_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.auto_provisioning_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_auto_provisioning_settings', value: 'view', },
        { label: 'auto_provisioning_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="auto_provision" /> | `text` | field from the `properties` object |
| <CopyableCode code="settingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes properties of an auto provisioning setting |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="settingName, subscriptionId" /> | Details of a specific setting |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Exposes the auto provisioning settings of the subscriptions |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="settingName, subscriptionId" /> | Details of a specific setting |

## `SELECT` examples

Exposes the auto provisioning settings of the subscriptions

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_auto_provisioning_settings', value: 'view', },
        { label: 'auto_provisioning_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auto_provision,
settingName,
subscriptionId,
type
FROM azure.security.vw_auto_provisioning_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.auto_provisioning_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>auto_provisioning_settings</code> resource.

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
INSERT INTO azure.security.auto_provisioning_settings (
settingName,
subscriptionId,
properties
)
SELECT 
'{{ settingName }}',
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
        - name: autoProvision
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>
