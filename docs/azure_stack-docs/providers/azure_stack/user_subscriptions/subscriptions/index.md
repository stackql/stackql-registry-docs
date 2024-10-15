---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - user_subscriptions
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.user_subscriptions.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier. |
| <CopyableCode code="displayName" /> | `string` | Subscription name. |
| <CopyableCode code="offerId" /> | `string` | Identifier of the offer under the scope of a delegated provider. |
| <CopyableCode code="state" /> | `string` | Subscription notification state. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription identifier. |
| <CopyableCode code="tenantId" /> | `string` | Directory tenant identifier. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets details about particular subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the list of subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId" /> | Create or updates a subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId" /> | Delete the specified subscription. |

## `SELECT` examples

Get the list of subscriptions.


```sql
SELECT
id,
displayName,
offerId,
state,
subscriptionId,
tenantId
FROM azure_stack.user_subscriptions.subscriptions
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriptions</code> resource.

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
INSERT INTO azure_stack.user_subscriptions.subscriptions (
subscriptionId,
displayName,
id,
offerId,
state,
subscriptionId,
tenantId
)
SELECT 
'{{ subscriptionId }}',
'{{ displayName }}',
'{{ id }}',
'{{ offerId }}',
'{{ state }}',
'{{ subscriptionId }}',
'{{ tenantId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: id
      value: string
    - name: offerId
      value: string
    - name: state
      value: []
    - name: subscriptionId
      value: string
    - name: tenantId
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.user_subscriptions.subscriptions
WHERE subscriptionId = '{{ subscriptionId }}';
```
