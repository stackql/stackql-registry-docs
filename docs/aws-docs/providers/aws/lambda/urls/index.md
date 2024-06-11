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

Creates, updates, deletes or gets an <code>url</code> resource or lists <code>urls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Url</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.urls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_function_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
<tr><td><CopyableCode code="qualifier" /></td><td><code>string</code></td><td>The alias qualifier for the target function. If TargetFunctionArn is unqualified then Qualifier must be passed.</td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td>Can be either AWS_IAM if the requests are authorized via IAM, or NONE if no authorization is configured on the Function URL.</td></tr>
<tr><td><CopyableCode code="invoke_mode" /></td><td><code>string</code></td><td>The invocation mode for the function's URL. Set to BUFFERED if you want to buffer responses before returning them to the client. Set to RESPONSE_STREAM if you want to stream responses, allowing faster time to first byte and larger response payload sizes. If not set, defaults to BUFFERED.</td></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The full Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
<tr><td><CopyableCode code="function_url" /></td><td><code>string</code></td><td>The generated url for this resource.</td></tr>
<tr><td><CopyableCode code="cors" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="TargetFunctionArn, AuthType, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>urls</code> in a region.
```sql
SELECT
region,
function_arn
FROM aws.lambda.urls
WHERE region = 'us-east-1';
```
Gets all properties from an <code>url</code>.
```sql
SELECT
region,
target_function_arn,
qualifier,
auth_type,
invoke_mode,
function_arn,
function_url,
cors
FROM aws.lambda.urls
WHERE region = 'us-east-1' AND data__Identifier = '<FunctionArn>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
lambda:GetFunctionUrlConfig
```

### Update
```json
lambda:UpdateFunctionUrlConfig
```

### List
```json
lambda:ListFunctionUrlConfigs
```

### Delete
```json
lambda:DeleteFunctionUrlConfig
```

