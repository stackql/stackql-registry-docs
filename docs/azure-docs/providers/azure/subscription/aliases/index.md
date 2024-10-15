---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
  - subscription
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

Creates, updates, deletes, gets or lists a <code>aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.aliases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_aliases', value: 'view', },
        { label: 'aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified ID for the alias resource. |
| <CopyableCode code="name" /> | `text` | Alias ID. |
| <CopyableCode code="accept_ownership_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="accept_ownership_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="aliasName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reseller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_owner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type, Microsoft.Subscription/aliases. |
| <CopyableCode code="workload" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the alias resource. |
| <CopyableCode code="name" /> | `string` | Alias ID. |
| <CopyableCode code="properties" /> | `object` | Put subscription creation result properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type, Microsoft.Subscription/aliases. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aliasName" /> | Get Alias Subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List Alias Subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="aliasName" /> | Create Alias Subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="aliasName" /> | Delete Alias. |

## `SELECT` examples

List Alias Subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_aliases', value: 'view', },
        { label: 'aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accept_ownership_state,
accept_ownership_url,
aliasName,
billing_scope,
created_time,
display_name,
management_group_id,
provisioning_state,
reseller_id,
subscription_id,
subscription_owner_id,
system_data,
tags,
type,
workload
FROM azure.subscription.vw_aliases
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.subscription.aliases
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>aliases</code> resource.

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
INSERT INTO azure.subscription.aliases (
aliasName,
properties
)
SELECT 
'{{ aliasName }}',
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
        - name: displayName
          value: string
        - name: workload
          value: []
        - name: billingScope
          value: []
        - name: subscriptionId
          value: string
        - name: resellerId
          value: string
        - name: additionalProperties
          value:
            - name: managementGroupId
              value: string
            - name: subscriptionTenantId
              value: string
            - name: subscriptionOwnerId
              value: string
            - name: tags
              value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>aliases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.subscription.aliases
WHERE aliasName = '{{ aliasName }}';
```
