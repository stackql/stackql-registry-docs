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


Used to retrieve a list of <code>versions</code> in a region or to create or delete a <code>versions</code> resource, use <code>version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Version</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The ARN of the version.</td></tr>
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
FROM aws.lambda.versions
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
 "FunctionName": "{{ FunctionName }}"
}
>>>
--required properties only
INSERT INTO aws.lambda.versions (
 FunctionName,
 region
)
SELECT 
{{ .FunctionName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CodeSha256": "{{ CodeSha256 }}",
 "Description": "{{ Description }}",
 "FunctionName": "{{ FunctionName }}",
 "ProvisionedConcurrencyConfig": {
  "ProvisionedConcurrentExecutions": "{{ ProvisionedConcurrentExecutions }}"
 },
 "RuntimePolicy": {
  "RuntimeVersionArn": "{{ RuntimeVersionArn }}",
  "UpdateRuntimeOn": "{{ UpdateRuntimeOn }}"
 }
}
>>>
--all properties
INSERT INTO aws.lambda.versions (
 CodeSha256,
 Description,
 FunctionName,
 ProvisionedConcurrencyConfig,
 RuntimePolicy,
 region
)
SELECT 
 {{ .CodeSha256 }},
 {{ .Description }},
 {{ .FunctionName }},
 {{ .ProvisionedConcurrencyConfig }},
 {{ .RuntimePolicy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
lambda:GetFunctionConfiguration,
lambda:DeleteFunction
```

### List
```json
lambda:ListVersionsByFunction
```

