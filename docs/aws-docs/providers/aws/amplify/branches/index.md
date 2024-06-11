---
title: branches
hide_title: false
hide_table_of_contents: false
keywords:
  - branches
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

Creates, updates, deletes or gets a <code>branch</code> resource or lists <code>branches</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Branch resource creates a new branch within an app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.branches" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="basic_auth_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="backend" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AppId, BranchName, region" /></td>
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
List all <code>branches</code> in a region.
```sql
SELECT
region,
arn
FROM aws.amplify.branches
WHERE region = 'us-east-1';
```
Gets all properties from a <code>branch</code>.
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
FROM aws.amplify.branches
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>branch</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.amplify.branches (
 AppId,
 BranchName,
 region
)
SELECT 
'{{ AppId }}',
 '{{ BranchName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.amplify.branches (
 AppId,
 BasicAuthConfig,
 Backend,
 BranchName,
 BuildSpec,
 Description,
 EnableAutoBuild,
 EnablePerformanceMode,
 EnablePullRequestPreview,
 EnvironmentVariables,
 Framework,
 PullRequestEnvironmentName,
 Stage,
 Tags,
 region
)
SELECT 
 '{{ AppId }}',
 '{{ BasicAuthConfig }}',
 '{{ Backend }}',
 '{{ BranchName }}',
 '{{ BuildSpec }}',
 '{{ Description }}',
 '{{ EnableAutoBuild }}',
 '{{ EnablePerformanceMode }}',
 '{{ EnablePullRequestPreview }}',
 '{{ EnvironmentVariables }}',
 '{{ Framework }}',
 '{{ PullRequestEnvironmentName }}',
 '{{ Stage }}',
 '{{ Tags }}',
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
  - name: branch
    props:
      - name: AppId
        value: '{{ AppId }}'
      - name: BasicAuthConfig
        value:
          EnableBasicAuth: '{{ EnableBasicAuth }}'
          Username: '{{ Username }}'
          Password: '{{ Password }}'
      - name: Backend
        value:
          StackArn: '{{ StackArn }}'
      - name: BranchName
        value: '{{ BranchName }}'
      - name: BuildSpec
        value: '{{ BuildSpec }}'
      - name: Description
        value: '{{ Description }}'
      - name: EnableAutoBuild
        value: '{{ EnableAutoBuild }}'
      - name: EnablePerformanceMode
        value: '{{ EnablePerformanceMode }}'
      - name: EnablePullRequestPreview
        value: '{{ EnablePullRequestPreview }}'
      - name: EnvironmentVariables
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'
      - name: Framework
        value: '{{ Framework }}'
      - name: PullRequestEnvironmentName
        value: '{{ PullRequestEnvironmentName }}'
      - name: Stage
        value: '{{ Stage }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.amplify.branches
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>branches</code> resource, the following permissions are required:

### Create
```json
amplify:GetBranch,
amplify:CreateBranch,
amplify:TagResource,
codecommit:GetRepository,
codecommit:PutRepositoryTriggers,
codecommit:GetRepositoryTriggers,
s3:GetObject,
s3:GetObjectAcl,
s3:PutObject,
s3:PutObjectAcl,
sns:CreateTopic,
sns:Subscribe,
iam:PassRole
```

### Delete
```json
amplify:GetBranch,
amplify:DeleteBranch,
codecommit:GetRepository,
codecommit:GetRepositoryTriggers,
sns:Unsubscribe,
iam:PassRole
```

### List
```json
amplify:GetBranch,
amplify:ListBranches,
amplify:ListTagsForResource,
iam:PassRole
```

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

