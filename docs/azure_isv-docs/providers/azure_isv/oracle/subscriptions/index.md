---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - oracle
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Oracle Subscription resource model |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a OracleSubscription |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List OracleSubscription resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId" /> | Create a OracleSubscription |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId" /> | Delete a OracleSubscription |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="subscriptionId" /> | Update a OracleSubscription |
| <CopyableCode code="add_azure_subscriptions" /> | `EXEC` | <CopyableCode code="subscriptionId, data__azureSubscriptionIds" /> | Add Azure Subscriptions |

## `SELECT` examples

Get a OracleSubscription


```sql
SELECT
plan,
properties
FROM azure_isv.oracle.subscriptions
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
INSERT INTO azure_isv.oracle.subscriptions (
subscriptionId,
properties,
plan
)
SELECT 
'{{ subscriptionId }}',
'{{ properties }}',
'{{ plan }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: saasSubscriptionId
          value: string
        - name: cloudAccountId
          value: []
        - name: cloudAccountState
          value: []
        - name: termUnit
          value: string
        - name: productCode
          value: string
        - name: intent
          value: []
        - name: azureSubscriptionIds
          value:
            - string
        - name: addSubscriptionOperationState
          value: []
        - name: lastOperationStatusDetail
          value: string
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: version
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure_isv.oracle.subscriptions
SET 
plan = '{{ plan }}',
properties = '{{ properties }}'
WHERE 
subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.oracle.subscriptions
WHERE subscriptionId = '{{ subscriptionId }}';
```
