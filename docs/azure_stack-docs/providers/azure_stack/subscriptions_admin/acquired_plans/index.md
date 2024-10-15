---
title: acquired_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - acquired_plans
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

Creates, updates, deletes, gets or lists a <code>acquired_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acquired_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.acquired_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier in the tenant subscription context. |
| <CopyableCode code="acquisitionId" /> | `string` | Acquisition identifier. |
| <CopyableCode code="acquisitionTime" /> | `string` | Acquisition time. |
| <CopyableCode code="externalReferenceId" /> | `string` | External reference identifier. |
| <CopyableCode code="planId" /> | `string` | Plan identifier in the tenant subscription context. |
| <CopyableCode code="provisioningState" /> | `string` | Provisioning state for subscriptions service resources, for example, resource provider registration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planAcquisitionId, subscriptionId, targetSubscriptionId" /> | Gets the specified plan acquired by a subscription consuming the offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId, targetSubscriptionId" /> | Get a collection of all acquired plans that subscription has access to. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="planAcquisitionId, subscriptionId, targetSubscriptionId" /> | Creates an acquired plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planAcquisitionId, subscriptionId, targetSubscriptionId" /> | Deletes an acquired plan. |

## `SELECT` examples

Get a collection of all acquired plans that subscription has access to.


```sql
SELECT
id,
acquisitionId,
acquisitionTime,
externalReferenceId,
planId,
provisioningState
FROM azure_stack.subscriptions_admin.acquired_plans
WHERE subscriptionId = '{{ subscriptionId }}'
AND targetSubscriptionId = '{{ targetSubscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>acquired_plans</code> resource.

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
INSERT INTO azure_stack.subscriptions_admin.acquired_plans (
planAcquisitionId,
subscriptionId,
targetSubscriptionId,
acquisitionId,
id,
planId,
externalReferenceId,
provisioningState,
acquisitionTime
)
SELECT 
'{{ planAcquisitionId }}',
'{{ subscriptionId }}',
'{{ targetSubscriptionId }}',
'{{ acquisitionId }}',
'{{ id }}',
'{{ planId }}',
'{{ externalReferenceId }}',
'{{ provisioningState }}',
'{{ acquisitionTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: acquisitionId
      value: string
    - name: id
      value: string
    - name: planId
      value: string
    - name: externalReferenceId
      value: string
    - name: provisioningState
      value: []
    - name: acquisitionTime
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>acquired_plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.subscriptions_admin.acquired_plans
WHERE planAcquisitionId = '{{ planAcquisitionId }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetSubscriptionId = '{{ targetSubscriptionId }}';
```
