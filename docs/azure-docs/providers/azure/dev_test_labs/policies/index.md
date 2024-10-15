---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="evaluator_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="fact_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="fact_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="policySetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="threshold" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a Policy. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, policySetName, resourceGroupName, subscriptionId" /> | Get policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, policySetName, resourceGroupName, subscriptionId" /> | List policies in a given policy set. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, policySetName, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, policySetName, resourceGroupName, subscriptionId" /> | Delete policy. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, policySetName, resourceGroupName, subscriptionId" /> | Allows modifying tags of policies. All other properties will be ignored. |

## `SELECT` examples

List policies in a given policy set.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
created_date,
evaluator_type,
fact_data,
fact_name,
labName,
location,
policySetName,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
threshold,
type,
unique_identifier
FROM azure.dev_test_labs.vw_policies
WHERE labName = '{{ labName }}'
AND policySetName = '{{ policySetName }}'
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
FROM azure.dev_test_labs.policies
WHERE labName = '{{ labName }}'
AND policySetName = '{{ policySetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO azure.dev_test_labs.policies (
labName,
name,
policySetName,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
'{{ name }}',
'{{ policySetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
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
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: description
          value: string
        - name: status
          value: string
        - name: factName
          value: string
        - name: factData
          value: string
        - name: threshold
          value: string
        - name: evaluatorType
          value: string
        - name: createdDate
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>policies</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.policies
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND policySetName = '{{ policySetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.policies
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND policySetName = '{{ policySetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
