---
title: packet_core_control_plane_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_control_plane_versions
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>packet_core_control_plane_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_core_control_plane_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_core_control_plane_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_core_control_plane_versions', value: 'view', },
        { label: 'packet_core_control_plane_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="platforms" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="versionName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Packet core control plane version properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="versionName" /> | Gets information about the specified packet core control plane version. |
| <CopyableCode code="get_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId, versionName" /> | Gets information about the specified packet core control plane version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all supported packet core control planes versions. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all supported packet core control planes versions. |

## `SELECT` examples

Lists all supported packet core control planes versions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_core_control_plane_versions', value: 'view', },
        { label: 'packet_core_control_plane_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
platforms,
provisioning_state,
subscriptionId,
versionName
FROM azure.mobile_network.vw_packet_core_control_plane_versions
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mobile_network.packet_core_control_plane_versions
;
```
</TabItem></Tabs>

