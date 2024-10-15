---
title: onboarding_states
hide_title: false
hide_table_of_contents: false
keywords:
  - onboarding_states
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>onboarding_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>onboarding_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.onboarding_states" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_onboarding_states', value: 'view', },
        { label: 'onboarding_states', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="customer_managed_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sentinelOnboardingStateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | The Sentinel onboarding state properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName" /> | Get Sentinel onboarding state |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all Sentinel onboarding states |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName" /> | Create Sentinel onboarding state |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName" /> | Delete Sentinel onboarding state |

## `SELECT` examples

Gets all Sentinel onboarding states

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_onboarding_states', value: 'view', },
        { label: 'onboarding_states', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
customer_managed_key,
etag,
resourceGroupName,
sentinelOnboardingStateName,
subscriptionId,
workspaceName
FROM azure.sentinel.vw_onboarding_states
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.onboarding_states
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>onboarding_states</code> resource.

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
INSERT INTO azure.sentinel.onboarding_states (
resourceGroupName,
sentinelOnboardingStateName,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sentinelOnboardingStateName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: customerManagedKey
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>onboarding_states</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.onboarding_states
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sentinelOnboardingStateName = '{{ sentinelOnboardingStateName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
