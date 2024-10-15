---
title: bgp_peers
hide_title: false
hide_table_of_contents: false
keywords:
  - bgp_peers
  - k8s_runtime
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

Creates, updates, deletes, gets or lists a <code>bgp_peers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bgp_peers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.k8s_runtime.bgp_peers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bgp_peers', value: 'view', },
        { label: 'bgp_peers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bgpPeerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="my_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Details of the BgpPeer. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bgpPeerName, resourceUri" /> | Get a BgpPeer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List BgpPeer resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bgpPeerName, resourceUri" /> | Create a BgpPeer |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bgpPeerName, resourceUri" /> | Delete a BgpPeer |

## `SELECT` examples

List BgpPeer resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bgp_peers', value: 'view', },
        { label: 'bgp_peers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bgpPeerName,
my_asn,
peer_address,
peer_asn,
provisioning_state,
resourceUri
FROM azure.k8s_runtime.vw_bgp_peers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.k8s_runtime.bgp_peers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bgp_peers</code> resource.

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
INSERT INTO azure.k8s_runtime.bgp_peers (
bgpPeerName,
resourceUri,
properties
)
SELECT 
'{{ bgpPeerName }}',
'{{ resourceUri }}',
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
        - name: myAsn
          value: integer
        - name: peerAsn
          value: integer
        - name: peerAddress
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>bgp_peers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.k8s_runtime.bgp_peers
WHERE bgpPeerName = '{{ bgpPeerName }}'
AND resourceUri = '{{ resourceUri }}';
```
