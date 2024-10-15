---
title: workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
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

Creates, updates, deletes, gets or lists a <code>workspace_managed_sql_server_dedicated_sql_minimal_tls_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_dedicated_sql_minimal_tls_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_dedicated_sql_minimal_tls_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_managed_sql_server_dedicated_sql_minimal_tls_settings', value: 'view', },
        { label: 'workspace_managed_sql_server_dedicated_sql_minimal_tls_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dedicatedSQLminimalTlsSettingsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="minimal_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a dedicated sql minimal tls settings. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dedicatedSQLminimalTlsSettingsName, resourceGroupName, subscriptionId, workspaceName" /> | Get workspace managed sql server's minimal tls settings. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List workspace managed sql server's minimal tls settings. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="dedicatedSQLminimalTlsSettingsName, resourceGroupName, subscriptionId, workspaceName" /> | Update workspace managed sql server's minimal tls settings. |

## `SELECT` examples

List workspace managed sql server's minimal tls settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_managed_sql_server_dedicated_sql_minimal_tls_settings', value: 'view', },
        { label: 'workspace_managed_sql_server_dedicated_sql_minimal_tls_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dedicatedSQLminimalTlsSettingsName,
location,
minimal_tls_version,
resourceGroupName,
subscriptionId,
workspaceName
FROM azure.synapse.vw_workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure.synapse.workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>workspace_managed_sql_server_dedicated_sql_minimal_tls_settings</code> resource.

```sql
/*+ update */
REPLACE azure.synapse.workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
SET 
properties = '{{ properties }}'
WHERE 
dedicatedSQLminimalTlsSettingsName = '{{ dedicatedSQLminimalTlsSettingsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
