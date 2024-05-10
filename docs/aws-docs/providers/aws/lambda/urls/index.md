---
title: urls
hide_title: false
hide_table_of_contents: false
keywords:
  - urls
  - lambda
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


Used to retrieve a list of <code>urls</code> in a region or to create or delete a <code>urls</code> resource, use <code>url</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Url</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.urls" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The full Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
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
function_arn
FROM aws.lambda.urls
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>url</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- url.iql (required properties only)
INSERT INTO aws.lambda.urls (
 TargetFunctionArn,
 AuthType,
 region
)
SELECT 
'{{ TargetFunctionArn }}',
 '{{ AuthType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- url.iql (all properties)
INSERT INTO aws.lambda.urls (
 TargetFunctionArn,
 Qualifier,
 AuthType,
 InvokeMode,
 Cors,
 region
)
SELECT 
 '{{ TargetFunctionArn }}',
 '{{ Qualifier }}',
 '{{ AuthType }}',
 '{{ InvokeMode }}',
 '{{ Cors }}',
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
  - name: url
    props:
      - name: TargetFunctionArn
        value: '{{ TargetFunctionArn }}'
      - name: Qualifier
        value: '{{ Qualifier }}'
      - name: AuthType
        value: '{{ AuthType }}'
      - name: InvokeMode
        value: '{{ InvokeMode }}'
      - name: Cors
        value:
          AllowCredentials: '{{ AllowCredentials }}'
          AllowHeaders:
            - '{{ AllowHeaders[0] }}'
          AllowMethods:
            - '{{ AllowMethods[0] }}'
          AllowOrigins:
            - '{{ AllowOrigins[0] }}'
          ExposeHeaders:
            - '{{ ExposeHeaders[0] }}'
          MaxAge: '{{ MaxAge }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lambda.urls
WHERE data__Identifier = '<FunctionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>urls</code> resource, the following permissions are required:

### Create
```json
lambda:CreateFunctionUrlConfig
```

### List
```json
lambda:ListFunctionUrlConfigs
```

### Delete
```json
lambda:DeleteFunctionUrlConfig
```

