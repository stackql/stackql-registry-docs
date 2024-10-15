---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - postgresql_hsc
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator_login" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="citus_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ha" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_public_ip_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="ha_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_read_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="postgresql_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_quota_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_cores" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a server in cluster. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, serverName, subscriptionId" /> | Gets information about a server in cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists servers of a cluster. |

## `SELECT` examples

Lists servers of a cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator_login,
availability_zone,
citus_version,
clusterName,
enable_ha,
enable_public_ip_access,
fully_qualified_domain_name,
ha_state,
is_read_only,
postgresql_version,
resourceGroupName,
role,
serverName,
server_edition,
state,
storage_quota_in_mb,
subscriptionId,
v_cores
FROM azure.postgresql_hsc.vw_servers
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql_hsc.servers
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

