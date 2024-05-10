---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - events
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


Used to retrieve a list of <code>connections</code> in a region or to create or delete a <code>connections</code> resource, use <code>connection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Connection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the connection.</td></tr>
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
name
FROM aws.events.connections
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
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "AuthorizationType": "{{ AuthorizationType }}",
 "AuthParameters": {
  "ApiKeyAuthParameters": {
   "ApiKeyName": "{{ ApiKeyName }}",
   "ApiKeyValue": "{{ ApiKeyValue }}"
  },
  "BasicAuthParameters": {
   "Username": "{{ Username }}",
   "Password": "{{ Password }}"
  },
  "OAuthParameters": {
   "ClientParameters": {
    "ClientID": "{{ ClientID }}",
    "ClientSecret": "{{ ClientSecret }}"
   },
   "AuthorizationEndpoint": "{{ AuthorizationEndpoint }}",
   "HttpMethod": "{{ HttpMethod }}",
   "OAuthHttpParameters": {
    "HeaderParameters": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}",
      "IsValueSecret": "{{ IsValueSecret }}"
     }
    ],
    "QueryStringParameters": [
     null
    ],
    "BodyParameters": [
     null
    ]
   }
  },
  "InvocationHttpParameters": null
 }
}
>>>
--required properties only
INSERT INTO aws.events.connections (
 Name,
 Description,
 AuthorizationType,
 AuthParameters,
 region
)
SELECT 
{{ Name }},
 {{ Description }},
 {{ AuthorizationType }},
 {{ AuthParameters }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "AuthorizationType": "{{ AuthorizationType }}",
 "AuthParameters": {
  "ApiKeyAuthParameters": {
   "ApiKeyName": "{{ ApiKeyName }}",
   "ApiKeyValue": "{{ ApiKeyValue }}"
  },
  "BasicAuthParameters": {
   "Username": "{{ Username }}",
   "Password": "{{ Password }}"
  },
  "OAuthParameters": {
   "ClientParameters": {
    "ClientID": "{{ ClientID }}",
    "ClientSecret": "{{ ClientSecret }}"
   },
   "AuthorizationEndpoint": "{{ AuthorizationEndpoint }}",
   "HttpMethod": "{{ HttpMethod }}",
   "OAuthHttpParameters": {
    "HeaderParameters": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}",
      "IsValueSecret": "{{ IsValueSecret }}"
     }
    ],
    "QueryStringParameters": [
     null
    ],
    "BodyParameters": [
     null
    ]
   }
  },
  "InvocationHttpParameters": null
 }
}
>>>
--all properties
INSERT INTO aws.events.connections (
 Name,
 Description,
 AuthorizationType,
 AuthParameters,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ AuthorizationType }},
 {{ AuthParameters }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.events.connections
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connections</code> resource, the following permissions are required:

### Create
```json
events:CreateConnection,
events:DescribeConnection,
secretsmanager:CreateSecret,
secretsmanager:GetSecretValue,
secretsmanager:PutSecretValue,
iam:CreateServiceLinkedRole
```

### Delete
```json
events:DeleteConnection,
events:DescribeConnection
```

### List
```json
events:ListConnections
```

