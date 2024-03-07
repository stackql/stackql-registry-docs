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
Gets an individual <code>app</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the app.</td></tr>
<tr><td><code>app_name</code></td><td><code>string</code></td><td>The name of the app.</td></tr>
<tr><td><code>app_type</code></td><td><code>string</code></td><td>The type of app.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The domain ID.</td></tr>
<tr><td><code>resource_spec</code></td><td><code>object</code></td><td>The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags to apply to the app.</td></tr>
<tr><td><code>user_profile_name</code></td><td><code>string</code></td><td>The user profile name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
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
FROM awscc.sagemaker.app
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AppName&gt;'
AND data__Identifier = '&lt;AppType&gt;'
AND data__Identifier = '&lt;DomainId&gt;'
AND data__Identifier = '&lt;UserProfileName&gt;'
```
