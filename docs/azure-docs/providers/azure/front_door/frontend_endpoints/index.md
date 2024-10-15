---
title: frontend_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - frontend_endpoints
  - front_door
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

Creates, updates, deletes, gets or lists a <code>frontend_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frontend_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.frontend_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_frontend_endpoints', value: 'view', },
        { label: 'frontend_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="custom_https_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_https_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_https_provisioning_substate" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontDoorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontendEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_affinity_enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_affinity_ttl_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="web_application_firewall_policy_link" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a frontend endpoint. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId" /> | Gets a Frontend endpoint with the specified name within the specified Front Door. |
| <CopyableCode code="list_by_front_door" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Lists all of the frontend endpoints within a Front Door. |
| <CopyableCode code="disable_https" /> | `EXEC` | <CopyableCode code="frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId" /> | Disables a frontendEndpoint for HTTPS traffic |
| <CopyableCode code="enable_https" /> | `EXEC` | <CopyableCode code="frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId, data__certificateSource, data__minimumTlsVersion, data__protocolType" /> | Enables a frontendEndpoint for HTTPS traffic |

## `SELECT` examples

Lists all of the frontend endpoints within a Front Door.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_frontend_endpoints', value: 'view', },
        { label: 'frontend_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_https_configuration,
custom_https_provisioning_state,
custom_https_provisioning_substate,
frontDoorName,
frontendEndpointName,
host_name,
resourceGroupName,
resource_state,
session_affinity_enabled_state,
session_affinity_ttl_seconds,
subscriptionId,
type,
web_application_firewall_policy_link
FROM azure.front_door.vw_frontend_endpoints
WHERE frontDoorName = '{{ frontDoorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.front_door.frontend_endpoints
WHERE frontDoorName = '{{ frontDoorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

