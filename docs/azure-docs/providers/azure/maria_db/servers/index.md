---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - maria_db
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.servers" /></td></tr>
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
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="master_server_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimal_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="ssl_enforcement" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_visible_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a server. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets information about a server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the servers in a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the servers in a given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__location, data__properties" /> | Creates a new server or updates an existing server. The update action will overwrite the existing server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Deletes a server. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Restarts a server. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Starts a stopped server. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Stops a running server. |

## `SELECT` examples

List all the servers in a given subscription.

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
earliest_restore_date,
fully_qualified_domain_name,
location,
master_server_id,
minimal_tls_version,
private_endpoint_connections,
public_network_access,
replica_capacity,
replication_role,
resourceGroupName,
serverName,
sku,
ssl_enforcement,
storage_profile,
subscriptionId,
tags,
user_visible_state,
version
FROM azure.maria_db.vw_servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.maria_db.servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>servers</code> resource.

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
INSERT INTO azure.maria_db.servers (
resourceGroupName,
serverName,
subscriptionId,
data__location,
data__properties,
sku,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ sku }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: version
          value: []
        - name: sslEnforcement
          value: []
        - name: minimalTlsVersion
          value: []
        - name: publicNetworkAccess
          value: []
        - name: storageProfile
          value:
            - name: backupRetentionDays
              value: integer
            - name: geoRedundantBackup
              value: string
            - name: storageMB
              value: integer
            - name: storageAutogrow
              value: string
        - name: createMode
          value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>servers</code> resource.

```sql
/*+ update */
UPDATE azure.maria_db.servers
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.maria_db.servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
