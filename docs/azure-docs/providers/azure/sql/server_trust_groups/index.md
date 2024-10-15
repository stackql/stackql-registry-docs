---
title: server_trust_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - server_trust_groups
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

Creates, updates, deletes, gets or lists a <code>server_trust_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_trust_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_trust_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_trust_groups', value: 'view', },
        { label: 'server_trust_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="group_members" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverTrustGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="trust_scopes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a server trust group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, serverTrustGroupName, subscriptionId" /> | Gets a server trust group. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists a server trust group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="locationName, resourceGroupName, serverTrustGroupName, subscriptionId" /> | Creates or updates a server trust group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationName, resourceGroupName, serverTrustGroupName, subscriptionId" /> | Deletes a server trust group. |

## `SELECT` examples

Lists a server trust group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_trust_groups', value: 'view', },
        { label: 'server_trust_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
group_members,
locationName,
resourceGroupName,
serverTrustGroupName,
subscriptionId,
trust_scopes
FROM azure.sql.vw_server_trust_groups
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.server_trust_groups
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_trust_groups</code> resource.

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
INSERT INTO azure.sql.server_trust_groups (
locationName,
resourceGroupName,
serverTrustGroupName,
subscriptionId,
properties
)
SELECT 
'{{ locationName }}',
'{{ resourceGroupName }}',
'{{ serverTrustGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: groupMembers
          value:
            - - name: serverId
                value: string
        - name: trustScopes
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>server_trust_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.server_trust_groups
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverTrustGroupName = '{{ serverTrustGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
