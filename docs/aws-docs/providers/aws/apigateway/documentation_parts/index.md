---
title: documentation_parts
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_parts
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>documentation_parts</code> in a region or to create or delete a <code>documentation_parts</code> resource, use <code>documentation_part</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_parts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::DocumentationPart`` resource creates a documentation part for an API. For more information, see &#91;Representation of API Documentation in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-documenting-api-content-representation.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.documentation_parts" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="documentation_part_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
documentation_part_id,
rest_api_id
FROM aws.apigateway.documentation_parts
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>documentation_part</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- documentation_part.iql (required properties only)
INSERT INTO aws.apigateway.documentation_parts (
 Location,
 Properties,
 RestApiId,
 region
)
SELECT 
'{{ Location }}',
 '{{ Properties }}',
 '{{ RestApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- documentation_part.iql (all properties)
INSERT INTO aws.apigateway.documentation_parts (
 Location,
 Properties,
 RestApiId,
 region
)
SELECT 
 '{{ Location }}',
 '{{ Properties }}',
 '{{ RestApiId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: documentation_part
    props:
      - name: Location
        value:
          Method: '{{ Method }}'
          Name: '{{ Name }}'
          Path: '{{ Path }}'
          StatusCode: '{{ StatusCode }}'
          Type: '{{ Type }}'
      - name: Properties
        value: '{{ Properties }}'
      - name: RestApiId
        value: '{{ RestApiId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.documentation_parts
WHERE data__Identifier = '<DocumentationPartId|RestApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>documentation_parts</code> resource, the following permissions are required:

### Create
```json
apigateway:GET,
apigateway:POST
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```

