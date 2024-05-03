---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
  - sagemaker
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

Gets or operates on an individual <code>app</code> resource, use <code>apps</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::App</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.app" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the app.</td></tr>
<tr><td><CopyableCode code="app_name" /></td><td><code>string</code></td><td>The name of the app.</td></tr>
<tr><td><CopyableCode code="app_type" /></td><td><code>string</code></td><td>The type of app.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The domain ID.</td></tr>
<tr><td><CopyableCode code="resource_spec" /></td><td><code>object</code></td><td>The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the app.</td></tr>
<tr><td><CopyableCode code="user_profile_name" /></td><td><code>string</code></td><td>The user profile name.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
app_arn,
app_name,
app_type,
domain_id,
resource_spec,
tags,
user_profile_name
FROM aws.sagemaker.app
WHERE data__Identifier = '<AppName>|<AppType>|<DomainId>|<UserProfileName>';
```

## Permissions

To operate on the <code>app</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeApp,
sagemaker:DescribeApp
```

### Delete
```json
sagemaker:DeleteApp,
sagemaker:DescribeApp
```

