---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - web_pubsub
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

Creates, updates, deletes, gets or lists a <code>hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.hubs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hubs', value: 'view', },
        { label: 'hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="anonymous_connect_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_handlers" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_listeners" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_socket_keep_alive_interval_in_seconds" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a hub. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, resourceName, subscriptionId" /> | Get a hub setting. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List hub settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Create or update a hub setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, resourceGroupName, resourceName, subscriptionId" /> | Delete a hub setting. |

## `SELECT` examples

List hub settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hubs', value: 'view', },
        { label: 'hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
anonymous_connect_policy,
event_handlers,
event_listeners,
hubName,
resourceGroupName,
resourceName,
subscriptionId,
web_socket_keep_alive_interval_in_seconds
FROM azure.web_pubsub.vw_hubs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.web_pubsub.hubs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hubs</code> resource.

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
INSERT INTO azure.web_pubsub.hubs (
hubName,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ hubName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: eventHandlers
          value:
            - - name: urlTemplate
                value: string
              - name: userEventPattern
                value: string
              - name: systemEvents
                value:
                  - string
              - name: auth
                value:
                  - name: type
                    value: []
                  - name: managedIdentity
                    value:
                      - name: resource
                        value: string
        - name: eventListeners
          value:
            - - name: filter
                value:
                  - name: type
                    value: string
              - name: endpoint
                value:
                  - name: type
                    value: string
        - name: anonymousConnectPolicy
          value: string
        - name: webSocketKeepAliveIntervalInSeconds
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hubs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.web_pubsub.hubs
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
