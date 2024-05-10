---
title: authorizers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizers
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


Used to retrieve a list of <code>authorizers</code> in a region or to create or delete a <code>authorizers</code> resource, use <code>authorizer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::Authorizer`` resource creates an authorization layer that API Gateway activates for methods that have authorization enabled. API Gateway activates the authorizer when a client calls those methods.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.authorizers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="authorizer_id" /></td><td><code>string</code></td><td></td></tr>
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
rest_api_id,
authorizer_id
FROM aws.apigateway.authorizers
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
 "RestApiId": "{{ RestApiId }}",
 "Name": "{{ Name }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.apigateway.authorizers (
 RestApiId,
 Name,
 Type,
 region
)
SELECT 
{{ .RestApiId }},
 {{ .Name }},
 {{ .Type }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "RestApiId": "{{ RestApiId }}",
 "AuthType": "{{ AuthType }}",
 "AuthorizerCredentials": "{{ AuthorizerCredentials }}",
 "AuthorizerResultTtlInSeconds": "{{ AuthorizerResultTtlInSeconds }}",
 "AuthorizerUri": "{{ AuthorizerUri }}",
 "IdentitySource": "{{ IdentitySource }}",
 "IdentityValidationExpression": "{{ IdentityValidationExpression }}",
 "Name": "{{ Name }}",
 "ProviderARNs": [
  "{{ ProviderARNs[0] }}"
 ],
 "Type": "{{ Type }}"
}
>>>
--all properties
INSERT INTO aws.apigateway.authorizers (
 RestApiId,
 AuthType,
 AuthorizerCredentials,
 AuthorizerResultTtlInSeconds,
 AuthorizerUri,
 IdentitySource,
 IdentityValidationExpression,
 Name,
 ProviderARNs,
 Type,
 region
)
SELECT 
 {{ .RestApiId }},
 {{ .AuthType }},
 {{ .AuthorizerCredentials }},
 {{ .AuthorizerResultTtlInSeconds }},
 {{ .AuthorizerUri }},
 {{ .IdentitySource }},
 {{ .IdentityValidationExpression }},
 {{ .Name }},
 {{ .ProviderARNs }},
 {{ .Type }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.authorizers
WHERE data__Identifier = '<RestApiId|AuthorizerId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>authorizers</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
iam:PassRole
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```

