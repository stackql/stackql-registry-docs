---
title: api_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operations
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

Creates, updates, deletes, gets or lists a <code>api_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_operations', value: 'view', },
        { label: 'api_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="method" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="request" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="responses" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="template_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="url_template" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Operation Contract Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the API Operation specified by its identifier. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of the operations for the specified API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new operation in the API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified operation in the API. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the operation in the API specified by its identifier. |

## `SELECT` examples

Lists a collection of the operations for the specified API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_operations', value: 'view', },
        { label: 'api_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiId,
display_name,
method,
operationId,
policies,
request,
resourceGroupName,
responses,
serviceName,
subscriptionId,
template_parameters,
url_template
FROM azure.api_management.vw_api_operations
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
FROM azure.api_management.api_operations
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_operations</code> resource.

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
INSERT INTO azure.api_management.api_operations (
apiId,
operationId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ operationId }}',
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
        - name: displayName
          value: string
        - name: method
          value: string
        - name: urlTemplate
          value: string
        - name: templateParameters
          value:
            - - name: name
                value: string
              - name: description
                value: string
              - name: type
                value: string
              - name: defaultValue
                value: string
              - name: required
                value: boolean
              - name: values
                value:
                  - string
              - name: schemaId
                value: string
              - name: typeName
                value: string
              - name: examples
                value: []
        - name: description
          value: string
        - name: request
          value:
            - name: description
              value: string
            - name: queryParameters
              value:
                - - name: name
                    value: string
                  - name: description
                    value: string
                  - name: type
                    value: string
                  - name: defaultValue
                    value: string
                  - name: required
                    value: boolean
                  - name: values
                    value:
                      - string
                  - name: schemaId
                    value: string
                  - name: typeName
                    value: string
            - name: headers
              value:
                - - name: name
                    value: string
                  - name: description
                    value: string
                  - name: type
                    value: string
                  - name: defaultValue
                    value: string
                  - name: required
                    value: boolean
                  - name: values
                    value:
                      - string
                  - name: schemaId
                    value: string
                  - name: typeName
                    value: string
            - name: representations
              value:
                - - name: contentType
                    value: string
                  - name: schemaId
                    value: string
                  - name: typeName
                    value: string
                  - name: formParameters
                    value:
                      - - name: name
                          value: string
                        - name: description
                          value: string
                        - name: type
                          value: string
                        - name: defaultValue
                          value: string
                        - name: required
                          value: boolean
                        - name: values
                          value:
                            - string
                        - name: schemaId
                          value: string
                        - name: typeName
                          value: string
        - name: responses
          value:
            - - name: statusCode
                value: integer
              - name: description
                value: string
              - name: representations
                value:
                  - - name: contentType
                      value: string
                    - name: schemaId
                      value: string
                    - name: typeName
                      value: string
                    - name: formParameters
                      value:
                        - - name: name
                            value: string
                          - name: description
                            value: string
                          - name: type
                            value: string
                          - name: defaultValue
                            value: string
                          - name: required
                            value: boolean
                          - name: values
                            value:
                              - string
                          - name: schemaId
                            value: string
                          - name: typeName
                            value: string
              - name: headers
                value:
                  - - name: name
                      value: string
                    - name: description
                      value: string
                    - name: type
                      value: string
                    - name: defaultValue
                      value: string
                    - name: required
                      value: boolean
                    - name: values
                      value:
                        - string
                    - name: schemaId
                      value: string
                    - name: typeName
                      value: string
        - name: policies
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>api_operations</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.api_operations
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>api_operations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_operations
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
