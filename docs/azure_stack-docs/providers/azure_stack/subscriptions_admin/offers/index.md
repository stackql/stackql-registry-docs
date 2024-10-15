---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
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

Creates, updates, deletes, gets or lists a <code>offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.offers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offers', value: 'view', },
        { label: 'offers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="addon_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="base_plan_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_reference_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="max_subscriptions_per_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Represents an offering of services against which a subscription can be created. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Get the specified offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get the list of offers under a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the list of offers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Create or update the offer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Delete the specified offer. |
| <CopyableCode code="link" /> | `EXEC` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Links a plan to an offer. |
| <CopyableCode code="unlink" /> | `EXEC` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> | Unlink a plan from an offer. |

## `SELECT` examples

Get the list of offers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_offers', value: 'view', },
        { label: 'offers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
addon_plans,
base_plan_ids,
display_name,
external_reference_id,
location,
max_subscriptions_per_account,
offer,
resourceGroupName,
state,
subscriptionId,
subscription_count,
tags,
type
FROM azure_stack.subscriptions_admin.vw_offers
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure_stack.subscriptions_admin.offers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>offers</code> resource.

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
INSERT INTO azure_stack.subscriptions_admin.offers (
offer,
resourceGroupName,
subscriptionId,
properties,
location
)
SELECT 
'{{ offer }}',
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
        - name: name
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: externalReferenceId
          value: string
        - name: state
          value: []
        - name: subscriptionCount
          value: integer
        - name: maxSubscriptionsPerAccount
          value: integer
        - name: basePlanIds
          value:
            - string
        - name: addonPlans
          value:
            - - name: planId
                value: string
              - name: maxAcquisitionCount
                value: integer
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

Deletes the specified <code>offers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.subscriptions_admin.offers
WHERE offer = '{{ offer }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
