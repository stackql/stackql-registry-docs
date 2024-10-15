---
title: server_dns_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dns_aliases
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_dns_aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_dns_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_dns_aliases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_dns_aliases', value: 'view', },
        { label: 'server_dns_aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_dns_record" /> | `text` | field from the `properties` object |
| <CopyableCode code="dnsAliasName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a server DNS alias. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId" /> | Gets a server DNS alias. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server DNS aliases for a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId" /> | Creates a server DNS alias. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId" /> | Deletes the server DNS alias with the given name. |
| <CopyableCode code="acquire" /> | `EXEC` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId, data__oldServerDnsAliasId" /> | Acquires server DNS alias from another server. |

## `SELECT` examples

Gets a list of server DNS aliases for a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_dns_aliases', value: 'view', },
        { label: 'server_dns_aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_dns_record,
dnsAliasName,
resourceGroupName,
serverName,
subscriptionId
FROM azure.sql.vw_server_dns_aliases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.server_dns_aliases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_dns_aliases</code> resource.

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
INSERT INTO azure.sql.server_dns_aliases (
dnsAliasName,
resourceGroupName,
serverName,
subscriptionId
)
SELECT 
'{{ dnsAliasName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>server_dns_aliases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.server_dns_aliases
WHERE dnsAliasName = '{{ dnsAliasName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
