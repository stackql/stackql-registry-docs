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


Used to retrieve a list of <code>apps</code> in a region or to create or delete a <code>apps</code> resource, use <code>app</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.apps" /></td></tr>
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
arn
FROM aws.amplify.apps
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
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.amplify.apps (
 Name,
 region
)
SELECT 
{{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccessToken": "{{ AccessToken }}",
 "AutoBranchCreationConfig": {
  "AutoBranchCreationPatterns": [
   "{{ AutoBranchCreationPatterns[0] }}"
  ],
  "BasicAuthConfig": {
   "EnableBasicAuth": "{{ EnableBasicAuth }}",
   "Username": "{{ Username }}",
   "Password": "{{ Password }}"
  },
  "BuildSpec": "{{ BuildSpec }}",
  "EnableAutoBranchCreation": "{{ EnableAutoBranchCreation }}",
  "EnableAutoBuild": "{{ EnableAutoBuild }}",
  "EnablePerformanceMode": "{{ EnablePerformanceMode }}",
  "EnablePullRequestPreview": "{{ EnablePullRequestPreview }}",
  "EnvironmentVariables": [
   {
    "Name": "{{ Name }}",
    "Value": "{{ Value }}"
   }
  ],
  "Framework": "{{ Framework }}",
  "PullRequestEnvironmentName": "{{ PullRequestEnvironmentName }}",
  "Stage": "{{ Stage }}"
 },
 "BasicAuthConfig": null,
 "BuildSpec": "{{ BuildSpec }}",
 "CustomHeaders": "{{ CustomHeaders }}",
 "CustomRules": [
  {
   "Condition": "{{ Condition }}",
   "Status": "{{ Status }}",
   "Target": "{{ Target }}",
   "Source": "{{ Source }}"
  }
 ],
 "Description": "{{ Description }}",
 "EnableBranchAutoDeletion": "{{ EnableBranchAutoDeletion }}",
 "EnvironmentVariables": [
  null
 ],
 "IAMServiceRole": "{{ IAMServiceRole }}",
 "Name": "{{ Name }}",
 "OauthToken": "{{ OauthToken }}",
 "Platform": "{{ Platform }}",
 "Repository": "{{ Repository }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.amplify.apps (
 AccessToken,
 AutoBranchCreationConfig,
 BasicAuthConfig,
 BuildSpec,
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
 {{ AccessToken }},
 {{ AutoBranchCreationConfig }},
 {{ BasicAuthConfig }},
 {{ BuildSpec }},
 {{ CustomHeaders }},
 {{ CustomRules }},
 {{ Description }},
 {{ EnableBranchAutoDeletion }},
 {{ EnvironmentVariables }},
 {{ IAMServiceRole }},
 {{ Name }},
 {{ OauthToken }},
 {{ Platform }},
 {{ Repository }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

