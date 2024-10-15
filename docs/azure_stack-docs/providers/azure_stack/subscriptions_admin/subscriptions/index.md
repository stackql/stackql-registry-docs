---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - subscriptions_admin
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier. |
| <CopyableCode code="delegatedProviderSubscriptionId" /> | `string` | Parent DelegatedProvider subscription identifier. |
| <CopyableCode code="displayName" /> | `string` | Subscription name. |
| <CopyableCode code="externalReferenceId" /> | `string` | External reference identifier. |
| <CopyableCode code="offerId" /> | `string` | Identifier of the offer under the scope of a delegated provider. |
| <CopyableCode code="owner" /> | `string` | Subscription owner. |
| <CopyableCode code="routingResourceManagerType" /> | `string` | Resource manager type. |
| <CopyableCode code="state" /> | `string` | Subscription notification state. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription identifier. |
| <CopyableCode code="tenantId" /> | `string` | Directory tenant identifier. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Get a specified subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the list of subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Creates or updates the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Delete the specified subscription. |
| <CopyableCode code="check_identity_health" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Checks the identity health |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get the list of subscriptions. |
| <CopyableCode code="move_subscriptions" /> | `EXEC` | <CopyableCode code="subscriptionId, data__resources" /> | Move subscriptions between delegated provider offers. |
| <CopyableCode code="restore_data" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Restores the data |
| <CopyableCode code="validate_move_subscriptions" /> | `EXEC` | <CopyableCode code="subscriptionId, data__resources" /> | Validate that user subscriptions can be moved between delegated provider offers. |

## `SELECT` examples

Get the list of subscriptions.


```sql
SELECT
id,
delegatedProviderSubscriptionId,
displayName,
externalReferenceId,
offerId,
owner,
routingResourceManagerType,
state,
subscriptionId,
tenantId
FROM azure_stack.subscriptions_admin.subscriptions
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure_stack.subscriptions_admin.subscriptions (
subscriptionId,
targetSubscriptionId,
delegatedProviderSubscriptionId,
displayName,
id,
externalReferenceId,
offerId,
owner,
routingResourceManagerType,
state,
subscriptionId,
tenantId
)
SELECT 
'{{ subscriptionId }}',
'{{ targetSubscriptionId }}',
'{{ delegatedProviderSubscriptionId }}',
'{{ displayName }}',
'{{ id }}',
'{{ externalReferenceId }}',
'{{ offerId }}',
'{{ owner }}',
'{{ routingResourceManagerType }}',
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
    - name: delegatedProviderSubscriptionId
      value: string
    - name: displayName
      value: string
    - name: id
      value: string
    - name: externalReferenceId
      value: string
    - name: offerId
      value: string
    - name: owner
      value: string
    - name: routingResourceManagerType
      value: []
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
DELETE FROM azure_stack.subscriptions_admin.subscriptions
WHERE subscriptionId = '{{ subscriptionId }}'
AND targetSubscriptionId = '{{ targetSubscriptionId }}';
```
