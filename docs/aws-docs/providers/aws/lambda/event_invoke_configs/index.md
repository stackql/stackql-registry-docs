---
title: event_invoke_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_configs
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


Used to retrieve a list of <code>event_invoke_configs</code> in a region or to create or delete a <code>event_invoke_configs</code> resource, use <code>event_invoke_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Lambda::EventInvokeConfig resource configures options for asynchronous invocation on a version or an alias.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.event_invoke_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><CopyableCode code="qualifier" /></td><td><code>string</code></td><td>The identifier of a version or alias.</td></tr>
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
function_name,
qualifier
FROM aws.lambda.event_invoke_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>event_invoke_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- event_invoke_config.iql (required properties only)
INSERT INTO aws.lambda.event_invoke_configs (
 FunctionName,
 Qualifier,
 region
)
SELECT 
'{{ FunctionName }}',
 '{{ Qualifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- event_invoke_config.iql (all properties)
INSERT INTO aws.lambda.event_invoke_configs (
 DestinationConfig,
 FunctionName,
 MaximumEventAgeInSeconds,
 MaximumRetryAttempts,
 Qualifier,
 region
)
SELECT 
 '{{ DestinationConfig }}',
 '{{ FunctionName }}',
 '{{ MaximumEventAgeInSeconds }}',
 '{{ MaximumRetryAttempts }}',
 '{{ Qualifier }}',
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
  - name: event_invoke_config
    props:
      - name: DestinationConfig
        value:
          OnFailure:
            Destination: '{{ Destination }}'
      - name: FunctionName
        value: '{{ FunctionName }}'
      - name: MaximumEventAgeInSeconds
        value: '{{ MaximumEventAgeInSeconds }}'
      - name: MaximumRetryAttempts
        value: '{{ MaximumRetryAttempts }}'
      - name: Qualifier
        value: '{{ Qualifier }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lambda.event_invoke_configs
WHERE data__Identifier = '<FunctionName|Qualifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_invoke_configs</code> resource, the following permissions are required:

### Create
```json
lambda:PutFunctionEventInvokeConfig
```

### Delete
```json
lambda:DeleteFunctionEventInvokeConfig
```

### List
```json
lambda:ListFunctionEventInvokeConfigs
```

