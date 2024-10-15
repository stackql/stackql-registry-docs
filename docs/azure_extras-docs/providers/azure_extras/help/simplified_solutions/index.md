---
title: simplified_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - simplified_solutions
  - help
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

Creates, updates, deletes, gets or lists a <code>simplified_solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simplified_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.simplified_solutions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_simplified_solutions', value: 'view', },
        { label: 'simplified_solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appendix" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="simplifiedSolutionsResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Simplified Solutions result |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, simplifiedSolutionsResourceName" /> | Get the simplified Solutions using the applicable solutionResourceName while creating the simplified Solutions. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="scope, simplifiedSolutionsResourceName" /> | Creates Simplified Solutions for an Azure subscription using 'solutionId' from Discovery Solutions as the input. <br/><br/> Simplified Solutions API makes the consumption of solutions APIs easier while still providing access to the same powerful solutions rendered in Solutions API. With Simplified Solutions, users don't have to worry about stitching together the article using replacement maps and can use the content in the API response to directly render as HTML content.<br/> |

## `SELECT` examples

Get the simplified Solutions using the applicable solutionResourceName while creating the simplified Solutions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_simplified_solutions', value: 'view', },
        { label: 'simplified_solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appendix,
content,
parameters,
provisioning_state,
scope,
simplifiedSolutionsResourceName,
solution_id,
title
FROM azure_extras.help.vw_simplified_solutions
WHERE scope = '{{ scope }}'
AND simplifiedSolutionsResourceName = '{{ simplifiedSolutionsResourceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.help.simplified_solutions
WHERE scope = '{{ scope }}'
AND simplifiedSolutionsResourceName = '{{ simplifiedSolutionsResourceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>simplified_solutions</code> resource.

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
INSERT INTO azure_extras.help.simplified_solutions (
scope,
simplifiedSolutionsResourceName,
properties
)
SELECT 
'{{ scope }}',
'{{ simplifiedSolutionsResourceName }}',
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
        - name: solutionId
          value: string
        - name: parameters
          value: object
        - name: title
          value: string
        - name: appendix
          value: object
        - name: content
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>
