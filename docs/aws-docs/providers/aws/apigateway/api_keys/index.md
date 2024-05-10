---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
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


Used to retrieve a list of <code>api_keys</code> in a region or to create or delete a <code>api_keys</code> resource, use <code>api_key</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.api_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_key_id" /></td><td><code>string</code></td><td></td></tr>
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
api_key_id
FROM aws.apigateway.api_keys
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
 "CustomerId": "{{ CustomerId }}",
 "Description": "{{ Description }}",
 "Enabled": "{{ Enabled }}",
 "GenerateDistinctId": "{{ GenerateDistinctId }}",
 "Name": "{{ Name }}",
 "StageKeys": [
  {
   "RestApiId": "{{ RestApiId }}",
   "StageName": "{{ StageName }}"
  }
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Value": "{{ Value }}"
}
>>>
--required properties only
INSERT INTO aws.apigateway.api_keys (
 CustomerId,
 Description,
 Enabled,
 GenerateDistinctId,
 Name,
 StageKeys,
 Tags,
 Value,
 region
)
SELECT 
{{ CustomerId }},
 {{ Description }},
 {{ Enabled }},
 {{ GenerateDistinctId }},
 {{ Name }},
 {{ StageKeys }},
 {{ Tags }},
 {{ Value }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CustomerId": "{{ CustomerId }}",
 "Description": "{{ Description }}",
 "Enabled": "{{ Enabled }}",
 "GenerateDistinctId": "{{ GenerateDistinctId }}",
 "Name": "{{ Name }}",
 "StageKeys": [
  {
   "RestApiId": "{{ RestApiId }}",
   "StageName": "{{ StageName }}"
  }
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Value": "{{ Value }}"
}
>>>
--all properties
INSERT INTO aws.apigateway.api_keys (
 CustomerId,
 Description,
 Enabled,
 GenerateDistinctId,
 Name,
 StageKeys,
 Tags,
 Value,
 region
)
SELECT 
 {{ CustomerId }},
 {{ Description }},
 {{ Enabled }},
 {{ GenerateDistinctId }},
 {{ Name }},
 {{ StageKeys }},
 {{ Tags }},
 {{ Value }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.api_keys
WHERE data__Identifier = '<APIKeyId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>api_keys</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET,
apigateway:PUT
```

### Delete
```json
apigateway:DELETE,
apigateway:GET
```

### List
```json
apigateway:GET
```

