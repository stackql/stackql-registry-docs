---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
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

Creates, updates, deletes, gets or lists a <code>exports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.exports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_exports', value: 'view', },
        { label: 'exports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="exportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `text` | The location of the Export's managed identity. Only required when utilizing managed identity. |
| <CopyableCode code="next_run_time_estimate" /> | `text` | field from the `properties` object |
| <CopyableCode code="partition_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_history" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The location of the Export's managed identity. Only required when utilizing managed identity. |
| <CopyableCode code="properties" /> | `object` | The properties of the export. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="exportName, scope" /> | The operation to get the export for the defined scope by export name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | The operation to list all exports at the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="exportName, scope" /> | The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="exportName, scope" /> | The operation to delete a export. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="exportName, scope" /> | The operation to run an export. |

## `SELECT` examples

The operation to list all exports at the given scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_exports', value: 'view', },
        { label: 'exports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
definition,
delivery_info,
e_tag,
exportName,
format,
identity,
location,
next_run_time_estimate,
partition_data,
run_history,
schedule,
scope,
type
FROM azure.cost_management.vw_exports
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
identity,
location,
properties,
type
FROM azure.cost_management.exports
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>exports</code> resource.

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
INSERT INTO azure.cost_management.exports (
exportName,
scope,
eTag,
identity,
location,
properties
)
SELECT 
'{{ exportName }}',
'{{ scope }}',
'{{ eTag }}',
'{{ identity }}',
'{{ location }}',
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
    - name: eTag
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
    - name: location
      value: string
    - name: properties
      value:
        - name: format
          value: string
        - name: deliveryInfo
          value:
            - name: destination
              value:
                - name: resourceId
                  value: string
                - name: container
                  value: string
                - name: rootFolderPath
                  value: string
                - name: sasToken
                  value: string
                - name: storageAccount
                  value: string
        - name: definition
          value:
            - name: type
              value: string
            - name: timeframe
              value: string
            - name: timePeriod
              value:
                - name: from
                  value: string
                - name: to
                  value: string
            - name: dataSet
              value:
                - name: granularity
                  value: string
                - name: configuration
                  value:
                    - name: columns
                      value:
                        - string
        - name: runHistory
          value:
            - name: value
              value:
                - - name: id
                    value: string
                  - name: name
                    value: string
                  - name: type
                    value: string
                  - name: eTag
                    value: string
                  - name: properties
                    value:
                      - name: executionType
                        value: string
                      - name: status
                        value: string
                      - name: submittedBy
                        value: string
                      - name: submittedTime
                        value: string
                      - name: processingStartTime
                        value: string
                      - name: processingEndTime
                        value: string
                      - name: fileName
                        value: string
                      - name: runSettings
                        value:
                          - name: format
                            value: string
                          - name: partitionData
                            value: boolean
                          - name: nextRunTimeEstimate
                            value: string
                      - name: error
                        value:
                          - name: code
                            value: string
                          - name: message
                            value: string
        - name: partitionData
          value: boolean
        - name: nextRunTimeEstimate
          value: string
        - name: schedule
          value:
            - name: status
              value: string
            - name: recurrence
              value: string
            - name: recurrencePeriod
              value:
                - name: from
                  value: string
                - name: to
                  value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>exports</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cost_management.exports
WHERE exportName = '{{ exportName }}'
AND scope = '{{ scope }}';
```
