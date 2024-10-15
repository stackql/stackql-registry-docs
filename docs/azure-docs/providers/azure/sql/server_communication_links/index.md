---
title: server_communication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - server_communication_links
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

Creates, updates, deletes, gets or lists a <code>server_communication_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_communication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_communication_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_communication_links', value: 'view', },
        { label: 'server_communication_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="communicationLinkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Communication link kind.  This property is used for Azure Portal metadata. |
| <CopyableCode code="location" /> | `text` | Communication link location. |
| <CopyableCode code="partner_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Communication link kind.  This property is used for Azure Portal metadata. |
| <CopyableCode code="location" /> | `string` | Communication link location. |
| <CopyableCode code="properties" /> | `object` | The properties of a server communication link. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationLinkName, resourceGroupName, serverName, subscriptionId" /> | Returns a server communication link. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server communication links. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="communicationLinkName, resourceGroupName, serverName, subscriptionId" /> | Creates a server communication link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communicationLinkName, resourceGroupName, serverName, subscriptionId" /> | Deletes a server communication link. |

## `SELECT` examples

Gets a list of server communication links.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_communication_links', value: 'view', },
        { label: 'server_communication_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
communicationLinkName,
kind,
location,
partner_server,
resourceGroupName,
serverName,
state,
subscriptionId
FROM azure.sql.vw_server_communication_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.sql.server_communication_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_communication_links</code> resource.

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
INSERT INTO azure.sql.server_communication_links (
communicationLinkName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ communicationLinkName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
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
        - name: state
          value: string
        - name: partnerServer
          value: string
    - name: location
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>server_communication_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.server_communication_links
WHERE communicationLinkName = '{{ communicationLinkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
