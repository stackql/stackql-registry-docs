---
title: workspace_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_diagnostics
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

Creates, updates, deletes, gets or lists a <code>workspace_diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_diagnostics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_diagnostics', value: 'view', },
        { label: 'workspace_diagnostics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="always_log" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnosticId" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_correlation_protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_client_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="logger_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_name_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sampling" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="verbosity" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostic Entity Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the Diagnostic specified by its identifier. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all diagnostics in the specified workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates a new Diagnostic or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the specified Diagnostic. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the Diagnostic specified by its identifier. |

## `SELECT` examples

Lists all diagnostics in the specified workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_diagnostics', value: 'view', },
        { label: 'workspace_diagnostics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
always_log,
backend,
diagnosticId,
frontend,
http_correlation_protocol,
log_client_ip,
logger_id,
metrics,
operation_name_format,
resourceGroupName,
sampling,
serviceName,
subscriptionId,
verbosity,
workspaceId
FROM azure.api_management.vw_workspace_diagnostics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_diagnostics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_diagnostics</code> resource.

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
INSERT INTO azure.api_management.workspace_diagnostics (
diagnosticId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ diagnosticId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
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
        - name: alwaysLog
          value: string
        - name: loggerId
          value: string
        - name: sampling
          value:
            - name: samplingType
              value: string
            - name: percentage
              value: number
        - name: frontend
          value:
            - name: request
              value:
                - name: headers
                  value:
                    - string
                - name: body
                  value:
                    - name: bytes
                      value: integer
                - name: dataMasking
                  value:
                    - name: queryParams
                      value:
                        - - name: value
                            value: string
                          - name: mode
                            value: string
                    - name: headers
                      value:
                        - - name: value
                            value: string
                          - name: mode
                            value: string
        - name: logClientIp
          value: boolean
        - name: httpCorrelationProtocol
          value: string
        - name: verbosity
          value: string
        - name: operationNameFormat
          value: string
        - name: metrics
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_diagnostics</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_diagnostics
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND diagnosticId = '{{ diagnosticId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_diagnostics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_diagnostics
WHERE If-Match = '{{ If-Match }}'
AND diagnosticId = '{{ diagnosticId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
