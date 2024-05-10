---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - apigatewayv2
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


Used to retrieve a list of <code>routes</code> in a region or to create or delete a <code>routes</code> resource, use <code>route</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::Route`` resource creates a route for an API.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><CopyableCode code="route_id" /></td><td><code>string</code></td><td></td></tr>
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
api_id,
route_id
FROM aws.apigatewayv2.routes
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "RouteKey": "{{ RouteKey }}",
 "ApiId": "{{ ApiId }}"
}
>>>
--required properties only
INSERT INTO aws.apigatewayv2.routes (
 RouteKey,
 ApiId,
 region
)
SELECT 
{{ RouteKey }},
 {{ ApiId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "RouteResponseSelectionExpression": "{{ RouteResponseSelectionExpression }}",
 "RequestModels": {},
 "OperationName": "{{ OperationName }}",
 "AuthorizationScopes": [
  "{{ AuthorizationScopes[0] }}"
 ],
 "ApiKeyRequired": "{{ ApiKeyRequired }}",
 "RouteKey": "{{ RouteKey }}",
 "AuthorizationType": "{{ AuthorizationType }}",
 "ModelSelectionExpression": "{{ ModelSelectionExpression }}",
 "ApiId": "{{ ApiId }}",
 "RequestParameters": {},
 "Target": "{{ Target }}",
 "AuthorizerId": "{{ AuthorizerId }}"
}
>>>
--all properties
INSERT INTO aws.apigatewayv2.routes (
 RouteResponseSelectionExpression,
 RequestModels,
 OperationName,
 AuthorizationScopes,
 ApiKeyRequired,
 RouteKey,
 AuthorizationType,
 ModelSelectionExpression,
 ApiId,
 RequestParameters,
 Target,
 AuthorizerId,
 region
)
SELECT 
 {{ RouteResponseSelectionExpression }},
 {{ RequestModels }},
 {{ OperationName }},
 {{ AuthorizationScopes }},
 {{ ApiKeyRequired }},
 {{ RouteKey }},
 {{ AuthorizationType }},
 {{ ModelSelectionExpression }},
 {{ ApiId }},
 {{ RequestParameters }},
 {{ Target }},
 {{ AuthorizerId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigatewayv2.routes
WHERE data__Identifier = '<ApiId|RouteId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>routes</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

### List
```json
apigateway:GET
```

