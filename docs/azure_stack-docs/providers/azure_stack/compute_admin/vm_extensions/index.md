---
title: vm_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_extensions
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>vm_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vm_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.vm_extensions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vm_extensions', value: 'view', },
        { label: 'vm_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="compute_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_system_extension" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_blob" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_multiple_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_scale_set_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a Virtual Machine Extension Image. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, publisher, subscriptionId, type, version" /> | Returns requested Virtual Machine Extension Image matching publisher, type, version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List of all Virtual Machine Extension Images for the current location are returned. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, publisher, subscriptionId, type, version" /> | Create a Virtual Machine Extension Image with publisher, version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, publisher, subscriptionId, type, version" /> | Deletes specified Virtual Machine Extension Image. |

## `SELECT` examples

List of all Virtual Machine Extension Images for the current location are returned.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vm_extensions', value: 'view', },
        { label: 'vm_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
compute_role,
is_system_extension,
location,
provisioning_state,
publisher,
source_blob,
subscriptionId,
support_multiple_extensions,
type,
version,
vm_os_type,
vm_scale_set_enabled
FROM azure_stack.compute_admin.vw_vm_extensions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.compute_admin.vm_extensions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vm_extensions</code> resource.

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
INSERT INTO azure_stack.compute_admin.vm_extensions (
location,
publisher,
subscriptionId,
type,
version,
properties
)
SELECT 
'{{ location }}',
'{{ publisher }}',
'{{ subscriptionId }}',
'{{ type }}',
'{{ version }}',
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
        - name: vmOsType
          value: []
        - name: publisher
          value: string
        - name: computeRole
          value: string
        - name: vmScaleSetEnabled
          value: boolean
        - name: supportMultipleExtensions
          value: boolean
        - name: isSystemExtension
          value: boolean
        - name: sourceBlob
          value:
            - name: uri
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vm_extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.compute_admin.vm_extensions
WHERE location = '{{ location }}'
AND publisher = '{{ publisher }}'
AND subscriptionId = '{{ subscriptionId }}'
AND type = '{{ type }}'
AND version = '{{ version }}';
```
