---
title: api_schemata
hide_title: false
hide_table_of_contents: false
keywords:
  - api_schemata
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

Creates, updates, deletes, gets or lists a <code>api_schemata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_schemata" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_schemata', value: 'view', },
        { label: 'api_schemata', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="document" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaId" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API Schema create or update contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, schemaId, serviceName, subscriptionId" /> | Get the schema configuration at the API level. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Get the schema configuration at the API level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resourceGroupName, schemaId, serviceName, subscriptionId" /> | Creates or updates schema configuration for the API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resourceGroupName, schemaId, serviceName, subscriptionId" /> | Deletes the schema configuration at the Api. |

## `SELECT` examples

Get the schema configuration at the API level.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_schemata', value: 'view', },
        { label: 'api_schemata', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiId,
content_type,
document,
provisioning_state,
resourceGroupName,
schemaId,
serviceName,
subscriptionId
FROM azure.api_management.vw_api_schemata
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
FROM azure.api_management.api_schemata
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_schemata</code> resource.

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
INSERT INTO azure.api_management.api_schemata (
apiId,
resourceGroupName,
schemaId,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ resourceGroupName }}',
'{{ schemaId }}',
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
        - name: contentType
          value: string
        - name: document
          value:
            - name: value
              value: string
            - name: definitions
              value: object
            - name: components
              value: object
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_schemata</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_schemata
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaId = '{{ schemaId }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
