---
title: branch
hide_title: false
hide_table_of_contents: false
keywords:
  - branch
  - amplify
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


Gets or updates an individual <code>branch</code> resource, use <code>branches</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Branch resource creates a new branch within an app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.branch" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="basic_auth_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="backend" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="branch_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="build_spec" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_auto_build" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_performance_mode" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_pull_request_preview" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_variables" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="framework" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pull_request_environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
app_id,
arn,
basic_auth_config,
backend,
branch_name,
build_spec,
description,
enable_auto_build,
enable_performance_mode,
enable_pull_request_preview,
environment_variables,
framework,
pull_request_environment_name,
stage,
tags
FROM aws.amplify.branch
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>branch</code> resource, the following permissions are required:

### Read
```json
amplify:GetBranch,
amplify:ListTagsForResource,
codecommit:GetRepository,
codecommit:GetRepositoryTriggers,
s3:GetObject,
s3:GetObjectAcl,
iam:PassRole
```

### Update
```json
amplify:GetBranch,
amplify:UpdateBranch,
amplify:ListTagsForResource,
amplify:TagResource,
amplify:UntagResource,
codecommit:GetRepository,
codecommit:PutRepositoryTriggers,
codecommit:GetRepositoryTriggers,
s3:GetObject,
s3:GetObjectAcl,
s3:PutObject,
s3:PutObjectAcl,
sns:CreateTopic,
sns:Subscribe,
sns:Unsubscribe,
iam:PassRole
```

