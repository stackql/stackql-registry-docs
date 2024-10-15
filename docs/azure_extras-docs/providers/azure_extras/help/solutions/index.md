---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
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

Creates, updates, deletes, gets or lists a <code>solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.solutions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions', value: 'view', },
        { label: 'solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replacement_maps" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="sections" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger_criteria" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Solution result |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, solutionResourceName" /> | Get the solution using the applicable solutionResourceName while creating the solution. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="scope, solutionResourceName" /> | Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId and requiredInputs’ from discovery solutions. <br/> Azure solutions comprise a comprehensive library of self-help resources that have been thoughtfully curated by Azure engineers to aid customers in resolving typical troubleshooting issues. These solutions encompass: <br/> (1.) Dynamic and context-aware diagnostics, guided troubleshooting wizards, and data visualizations. <br/> (2.) Rich instructional video tutorials and illustrative diagrams and images. <br/> (3.) Thoughtfully assembled textual troubleshooting instructions. <br/> All these components are seamlessly converged into unified solutions tailored to address a specific support problem area. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="scope, solutionResourceName" /> | Update the requiredInputs or additional information needed to execute the solution  |
| <CopyableCode code="warm_up" /> | `EXEC` | <CopyableCode code="scope, solutionResourceName" /> | Warm up the solution resource by preloading asynchronous diagnostics results into cache |

## `SELECT` examples

Get the solution using the applicable solutionResourceName while creating the solution.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions', value: 'view', },
        { label: 'solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
content,
parameters,
provisioning_state,
replacement_maps,
scope,
sections,
solutionResourceName,
solution_id,
title,
trigger_criteria
FROM azure_extras.help.vw_solutions
WHERE scope = '{{ scope }}'
AND solutionResourceName = '{{ solutionResourceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.help.solutions
WHERE scope = '{{ scope }}'
AND solutionResourceName = '{{ solutionResourceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>solutions</code> resource.

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
INSERT INTO azure_extras.help.solutions (
scope,
solutionResourceName,
properties
)
SELECT 
'{{ scope }}',
'{{ solutionResourceName }}',
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
        - name: triggerCriteria
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: parameters
          value: object
        - name: solutionId
          value: string
        - name: provisioningState
          value: string
        - name: title
          value: string
        - name: content
          value: string
        - name: replacementMaps
          value:
            - name: webResults
              value:
                - - name: replacementKey
                    value: string
                  - name: searchResults
                    value:
                      - - name: solutionId
                          value: string
                        - name: content
                          value: string
                        - name: title
                          value: string
                        - name: confidence
                          value: string
                        - name: source
                          value: string
                        - name: resultType
                          value: string
                        - name: rank
                          value: integer
                        - name: link
                          value: string
            - name: diagnostics
              value:
                - - name: solutionId
                    value: string
                  - name: status
                    value: []
                  - name: statusDetails
                    value: string
                  - name: replacementKey
                    value: string
                  - name: estimatedCompletionTime
                    value: string
                  - name: requiredParameters
                    value:
                      - string
                  - name: insights
                    value:
                      - - name: id
                          value: string
                        - name: title
                          value: string
                        - name: results
                          value: string
                        - name: importanceLevel
                          value: string
            - name: troubleshooters
              value:
                - - name: solutionId
                    value: string
                  - name: title
                    value: string
                  - name: summary
                    value: string
            - name: metricsBasedCharts
              value:
                - - name: name
                    value: string
                  - name: aggregationType
                    value: string
                  - name: timeSpanDuration
                    value: string
                  - name: title
                    value: string
                  - name: filterGroup
                    value:
                      - name: filter
                        value:
                          - - name: name
                              value: string
                            - name: values
                              value: string
                            - name: operator
                              value: string
                  - name: replacementKey
                    value: string
            - name: videos
              value:
                - - name: src
                    value: string
                  - name: title
                    value: string
                  - name: replacementKey
                    value: string
            - name: videoGroups
              value:
                - - name: videos
                    value:
                      - - name: src
                          value: string
                        - name: title
                          value: string
                  - name: replacementKey
                    value: string
        - name: sections
          value:
            - - name: title
                value: string
              - name: content
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>solutions</code> resource.

```sql
/*+ update */
UPDATE azure_extras.help.solutions
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}'
AND solutionResourceName = '{{ solutionResourceName }}';
```
