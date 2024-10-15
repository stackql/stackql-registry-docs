---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - postgresql
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configurations', value: 'view', },
        { label: 'configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_values" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="documentation_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_config_pending_restart" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_dynamic_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_read_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a configuration. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, resourceGroupName, serverName, subscriptionId" /> | Gets information about a configuration of server. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the configurations in a given server. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="configurationName, resourceGroupName, serverName, subscriptionId" /> | Updates a configuration of a server. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="configurationName, resourceGroupName, serverName, subscriptionId" /> | Updates a configuration of a server. |

## `SELECT` examples

List all the configurations in a given server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configurations', value: 'view', },
        { label: 'configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
allowed_values,
configurationName,
data_type,
default_value,
documentation_link,
is_config_pending_restart,
is_dynamic_config,
is_read_only,
resourceGroupName,
serverName,
source,
subscriptionId,
unit,
value
FROM azure.postgresql.vw_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql.configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>configurations</code> resource.

```sql
/*+ update */
UPDATE azure.postgresql.configurations
SET 
properties = '{{ properties }}'
WHERE 
configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>configurations</code> resource.

```sql
/*+ update */
REPLACE azure.postgresql.configurations
SET 
properties = '{{ properties }}'
WHERE 
configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
