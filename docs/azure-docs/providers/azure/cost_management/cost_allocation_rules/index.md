---
title: cost_allocation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_allocation_rules
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>cost_allocation_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cost_allocation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.cost_allocation_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cost_allocation_rules', value: 'view', },
        { label: 'cost_allocation_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure Resource Manager Id for the rule. This is a read ony value. |
| <CopyableCode code="name" /> | `text` | Name of the rule. This is a read only value. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountId" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type of the rule. This is a read only value of Microsoft.CostManagement/CostAllocationRule. |
| <CopyableCode code="updated_date" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure Resource Manager Id for the rule. This is a read ony value. |
| <CopyableCode code="name" /> | `string` | Name of the rule. This is a read only value. |
| <CopyableCode code="properties" /> | `object` | The properties of a cost allocation rule |
| <CopyableCode code="type" /> | `string` | Resource type of the rule. This is a read only value of Microsoft.CostManagement/CostAllocationRule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountId, ruleName" /> | Get a cost allocation rule by rule name and billing account or enterprise enrollment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountId" /> | Get the list of all cost allocation rules for a billing account or enterprise enrollment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountId, ruleName" /> | Create/Update a rule to allocate cost between different resources within a billing account or enterprise enrollment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountId, ruleName" /> | Delete cost allocation rule for billing account or enterprise enrollment. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="billingAccountId" /> | Checks availability and correctness of a name for a cost allocation rule |

## `SELECT` examples

Get the list of all cost allocation rules for a billing account or enterprise enrollment.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cost_allocation_rules', value: 'view', },
        { label: 'cost_allocation_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
billingAccountId,
created_date,
details,
ruleName,
status,
type,
updated_date
FROM azure.cost_management.vw_cost_allocation_rules
WHERE billingAccountId = '{{ billingAccountId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.cost_management.cost_allocation_rules
WHERE billingAccountId = '{{ billingAccountId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cost_allocation_rules</code> resource.

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
INSERT INTO azure.cost_management.cost_allocation_rules (
billingAccountId,
ruleName,
properties
)
SELECT 
'{{ billingAccountId }}',
'{{ ruleName }}',
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
    - name: properties
      value:
        - name: description
          value: string
        - name: details
          value:
            - name: sourceResources
              value:
                - - name: resourceType
                    value: []
                  - name: name
                    value: string
            - name: targetResources
              value:
                - - name: name
                    value: string
        - name: status
          value: []
        - name: createdDate
          value: string
        - name: updatedDate
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cost_allocation_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cost_management.cost_allocation_rules
WHERE billingAccountId = '{{ billingAccountId }}'
AND ruleName = '{{ ruleName }}';
```
