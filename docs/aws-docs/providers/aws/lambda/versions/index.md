---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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

Creates, updates, deletes or gets a <code>version</code> resource or lists <code>versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Version</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The ARN of the version.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version number.</td></tr>
<tr><td><CopyableCode code="code_sha256" /></td><td><code>string</code></td><td>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. Updates are not supported for this property.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the version to override the description in the function configuration. Updates are not supported for this property.</td></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>The resource policy of your function</td></tr>
<tr><td><CopyableCode code="provisioned_concurrency_config" /></td><td><code>object</code></td><td>Specifies a provisioned concurrency configuration for a function's version. Updates are not supported for this property.</td></tr>
<tr><td><CopyableCode code="runtime_policy" /></td><td><code>object</code></td><td>Specifies the runtime management configuration of a function. Displays runtimeVersionArn only for Manual.</td></tr>
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
    <td><CopyableCode code="FunctionName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>versions</code> in a region.
```sql
SELECT
region,
function_arn,
version,
code_sha256,
description,
function_name,
policy,
provisioned_concurrency_config,
runtime_policy
FROM aws.lambda.versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>version</code>.
```sql
SELECT
region,
function_arn,
version,
code_sha256,
description,
function_name,
policy,
provisioned_concurrency_config,
runtime_policy
FROM aws.lambda.versions
WHERE region = 'us-east-1' AND data__Identifier = '<FunctionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lambda.versions (
 FunctionName,
 region
)
SELECT 
'{{ FunctionName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lambda.versions (
 CodeSha256,
 Description,
 FunctionName,
 Policy,
 ProvisionedConcurrencyConfig,
 RuntimePolicy,
 region
)
SELECT 
 '{{ CodeSha256 }}',
 '{{ Description }}',
 '{{ FunctionName }}',
 '{{ Policy }}',
 '{{ ProvisionedConcurrencyConfig }}',
 '{{ RuntimePolicy }}',
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
  - name: version
    props:
      - name: CodeSha256
        value: '{{ CodeSha256 }}'
      - name: Description
        value: '{{ Description }}'
      - name: FunctionName
        value: '{{ FunctionName }}'
      - name: Policy
        value: {}
      - name: ProvisionedConcurrencyConfig
        value:
          ProvisionedConcurrentExecutions: '{{ ProvisionedConcurrentExecutions }}'
      - name: RuntimePolicy
        value:
          RuntimeVersionArn: '{{ RuntimeVersionArn }}'
          UpdateRuntimeOn: '{{ UpdateRuntimeOn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lambda.versions
WHERE data__Identifier = '<FunctionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>versions</code> resource, the following permissions are required:

### Create
```json
lambda:PublishVersion,
lambda:GetFunctionConfiguration,
lambda:PutProvisionedConcurrencyConfig,
lambda:GetProvisionedConcurrencyConfig,
lambda:PutRuntimeManagementConfig,
lambda:GetRuntimeManagementConfig
```

### Read
```json
lambda:GetFunctionConfiguration,
lambda:GetProvisionedConcurrencyConfig,
lambda:GetRuntimeManagementConfig
```

### Delete
```json
lambda:GetFunctionConfiguration,
lambda:DeleteFunction
```

### List
```json
lambda:ListVersionsByFunction
```

