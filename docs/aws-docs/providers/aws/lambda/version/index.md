---
title: version
hide_title: false
hide_table_of_contents: false
keywords:
  - version
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


Gets or updates an individual <code>version</code> resource, use <code>versions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Version</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The ARN of the version.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version number.</td></tr>
<tr><td><CopyableCode code="code_sha256" /></td><td><code>string</code></td><td>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. Updates are not supported for this property.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the version to override the description in the function configuration. Updates are not supported for this property.</td></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
function_arn,
version,
code_sha256,
description,
function_name,
provisioned_concurrency_config,
runtime_policy
FROM aws.lambda.version
WHERE region = 'us-east-1' AND data__Identifier = '<FunctionArn>';
```


## Permissions

To operate on the <code>version</code> resource, the following permissions are required:

### Read
```json
lambda:GetFunctionConfiguration,
lambda:GetProvisionedConcurrencyConfig,
lambda:GetRuntimeManagementConfig
```

