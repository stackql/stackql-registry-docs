---
title: file_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - file_containers
  - deployment_admin
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

Creates, updates, deletes, gets or lists a <code>file_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.file_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_containers', value: 'view', },
        { label: 'file_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileContainerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="post_copy_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | File Container Properties. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileContainerId, subscriptionId" /> | Retrieves the specific file container details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns an array of file containers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fileContainerId, subscriptionId" /> | Creates a new file container. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fileContainerId, subscriptionId" /> | Delete an existing file container. |

## `SELECT` examples

Returns an array of file containers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_containers', value: 'view', },
        { label: 'file_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
error,
fileContainerId,
file_container_id,
location,
post_copy_action,
provisioning_state,
source_uri,
subscriptionId,
type,
uri
FROM azure_stack.deployment_admin.vw_file_containers
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure_stack.deployment_admin.file_containers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>file_containers</code> resource.

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
INSERT INTO azure_stack.deployment_admin.file_containers (
fileContainerId,
subscriptionId,
properties
)
SELECT 
'{{ fileContainerId }}',
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
        - name: postCopyAction
          value: []
        - name: sourceUri
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>file_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.deployment_admin.file_containers
WHERE fileContainerId = '{{ fileContainerId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
