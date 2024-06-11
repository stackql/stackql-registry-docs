---
title: web_experiences
hide_title: false
hide_table_of_contents: false
keywords:
  - web_experiences
  - qbusiness
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

Creates, updates, deletes or gets a <code>web_experience</code> resource or lists <code>web_experiences</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_experiences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::WebExperience Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.web_experiences" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sample_prompts_control_mode" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="subtitle" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="title" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_experience_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_experience_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="welcome_message" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ApplicationId, region" /></td>
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
List all <code>web_experiences</code> in a region.
```sql
SELECT
region,
application_id,
web_experience_id
FROM aws.qbusiness.web_experiences
WHERE region = 'us-east-1';
```
Gets all properties from a <code>web_experience</code>.
```sql
SELECT
region,
application_id,
created_at,
default_endpoint,
role_arn,
sample_prompts_control_mode,
status,
subtitle,
tags,
title,
updated_at,
web_experience_arn,
web_experience_id,
welcome_message
FROM aws.qbusiness.web_experiences
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<WebExperienceId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_experience</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.web_experiences (
 ApplicationId,
 region
)
SELECT 
'{{ ApplicationId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.web_experiences (
 ApplicationId,
 RoleArn,
 SamplePromptsControlMode,
 Subtitle,
 Tags,
 Title,
 WelcomeMessage,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ RoleArn }}',
 '{{ SamplePromptsControlMode }}',
 '{{ Subtitle }}',
 '{{ Tags }}',
 '{{ Title }}',
 '{{ WelcomeMessage }}',
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
  - name: web_experience
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: SamplePromptsControlMode
        value: '{{ SamplePromptsControlMode }}'
      - name: Subtitle
        value: '{{ Subtitle }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Title
        value: '{{ Title }}'
      - name: WelcomeMessage
        value: '{{ WelcomeMessage }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.qbusiness.web_experiences
WHERE data__Identifier = '<ApplicationId|WebExperienceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>web_experiences</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
qbusiness:CreateWebExperience,
qbusiness:GetWebExperience,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
sso:PutApplicationGrant,
sso:UpdateApplication
```

### Read
```json
qbusiness:GetWebExperience,
qbusiness:ListTagsForResource
```

### Update
```json
iam:PassRole,
qbusiness:GetWebExperience,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdateWebExperience,
sso:PutApplicationGrant,
sso:UpdateApplication
```

### Delete
```json
qbusiness:DeleteWebExperience,
qbusiness:GetWebExperience
```

### List
```json
qbusiness:ListWebExperiences
```

