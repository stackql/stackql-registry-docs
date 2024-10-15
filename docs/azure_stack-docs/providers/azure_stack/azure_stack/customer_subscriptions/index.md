---
title: customer_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_subscriptions
  - azure_stack
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

Creates, updates, deletes, gets or lists a <code>customer_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.customer_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customer_subscriptions', value: 'view', },
        { label: 'customer_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="customerSubscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="registrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="etag" /> | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="properties" /> | `object` | Customer subscription properties. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerSubscriptionName, registrationName, resourceGroup, subscriptionId" /> | Returns the specified product. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customerSubscriptionName, registrationName, resourceGroup, subscriptionId" /> | Creates a new customer subscription under a registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customerSubscriptionName, registrationName, resourceGroup, subscriptionId" /> | Deletes a customer subscription under a registration. |

## `SELECT` examples

Returns a list of products.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customer_subscriptions', value: 'view', },
        { label: 'customer_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
customerSubscriptionName,
etag,
registrationName,
resourceGroup,
subscriptionId,
tenant_id,
type
FROM azure_stack.azure_stack.vw_customer_subscriptions
WHERE registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure_stack.azure_stack.customer_subscriptions
WHERE registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>customer_subscriptions</code> resource.

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
INSERT INTO azure_stack.azure_stack.customer_subscriptions (
customerSubscriptionName,
registrationName,
resourceGroup,
subscriptionId,
properties,
etag
)
SELECT 
'{{ customerSubscriptionName }}',
'{{ registrationName }}',
'{{ resourceGroup }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: tenantId
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>customer_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack.customer_subscriptions
WHERE customerSubscriptionName = '{{ customerSubscriptionName }}'
AND registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
