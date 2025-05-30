---
title: loggers
hide_title: false
hide_table_of_contents: false
keywords:
  - loggers
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

Creates, updates, deletes, gets or lists a <code>loggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>loggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.loggers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_loggers', value: 'view', },
        { label: 'loggers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_buffered" /> | `text` | field from the `properties` object |
| <CopyableCode code="loggerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="logger_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Logger entity in API Management represents an event sink that you can use to log API Management events. Currently the Logger entity supports logging API Management events to Azure Event Hubs. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loggerId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the logger specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of loggers in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loggerId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a logger. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, loggerId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified logger. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, loggerId, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing logger. |

## `SELECT` examples

Lists a collection of loggers in the specified service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_loggers', value: 'view', },
        { label: 'loggers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
credentials,
is_buffered,
loggerId,
logger_type,
resourceGroupName,
resource_id,
serviceName,
subscriptionId
FROM azure.api_management.vw_loggers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.loggers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>loggers</code> resource.

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
INSERT INTO azure.api_management.loggers (
loggerId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ loggerId }}',
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
        - name: loggerType
          value: string
        - name: description
          value: string
        - name: credentials
          value: object
        - name: isBuffered
          value: boolean
        - name: resourceId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>loggers</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.loggers
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND loggerId = '{{ loggerId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>loggers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.loggers
WHERE If-Match = '{{ If-Match }}'
AND loggerId = '{{ loggerId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
