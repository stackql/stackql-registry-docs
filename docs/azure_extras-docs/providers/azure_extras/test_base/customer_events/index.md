---
title: customer_events
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_events
  - test_base
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

Creates, updates, deletes, gets or lists a <code>customer_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.customer_events" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customer_events', value: 'view', },
        { label: 'customer_events', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="customerEventName" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="receivers" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A notification events subscribed to be received by customer. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerEventName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base CustomerEvent. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all notification events subscribed under a Test Base Account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customerEventName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace a Test Base Customer Event. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customerEventName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Customer Event. |

## `SELECT` examples

Lists all notification events subscribed under a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customer_events', value: 'view', },
        { label: 'customer_events', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
customerEventName,
event_name,
receivers,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_customer_events
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.customer_events
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>customer_events</code> resource.

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
INSERT INTO azure_extras.test_base.customer_events (
customerEventName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties
)
SELECT 
'{{ customerEventName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testBaseAccountName }}',
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
        - name: eventName
          value: string
        - name: receivers
          value:
            - - name: receiverType
                value: string
              - name: receiverValue
                value:
                  - name: userObjectReceiverValue
                    value:
                      - name: userObjectIds
                        value:
                          - string
                  - name: subscriptionReceiverValue
                    value:
                      - name: subscriptionId
                        value: string
                      - name: subscriptionName
                        value: string
                      - name: role
                        value: string
                  - name: distributionGroupListReceiverValue
                    value:
                      - name: distributionGroups
                        value:
                          - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>customer_events</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.customer_events
WHERE customerEventName = '{{ customerEventName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
