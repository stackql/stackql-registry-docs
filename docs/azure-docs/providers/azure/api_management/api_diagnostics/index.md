---
title: api_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - api_diagnostics
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

Creates, updates, deletes, gets or lists a <code>api_diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_diagnostics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_diagnostics', value: 'view', },
        { label: 'api_diagnostics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="always_log" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
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
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostic Entity Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Diagnostic for an API specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all diagnostics of an API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Diagnostic for an API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Diagnostic from an API. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the Diagnostic for an API specified by its identifier. |

## `SELECT` examples

Lists all diagnostics of an API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_diagnostics', value: 'view', },
        { label: 'api_diagnostics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
always_log,
apiId,
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
verbosity
FROM azure.api_management.vw_api_diagnostics
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.api_diagnostics
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_diagnostics</code> resource.

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
INSERT INTO azure.api_management.api_diagnostics (
apiId,
diagnosticId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ diagnosticId }}',
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

Updates a <code>api_diagnostics</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.api_diagnostics
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND diagnosticId = '{{ diagnosticId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>api_diagnostics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_diagnostics
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND diagnosticId = '{{ diagnosticId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
