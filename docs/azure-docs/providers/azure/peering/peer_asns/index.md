---
title: peer_asns
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_asns
  - peering
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

Creates, updates, deletes, gets or lists a <code>peer_asns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peer_asns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peer_asns" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peer_asns', value: 'view', },
        { label: 'peer_asns', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="peerAsnName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_contact_detail" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="validation_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a peer's ASN. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peerAsnName, subscriptionId" /> | Gets the peer ASN with the specified name under the given subscription. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the peer ASNs under the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peerAsnName, subscriptionId" /> | Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peerAsnName, subscriptionId" /> | Deletes an existing peer ASN with the specified name under the given subscription. |

## `SELECT` examples

Lists all of the peer ASNs under the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peer_asns', value: 'view', },
        { label: 'peer_asns', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
error_message,
peerAsnName,
peer_asn,
peer_contact_detail,
peer_name,
subscriptionId,
type,
validation_state
FROM azure.peering.vw_peer_asns
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
FROM azure.peering.peer_asns
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>peer_asns</code> resource.

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
INSERT INTO azure.peering.peer_asns (
peerAsnName,
subscriptionId,
properties
)
SELECT 
'{{ peerAsnName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: peerAsn
          value: integer
        - name: peerContactDetail
          value:
            - - name: role
                value: string
              - name: email
                value: string
              - name: phone
                value: string
        - name: peerName
          value: string
        - name: validationState
          value: string
        - name: errorMessage
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>peer_asns</code> resource.

```sql
/*+ delete */
DELETE FROM azure.peering.peer_asns
WHERE peerAsnName = '{{ peerAsnName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
