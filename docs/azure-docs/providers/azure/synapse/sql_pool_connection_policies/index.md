---
title: sql_pool_connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_connection_policies
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_connection_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_connection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_connection_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_connection_policies', value: 'view', },
        { label: 'sql_pool_connection_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectionPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Resource kind. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="proxy_dns_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="proxy_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="redirection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_enabled_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_server_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="visibility" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Resource kind. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a Sql pool connection policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get a Sql pool's connection policy, which is used with table auditing. |

## `SELECT` examples

Get a Sql pool's connection policy, which is used with table auditing.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_connection_policies', value: 'view', },
        { label: 'sql_pool_connection_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connectionPolicyName,
kind,
location,
proxy_dns_name,
proxy_port,
redirection_state,
resourceGroupName,
security_enabled_access,
sqlPoolName,
state,
subscriptionId,
use_server_default,
visibility,
workspaceName
FROM azure.synapse.vw_sql_pool_connection_policies
WHERE connectionPolicyName = '{{ connectionPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.synapse.sql_pool_connection_policies
WHERE connectionPolicyName = '{{ connectionPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

