---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.functions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_functions', value: 'view', },
        { label: 'functions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="functionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | The properties that are associated with a function. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a function. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="functionName, jobName, resourceGroupName, subscriptionId" /> | Gets details about the specified function. |
| <CopyableCode code="list_by_streaming_job" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Lists all of the functions under the specified streaming job. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="functionName, jobName, resourceGroupName, subscriptionId" /> | Creates a function or replaces an already existing function under an existing streaming job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="functionName, jobName, resourceGroupName, subscriptionId" /> | Deletes a function from the streaming job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="functionName, jobName, resourceGroupName, subscriptionId" /> | Updates an existing function under an existing streaming job. This can be used to partially update (ie. update one or two properties) a function without affecting the rest the job or function definition. |
| <CopyableCode code="retrieve_default_definition" /> | `EXEC` | <CopyableCode code="functionName, jobName, resourceGroupName, subscriptionId, data__bindingType" /> | Retrieves the default definition of a function based on the parameters specified. |
| <CopyableCode code="test" /> | `EXEC` | <CopyableCode code="functionName, jobName, resourceGroupName, subscriptionId" /> | Tests if the information provided for a function is valid. This can range from testing the connection to the underlying web service behind the function or making sure the function code provided is syntactically correct. |

## `SELECT` examples

Lists all of the functions under the specified streaming job.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_functions', value: 'view', },
        { label: 'functions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
functionName,
jobName,
properties,
resourceGroupName,
subscriptionId,
type
FROM azure.stream_analytics.vw_functions
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.stream_analytics.functions
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>functions</code> resource.

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
INSERT INTO azure.stream_analytics.functions (
functionName,
jobName,
resourceGroupName,
subscriptionId,
name,
properties
)
SELECT 
'{{ functionName }}',
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ name }}',
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
        - name: type
          value: string
        - name: etag
          value: string
        - name: properties
          value:
            - name: inputs
              value:
                - - name: dataType
                    value: string
                  - name: isConfigurationParameter
                    value: boolean
            - name: output
              value:
                - name: dataType
                  value: string
            - name: binding
              value:
                - name: type
                  value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>functions</code> resource.

```sql
/*+ update */
UPDATE azure.stream_analytics.functions
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
functionName = '{{ functionName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>functions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.stream_analytics.functions
WHERE functionName = '{{ functionName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
