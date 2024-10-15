---
title: information_protection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - information_protection_policies
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

Creates, updates, deletes, gets or lists a <code>information_protection_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>information_protection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.information_protection_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_information_protection_policies', value: 'view', },
        { label: 'information_protection_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="informationProtectionPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="information_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes properties of an information protection policy. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="informationProtectionPolicyName, scope" /> | Details of the information protection policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Information protection policies of a specific management group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="informationProtectionPolicyName, scope" /> | Details of the information protection policy. |

## `SELECT` examples

Information protection policies of a specific management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_information_protection_policies', value: 'view', },
        { label: 'information_protection_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
informationProtectionPolicyName,
information_types,
labels,
last_modified_utc,
scope,
type,
version
FROM azure.security.vw_information_protection_policies
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.information_protection_policies
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>information_protection_policies</code> resource.

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
INSERT INTO azure.security.information_protection_policies (
informationProtectionPolicyName,
scope,
properties
)
SELECT 
'{{ informationProtectionPolicyName }}',
'{{ scope }}',
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
        - name: lastModifiedUtc
          value: string
        - name: version
          value: string
        - name: labels
          value: object
        - name: informationTypes
          value: object
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>
