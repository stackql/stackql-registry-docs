---
title: policy_restrictions
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_restrictions
  - api_management
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

Creates, updates, deletes, gets or lists a <code>policy_restrictions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_restrictions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.policy_restrictions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policy_restrictions', value: 'view', },
        { label: 'policy_restrictions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="policyRestrictionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="require_base" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Policy restrictions contract properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Get the policy restriction of the Api Management service. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets all policy restrictions of API Management services. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates the policy restriction configuration of the Api Management service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the policy restriction configuration of the Api Management Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Updates the policy restriction configuration of the Api Management service. |

## `SELECT` examples

Gets all policy restrictions of API Management services.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policy_restrictions', value: 'view', },
        { label: 'policy_restrictions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
policyRestrictionId,
require_base,
resourceGroupName,
scope,
serviceName,
subscriptionId
FROM azure.api_management.vw_policy_restrictions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.policy_restrictions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_restrictions</code> resource.

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
INSERT INTO azure.api_management.policy_restrictions (
policyRestrictionId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ policyRestrictionId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: scope
          value: string
        - name: requireBase
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>policy_restrictions</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.policy_restrictions
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND policyRestrictionId = '{{ policyRestrictionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>policy_restrictions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.policy_restrictions
WHERE policyRestrictionId = '{{ policyRestrictionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
