---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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

Creates, updates, deletes or gets an <code>app</code> resource or lists <code>apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.apps" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_branch_creation_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="basic_auth_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="build_spec" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cache_config" /></td><td><code>object</code></td><td></td></tr>
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

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html"><code>AWS::Amplify::App</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>apps</code> in a region.
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
cache_config,
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
FROM aws.amplify.apps
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>app</code>.
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
cache_config,
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
FROM aws.amplify.apps
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.amplify.apps (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.amplify.apps (
 AccessToken,
 AutoBranchCreationConfig,
 BasicAuthConfig,
 BuildSpec,
 CacheConfig,
 CustomHeaders,
 CustomRules,
 Description,
 EnableBranchAutoDeletion,
 EnvironmentVariables,
 IAMServiceRole,
 Name,
 OauthToken,
 Platform,
 Repository,
 Tags,
 region
)
SELECT 
 '{{ AccessToken }}',
 '{{ AutoBranchCreationConfig }}',
 '{{ BasicAuthConfig }}',
 '{{ BuildSpec }}',
 '{{ CacheConfig }}',
 '{{ CustomHeaders }}',
 '{{ CustomRules }}',
 '{{ Description }}',
 '{{ EnableBranchAutoDeletion }}',
 '{{ EnvironmentVariables }}',
 '{{ IAMServiceRole }}',
 '{{ Name }}',
 '{{ OauthToken }}',
 '{{ Platform }}',
 '{{ Repository }}',
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
  - name: app
    props:
      - name: AccessToken
        value: '{{ AccessToken }}'
      - name: AutoBranchCreationConfig
        value:
          AutoBranchCreationPatterns:
            - '{{ AutoBranchCreationPatterns[0] }}'
          BasicAuthConfig:
            EnableBasicAuth: '{{ EnableBasicAuth }}'
            Username: '{{ Username }}'
            Password: '{{ Password }}'
          BuildSpec: '{{ BuildSpec }}'
          EnableAutoBranchCreation: '{{ EnableAutoBranchCreation }}'
          EnableAutoBuild: '{{ EnableAutoBuild }}'
          EnablePerformanceMode: '{{ EnablePerformanceMode }}'
          EnablePullRequestPreview: '{{ EnablePullRequestPreview }}'
          EnvironmentVariables:
            - Name: '{{ Name }}'
              Value: '{{ Value }}'
          Framework: '{{ Framework }}'
          PullRequestEnvironmentName: '{{ PullRequestEnvironmentName }}'
          Stage: '{{ Stage }}'
      - name: BasicAuthConfig
        value: null
      - name: BuildSpec
        value: '{{ BuildSpec }}'
      - name: CacheConfig
        value:
          Type: '{{ Type }}'
      - name: CustomHeaders
        value: '{{ CustomHeaders }}'
      - name: CustomRules
        value:
          - Condition: '{{ Condition }}'
            Status: '{{ Status }}'
            Target: '{{ Target }}'
            Source: '{{ Source }}'
      - name: Description
        value: '{{ Description }}'
      - name: EnableBranchAutoDeletion
        value: '{{ EnableBranchAutoDeletion }}'
      - name: EnvironmentVariables
        value:
          - null
      - name: IAMServiceRole
        value: '{{ IAMServiceRole }}'
      - name: Name
        value: '{{ Name }}'
      - name: OauthToken
        value: '{{ OauthToken }}'
      - name: Platform
        value: '{{ Platform }}'
      - name: Repository
        value: '{{ Repository }}'
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
DELETE FROM aws.amplify.apps
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>apps</code> resource, the following permissions are required:

### Create
```json
amplify:GetApp,
amplify:CreateApp,
amplify:TagResource,
codecommit:GetRepository,
codecommit:PutRepositoryTriggers,
codecommit:GetRepositoryTriggers,
sns:CreateTopic,
sns:Subscribe,
iam:PassRole
```

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

### List
```json
amplify:GetApp,
amplify:ListApps,
amplify:ListTagsForResource,
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
