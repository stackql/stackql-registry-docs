---
title: vm_instance_guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_instance_guest_agents
  - connected_vsphere
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

Creates, updates, deletes, gets or lists a <code>vm_instance_guest_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vm_instance_guest_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.vm_instance_guest_agents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vm_instance_guest_agents', value: 'view', },
        { label: 'vm_instance_guest_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_proxy_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_scope_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Guest Agent. |
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
        { label: 'vw_vm_instance_guest_agents', value: 'view', },
        { label: 'vm_instance_guest_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
credentials,
custom_resource_name,
http_proxy_config,
private_link_scope_resource_id,
provisioning_action,
provisioning_state,
resourceUri,
status,
statuses,
uuid
FROM azure_isv.connected_vsphere.vw_vm_instance_guest_agents
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.connected_vsphere.vm_instance_guest_agents
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vm_instance_guest_agents</code> resource.

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
INSERT INTO azure_isv.connected_vsphere.vm_instance_guest_agents (
resourceUri,
data__properties,
properties
)
SELECT 
'{{ resourceUri }}',
'{{ data__properties }}',
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
        - name: uuid
          value: string
        - name: credentials
          value:
            - name: username
              value: string
            - name: password
              value: string
            - name: privateKey
              value: string
        - name: privateLinkScopeResourceId
          value: string
        - name: httpProxyConfig
          value:
            - name: httpsProxy
              value: string
        - name: provisioningAction
          value: []
        - name: status
          value: string
        - name: customResourceName
          value: string
        - name: statuses
          value:
            - - name: type
                value: string
              - name: status
                value: string
              - name: reason
                value: string
              - name: message
                value: string
              - name: severity
                value: string
              - name: lastUpdatedAt
                value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vm_instance_guest_agents</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.connected_vsphere.vm_instance_guest_agents
WHERE resourceUri = '{{ resourceUri }}';
```
