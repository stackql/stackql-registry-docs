---
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
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

Creates, updates, deletes, gets or lists a <code>diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.diagnostics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostics', value: 'view', },
        { label: 'diagnostics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accepted_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnosticsResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="global_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="insights" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostic resource properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticsResourceName, scope" /> | Get the diagnostics using the 'diagnosticsResourceName' you chose while creating the diagnostic. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="diagnosticsResourceName, scope" /> | Creates a diagnostic for the specific resource using solutionId from discovery solutions. <br/>Diagnostics are powerful solutions that access product resources or other relevant data and provide the root cause of the issue and the steps to address the issue.<br/><br/> |

## `SELECT` examples

Get the diagnostics using the 'diagnosticsResourceName' you chose while creating the diagnostic.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostics', value: 'view', },
        { label: 'diagnostics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accepted_at,
diagnostics,
diagnosticsResourceName,
global_parameters,
insights,
provisioning_state,
scope
FROM azure_extras.help.vw_diagnostics
WHERE diagnosticsResourceName = '{{ diagnosticsResourceName }}'
AND scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.help.diagnostics
WHERE diagnosticsResourceName = '{{ diagnosticsResourceName }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>diagnostics</code> resource.

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
INSERT INTO azure_extras.help.diagnostics (
diagnosticsResourceName,
scope,
properties
)
SELECT 
'{{ diagnosticsResourceName }}',
'{{ scope }}',
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
        - name: globalParameters
          value: object
        - name: insights
          value:
            - - name: solutionId
                value: string
              - name: additionalParameters
                value: object
        - name: acceptedAt
          value: string
        - name: provisioningState
          value: string
        - name: diagnostics
          value:
            - - name: solutionId
                value: string
              - name: status
                value: []
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
                  - name: type
                    value: string
                  - name: message
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: type
                          value: string
                        - name: message
                          value: string
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: type
                                value: string
                              - name: message
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: type
                                      value: string
                                    - name: message
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: type
                                            value: string
                                          - name: message
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: type
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: code
                                                              value: string
                                                            - name: type
                                                              value: string
                                                            - name: message
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []

```
</TabItem>
</Tabs>
