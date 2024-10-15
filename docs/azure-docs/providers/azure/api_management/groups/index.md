---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - api_management
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_groups', value: 'view', },
        { label: 'groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="built_in" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Group contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the group specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of groups defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, groupId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific group of the API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, groupId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the group specified by its identifier. |

## `SELECT` examples

Lists a collection of groups defined within a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_groups', value: 'view', },
        { label: 'groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
built_in,
display_name,
external_id,
groupId,
resourceGroupName,
serviceName,
subscriptionId,
type
FROM azure.api_management.vw_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

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
INSERT INTO azure.api_management.groups (
groupId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ groupId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: displayName
          value: string
        - name: description
          value: string
        - name: type
          value: string
        - name: externalId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>groups</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.groups
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND groupId = '{{ groupId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.groups
WHERE If-Match = '{{ If-Match }}'
AND groupId = '{{ groupId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
