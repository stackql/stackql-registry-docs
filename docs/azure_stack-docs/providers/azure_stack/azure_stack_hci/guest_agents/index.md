---
title: guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_agents
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>guest_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>guest_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.guest_agents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_guest_agents', value: 'view', },
        { label: 'guest_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Implements GuestAgent GET method. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Returns the list of GuestAgent of the given vm. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceUri, data__properties" /> | Create Or Update GuestAgent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | Implements GuestAgent DELETE method. |

## `SELECT` examples

Implements GuestAgent GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_guest_agents', value: 'view', },
        { label: 'guest_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
credentials,
provisioning_action,
provisioning_state,
resourceUri,
status,
system_data
FROM azure_stack.azure_stack_hci.vw_guest_agents
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_stack.azure_stack_hci.guest_agents
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>guest_agents</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.guest_agents (
resourceUri,
data__properties,
properties,
systemData
)
SELECT 
'{{ resourceUri }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: credentials
          value:
            - name: username
              value: string
            - name: password
              value: string
        - name: provisioningAction
          value: []
        - name: status
          value: string
        - name: provisioningState
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>guest_agents</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.guest_agents
WHERE resourceUri = '{{ resourceUri }}';
```
