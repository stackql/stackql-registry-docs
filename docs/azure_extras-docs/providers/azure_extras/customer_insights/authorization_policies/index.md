---
title: authorization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policies
  - customer_insights
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

Creates, updates, deletes, gets or lists a <code>authorization_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.authorization_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_policies', value: 'view', },
        { label: 'authorization_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="authorizationPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The authorization policy. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Gets an authorization policy in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the authorization policies in a specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Creates an authorization policy or updates an existing authorization policy. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Regenerates the primary policy key of the specified authorization policy. |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Regenerates the secondary policy key of the specified authorization policy. |

## `SELECT` examples

Gets all the authorization policies in a specified hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorization_policies', value: 'view', },
        { label: 'authorization_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authorizationPolicyName,
hubName,
permissions,
policy_name,
primary_key,
resourceGroupName,
secondary_key,
subscriptionId,
type
FROM azure_extras.customer_insights.vw_authorization_policies
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_extras.customer_insights.authorization_policies
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorization_policies</code> resource.

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
INSERT INTO azure_extras.customer_insights.authorization_policies (
authorizationPolicyName,
hubName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ authorizationPolicyName }}',
'{{ hubName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: policyName
          value: string
        - name: permissions
          value:
            - []
        - name: primaryKey
          value: string
        - name: secondaryKey
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>
