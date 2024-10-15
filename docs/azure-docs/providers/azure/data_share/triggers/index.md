---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - data_share
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

Creates, updates, deletes, gets or lists a <code>triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="kind" /> | `string` | Kind of synchronization on trigger. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId, triggerName" /> | Get a Trigger in a shareSubscription |
| <CopyableCode code="list_by_share_subscription" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | List Triggers in a share subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId, triggerName, data__kind" /> | Create a Trigger  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, shareSubscriptionName, subscriptionId, triggerName" /> | Delete a Trigger in a shareSubscription |

## `SELECT` examples

List Triggers in a share subscription


```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.data_share.triggers
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareSubscriptionName = '{{ shareSubscriptionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>triggers</code> resource.

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
INSERT INTO azure.data_share.triggers (
accountName,
resourceGroupName,
shareSubscriptionName,
subscriptionId,
triggerName,
data__kind,
kind
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ shareSubscriptionName }}',
'{{ subscriptionId }}',
'{{ triggerName }}',
'{{ data__kind }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: systemData
      value:
        - name: createdAt
          value: string
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: lastModifiedAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
    - name: type
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>triggers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_share.triggers
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareSubscriptionName = '{{ shareSubscriptionName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}';
```
