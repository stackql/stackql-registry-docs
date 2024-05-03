---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
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

Gets or operates on an individual <code>app</code> resource, use <code>apps</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.app" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_branch_creation_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="basic_auth_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="build_spec" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_headers" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_branch_auto_deletion" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_variables" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="iam_service_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="oauth_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="platform" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="repository" /></td><td><code>string</code></td><td></td></tr>
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
access_token,
app_id,
app_name,
arn,
auto_branch_creation_config,
basic_auth_config,
build_spec,
custom_headers,
custom_rules,
default_domain,
description,
enable_branch_auto_deletion,
environment_variables,
iam_service_role,
name,
oauth_token,
platform,
repository,
tags
FROM aws.amplify.app
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>app</code> resource, the following permissions are required:

### Delete
```json
amplify:GetApp,
amplify:DeleteApp,
codecommit:GetRepository,
codecommit:GetRepositoryTriggers,
codecommit:PutRepositoryTriggers,
sns:Unsubscribe,
iam:PassRole
```

### Read
```json
amplify:GetApp,
amplify:ListTagsForResource,
codecommit:GetRepository,
codecommit:GetRepositoryTriggers,
iam:PassRole
```

### Update
```json
amplify:GetApp,
amplify:UpdateApp,
amplify:ListTagsForResource,
amplify:TagResource,
amplify:UntagResource,
codecommit:GetRepository,
codecommit:PutRepositoryTriggers,
codecommit:GetRepositoryTriggers,
sns:CreateTopic,
sns:Subscribe,
sns:Unsubscribe,
iam:PassRole
```

