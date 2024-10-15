---
title: dapr_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - dapr_subscriptions
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>dapr_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dapr_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.dapr_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Dapr PubSub Event Subscription resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Creates or updates a Dapr subscription in a Managed Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Delete a Dapr subscription from a Managed Environment. |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.dapr_subscriptions
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dapr_subscriptions</code> resource.

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
INSERT INTO azure.container_apps.dapr_subscriptions (
environmentName,
name,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ environmentName }}',
'{{ name }}',
'{{ resourceGroupName }}',
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
        - name: pubsubName
          value: string
        - name: topic
          value: string
        - name: deadLetterTopic
          value: string
        - name: routes
          value:
            - name: rules
              value:
                - - name: match
                    value: string
                  - name: path
                    value: string
            - name: default
              value: string
        - name: scopes
          value:
            - string
        - name: metadata
          value: object
        - name: bulkSubscribe
          value:
            - name: enabled
              value: boolean
            - name: maxMessagesCount
              value: integer
            - name: maxAwaitDurationMs
              value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dapr_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.dapr_subscriptions
WHERE environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
