---
title: policy_fragments
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_fragments
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

Creates, updates, deletes, gets or lists a <code>policy_fragments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_fragments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.policy_fragments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policy_fragments', value: 'view', },
        { label: 'policy_fragments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Policy fragment contract properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, resourceGroupName, serviceName, subscriptionId" /> | Gets a policy fragment. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets all policy fragments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="id, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates a policy fragment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, id, resourceGroupName, serviceName, subscriptionId" /> | Deletes a policy fragment. |

## `SELECT` examples

Gets all policy fragments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policy_fragments', value: 'view', },
        { label: 'policy_fragments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
description,
format,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId,
value
FROM azure.api_management.vw_policy_fragments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.policy_fragments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_fragments</code> resource.

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
INSERT INTO azure.api_management.policy_fragments (
id,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ id }}',
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
        - name: value
          value: string
        - name: description
          value: string
        - name: format
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>policy_fragments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.policy_fragments
WHERE If-Match = '{{ If-Match }}'
AND id = '{{ id }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
