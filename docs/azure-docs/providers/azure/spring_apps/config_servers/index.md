---
title: config_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - config_servers
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>config_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.config_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_config_servers', value: 'view', },
        { label: 'config_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="config_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Config server git properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get the config server and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all config server resources in a Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Disable the default Config Server, only available in Enterprise Plan. |
| <CopyableCode code="update_patch" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Update the config server. |
| <CopyableCode code="update_put" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Update the config server. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Check if the config server settings are valid. |

## `SELECT` examples

Get the config server and its properties.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_config_servers', value: 'view', },
        { label: 'config_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
config_server,
enabled_state,
error,
instances,
provisioning_state,
resourceGroupName,
resource_requests,
serviceName,
subscriptionId
FROM azure.spring_apps.vw_config_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.config_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>config_servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.config_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
