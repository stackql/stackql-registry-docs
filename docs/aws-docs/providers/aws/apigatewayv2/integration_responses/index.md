---
title: integration_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_responses
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


Used to retrieve a list of <code>integration_responses</code> in a region or to create or delete a <code>integration_responses</code> resource, use <code>integration_response</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::IntegrationResponse`` resource updates an integration response for an WebSocket API. For more information, see &#91;Set up WebSocket API Integration Responses in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-integration-responses.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.integration_responses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><CopyableCode code="integration_id" /></td><td><code>string</code></td><td>The integration ID.</td></tr>
<tr><td><CopyableCode code="integration_response_id" /></td><td><code>string</code></td><td></td></tr>
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
integration_id,
integration_response_id
FROM aws.apigatewayv2.integration_responses
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
 "IntegrationId": "{{ IntegrationId }}",
 "IntegrationResponseKey": "{{ IntegrationResponseKey }}",
 "ApiId": "{{ ApiId }}"
}
>>>
--required properties only
INSERT INTO aws.apigatewayv2.integration_responses (
 IntegrationId,
 IntegrationResponseKey,
 ApiId,
 region
)
SELECT 
{{ IntegrationId }},
 {{ IntegrationResponseKey }},
 {{ ApiId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResponseTemplates": {},
 "TemplateSelectionExpression": "{{ TemplateSelectionExpression }}",
 "ResponseParameters": {},
 "ContentHandlingStrategy": "{{ ContentHandlingStrategy }}",
 "IntegrationId": "{{ IntegrationId }}",
 "IntegrationResponseKey": "{{ IntegrationResponseKey }}",
 "ApiId": "{{ ApiId }}"
}
>>>
--all properties
INSERT INTO aws.apigatewayv2.integration_responses (
 ResponseTemplates,
 TemplateSelectionExpression,
 ResponseParameters,
 ContentHandlingStrategy,
 IntegrationId,
 IntegrationResponseKey,
 ApiId,
 region
)
SELECT 
 {{ ResponseTemplates }},
 {{ TemplateSelectionExpression }},
 {{ ResponseParameters }},
 {{ ContentHandlingStrategy }},
 {{ IntegrationId }},
 {{ IntegrationResponseKey }},
 {{ ApiId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigatewayv2.integration_responses
WHERE data__Identifier = '<ApiId|IntegrationId|IntegrationResponseId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integration_responses</code> resource, the following permissions are required:

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

