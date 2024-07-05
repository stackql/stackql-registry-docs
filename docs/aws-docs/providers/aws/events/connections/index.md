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

Creates, updates, deletes or gets a <code>connection</code> resource or lists <code>connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Connection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the connection.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The arn of the connection resource.</td></tr>
<tr><td><CopyableCode code="secret_arn" /></td><td><code>string</code></td><td>The arn of the secrets manager secret created in the customer account.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the connection.</td></tr>
<tr><td><CopyableCode code="authorization_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_parameters" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>connections</code> in a region.
```sql
SELECT
region,
name,
arn,
secret_arn,
description,
authorization_type,
auth_parameters
FROM aws.events.connections
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>connection</code>.
```sql
SELECT
region,
name,
arn,
secret_arn,
description,
authorization_type,
auth_parameters
FROM aws.events.connections
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.events.connections (
 Name,
 Description,
 AuthorizationType,
 AuthParameters,
 region
)
SELECT 
'{{ Name }}',
 '{{ Description }}',
 '{{ AuthorizationType }}',
 '{{ AuthParameters }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.events.connections (
 Name,
 Description,
 AuthorizationType,
 AuthParameters,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ AuthorizationType }}',
 '{{ AuthParameters }}',
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
  - name: connection
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: AuthorizationType
        value: '{{ AuthorizationType }}'
      - name: AuthParameters
        value:
          ApiKeyAuthParameters:
            ApiKeyName: '{{ ApiKeyName }}'
            ApiKeyValue: '{{ ApiKeyValue }}'
          BasicAuthParameters:
            Username: '{{ Username }}'
            Password: '{{ Password }}'
          OAuthParameters:
            ClientParameters:
              ClientID: '{{ ClientID }}'
              ClientSecret: '{{ ClientSecret }}'
            AuthorizationEndpoint: '{{ AuthorizationEndpoint }}'
            HttpMethod: '{{ HttpMethod }}'
            OAuthHttpParameters:
              HeaderParameters:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
                  IsValueSecret: '{{ IsValueSecret }}'
              QueryStringParameters:
                - null
              BodyParameters:
                - null
          InvocationHttpParameters: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
events:DescribeConnection
```

### Update
```json
events:UpdateConnection,
events:DescribeConnection,
secretsmanager:CreateSecret,
secretsmanager:UpdateSecret,
secretsmanager:GetSecretValue,
secretsmanager:PutSecretValue
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

