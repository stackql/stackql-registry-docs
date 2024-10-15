---
title: offer_delegations
hide_title: false
hide_table_of_contents: false
keywords:
  - offer_delegations
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

Creates, updates, deletes, gets or lists a <code>offer_delegations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offer_delegations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.offer_delegations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offer_delegations', value: 'view', },
        { label: 'offer_delegations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerDelegationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for an offer delegation. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offer, offerDelegationName, resourceGroupName, subscriptionId" /> | Get the specified offer delegation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Get the list of offer delegations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="offer, offerDelegationName, resourceGroupName, subscriptionId" /> | Create or update the offer delegation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="offer, offerDelegationName, resourceGroupName, subscriptionId" /> | Delete the specified offer delegation. |

## `SELECT` examples

Get the list of offer delegations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offer_delegations', value: 'view', },
        { label: 'offer_delegations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
offer,
offerDelegationName,
resourceGroupName,
subscriptionId,
subscription_id,
tags,
type
FROM azure_stack.subscriptions_admin.vw_offer_delegations
WHERE offer = '{{ offer }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.subscriptions_admin.offer_delegations
WHERE offer = '{{ offer }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>offer_delegations</code> resource.

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
INSERT INTO azure_stack.subscriptions_admin.offer_delegations (
offer,
offerDelegationName,
resourceGroupName,
subscriptionId,
properties,
location
)
SELECT 
'{{ offer }}',
'{{ offerDelegationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: subscriptionId
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>offer_delegations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.subscriptions_admin.offer_delegations
WHERE offer = '{{ offer }}'
AND offerDelegationName = '{{ offerDelegationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
