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


Used to retrieve a list of <code>branches</code> in a region or to create or delete a <code>branches</code> resource, use <code>branch</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Branch resource creates a new branch within an app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.branches" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.amplify.branches
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

