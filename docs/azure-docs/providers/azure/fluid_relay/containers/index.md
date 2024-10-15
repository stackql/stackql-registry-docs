---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - fluid_relay
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

Creates, updates, deletes, gets or lists a <code>containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fluid_relay.containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_containers', value: 'view', },
        { label: 'containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="fluidRelayContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fluidRelayServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="frs_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="frs_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_access_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a Fluid Relay Container resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fluidRelayContainerName, fluidRelayServerName, resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="list_by_fluid_relay_servers" /> | `SELECT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fluidRelayContainerName, fluidRelayServerName, resourceGroup, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_containers', value: 'view', },
        { label: 'containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
fluidRelayContainerName,
fluidRelayServerName,
frs_container_id,
frs_tenant_id,
last_access_time,
provisioning_state,
resourceGroup,
subscriptionId,
system_data
FROM azure.fluid_relay.vw_containers
WHERE fluidRelayServerName = '{{ fluidRelayServerName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.fluid_relay.containers
WHERE fluidRelayServerName = '{{ fluidRelayServerName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fluid_relay.containers
WHERE fluidRelayContainerName = '{{ fluidRelayContainerName }}'
AND fluidRelayServerName = '{{ fluidRelayServerName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
