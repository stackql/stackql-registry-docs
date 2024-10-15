---
title: standards
hide_title: false
hide_table_of_contents: false
keywords:
  - standards
  - security
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

Creates, updates, deletes, gets or lists a <code>standards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.standards" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standards', value: 'view', },
        { label: 'standards', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessments" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_set_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="standardId" /> | `text` | field from the `properties` object |
| <CopyableCode code="standard_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of a standard. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, standardId" /> | Get a specific security standard for the requested scope by standardId |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of all relevant security standards over a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="scope, standardId" /> | Creates or updates a security standard over a given scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="scope, standardId" /> | Delete a security standard over a given scope |

## `SELECT` examples

Get a list of all relevant security standards over a scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standards', value: 'view', },
        { label: 'standards', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assessments,
cloud_providers,
display_name,
metadata,
policy_set_definition_id,
scope,
standardId,
standard_type,
type
FROM azure.security.vw_standards
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.standards
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>standards</code> resource.

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
INSERT INTO azure.security.standards (
scope,
standardId,
properties
)
SELECT 
'{{ scope }}',
'{{ standardId }}',
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
        - name: standardType
          value: string
        - name: description
          value: string
        - name: assessments
          value:
            - - name: assessmentKey
                value: string
        - name: cloudProviders
          value:
            - []
        - name: policySetDefinitionId
          value: string
        - name: metadata
          value:
            - name: createdBy
              value: string
            - name: createdOn
              value: string
            - name: lastUpdatedBy
              value: string
            - name: lastUpdatedOn
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

## `DELETE` example

Deletes the specified <code>standards</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.standards
WHERE scope = '{{ scope }}'
AND standardId = '{{ standardId }}';
```
