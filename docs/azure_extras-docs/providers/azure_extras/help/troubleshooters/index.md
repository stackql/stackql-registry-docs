---
title: troubleshooters
hide_title: false
hide_table_of_contents: false
keywords:
  - troubleshooters
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

Creates, updates, deletes, gets or lists a <code>troubleshooters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>troubleshooters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.troubleshooters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_troubleshooters', value: 'view', },
        { label: 'troubleshooters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="troubleshooterName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Troubleshooter Instance properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, troubleshooterName" /> | Gets troubleshooter instance result which includes the step status/result of the troubleshooter resource name that is being executed.<br/> Get API is used to retrieve the result of a Troubleshooter instance, which includes the status and result of each step in the Troubleshooter workflow. This API requires the Troubleshooter resource name that was created using the Create API. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="scope, troubleshooterName" /> | Creates the specific troubleshooter action under a resource or subscription using the ‘solutionId’ and  ‘properties.parameters’ as the trigger. <br/> Azure Troubleshooters help with hard to classify issues, reducing the gap between customer observed problems and solutions by guiding the user effortlessly through the troubleshooting process. Each Troubleshooter flow represents a problem area within Azure and has a complex tree-like structure that addresses many root causes. These flows are prepared with the help of Subject Matter experts and customer support engineers by carefully considering previous support requests raised by customers. Troubleshooters terminate at a well curated solution based off of resource backend signals and customer manual selections. |
| <CopyableCode code="continue" /> | `EXEC` | <CopyableCode code="scope, troubleshooterName" /> | Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the respective troubleshooter resource name. <br/>Continue API is used to provide inputs that are required for the specific troubleshooter to progress into the next step in the process. This API is used after the Troubleshooter has been created using the Create API. |
| <CopyableCode code="end" /> | `EXEC` | <CopyableCode code="scope, troubleshooterName" /> | Ends the troubleshooter action |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="scope, troubleshooterName" /> | Restarts the troubleshooter API using applicable troubleshooter resource name as the input.<br/> It returns new resource name which should be used in subsequent request. The old resource name is obsolete after this API is invoked. |

## `SELECT` examples

Gets troubleshooter instance result which includes the step status/result of the troubleshooter resource name that is being executed.<br/> Get API is used to retrieve the result of a Troubleshooter instance, which includes the status and result of each step in the Troubleshooter workflow. This API requires the Troubleshooter resource name that was created using the Create API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_troubleshooters', value: 'view', },
        { label: 'troubleshooters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
parameters,
provisioning_state,
scope,
solution_id,
steps,
troubleshooterName
FROM azure_extras.help.vw_troubleshooters
WHERE scope = '{{ scope }}'
AND troubleshooterName = '{{ troubleshooterName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.help.troubleshooters
WHERE scope = '{{ scope }}'
AND troubleshooterName = '{{ troubleshooterName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>troubleshooters</code> resource.

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
INSERT INTO azure_extras.help.troubleshooters (
scope,
troubleshooterName,
properties
)
SELECT 
'{{ scope }}',
'{{ troubleshooterName }}',
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
        - name: provisioningState
          value: string
        - name: steps
          value:
            - - name: id
                value: string
              - name: title
                value: string
              - name: description
                value: string
              - name: guidance
                value: string
              - name: executionStatus
                value: string
              - name: executionStatusDescription
                value: string
              - name: type
                value: string
              - name: isLastStep
                value: boolean
              - name: inputs
                value:
                  - - name: questionId
                      value: string
                    - name: questionType
                      value: []
                    - name: questionTitle
                      value: string
                    - name: questionContent
                      value: string
                    - name: questionContentType
                      value: string
                    - name: responseHint
                      value: string
                    - name: recommendedOption
                      value: string
                    - name: selectedOptionValue
                      value: string
                    - name: responseValidationProperties
                      value:
                        - name: regex
                          value: string
                        - name: validationScope
                          value: string
                        - name: isRequired
                          value: boolean
                        - name: validationErrorMessage
                          value: string
                        - name: maxLength
                          value: integer
                    - name: responseOptions
                      value:
                        - - name: key
                            value: string
                          - name: value
                            value: string
              - name: automatedCheckResults
                value:
                  - name: version
                    value: string
                  - name: status
                    value: string
                  - name: result
                    value: string
                  - name: type
                    value: string
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
              - name: error
                value:
                  - name: code
                    value: string
                  - name: message
                    value: string
                  - name: target
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: message
                          value: string
                        - name: target
                          value: string
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: message
                                value: string
                              - name: target
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: message
                                      value: string
                                    - name: target
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: message
                                            value: string
                                          - name: target
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: target
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: target
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                            - name: target
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: additionalInfo
                                                              value:
                                                                - []
                                                      - name: additionalInfo
                                                        value:
                                                          - - name: type
                                                              value: string
                                                            - name: info
                                                              value: object
                                                - name: additionalInfo
                                                  value:
                                                    - - name: type
                                                        value: string
                                                      - name: info
                                                        value: object
                                          - name: additionalInfo
                                            value:
                                              - - name: type
                                                  value: string
                                                - name: info
                                                  value: object
                                    - name: additionalInfo
                                      value:
                                        - - name: type
                                            value: string
                                          - name: info
                                            value: object
                              - name: additionalInfo
                                value:
                                  - - name: type
                                      value: string
                                    - name: info
                                      value: object
                        - name: additionalInfo
                          value:
                            - - name: type
                                value: string
                              - name: info
                                value: object
                  - name: additionalInfo
                    value:
                      - - name: type
                          value: string
                        - name: info
                          value: object

```
</TabItem>
</Tabs>
