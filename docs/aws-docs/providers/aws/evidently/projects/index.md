---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - evidently
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

Creates, updates, deletes or gets a <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Project</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_delivery" /></td><td><code>object</code></td><td>Destinations for data.</td></tr>
<tr><td><CopyableCode code="app_config_resource" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html"><code>AWS::Evidently::Project</code></a>.

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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>project</code>.
```sql
SELECT
region,
arn,
name,
description,
data_delivery,
app_config_resource,
tags
FROM aws.evidently.projects
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.evidently.projects (
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
INSERT INTO aws.evidently.projects (
 Name,
 Description,
 DataDelivery,
 AppConfigResource,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ DataDelivery }}',
 '{{ AppConfigResource }}',
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
  - name: project
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: DataDelivery
        value:
          S3:
            BucketName: '{{ BucketName }}'
            Prefix: '{{ Prefix }}'
          LogGroup: '{{ LogGroup }}'
      - name: AppConfigResource
        value:
          ApplicationId: '{{ ApplicationId }}'
          EnvironmentId: '{{ EnvironmentId }}'
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
DELETE FROM aws.evidently.projects
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
evidently:CreateProject,
evidently:GetProject,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
evidently:TagResource,
evidently:ExportProjectAsConfiguration,
appconfig:GetEnvironment,
appconfig:CreateConfigurationProfile,
appconfig:CreateHostedConfigurationVersion,
appconfig:CreateExtensionAssociation,
appconfig:TagResource,
iam:GetRole,
iam:CreateServiceLinkedRole
```

### Read
```json
evidently:GetProject,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:GetBucketPolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateProject,
evidently:UpdateProjectDataDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
evidently:TagResource,
evidently:UntagResource,
evidently:ListTagsForResource,
evidently:GetProject,
evidently:ExportProjectAsConfiguration,
appconfig:GetEnvironment,
appconfig:CreateConfigurationProfile,
appconfig:CreateHostedConfigurationVersion,
appconfig:CreateExtensionAssociation,
appconfig:TagResource,
iam:GetRole,
iam:CreateServiceLinkedRole
```

### Delete
```json
evidently:DeleteProject,
evidently:GetProject,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
s3:GetBucketPolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
evidently:UntagResource,
appconfig:DeleteHostedConfigurationVersion,
appconfig:DeleteExtensionAssociation,
appconfig:DeleteConfigurationProfile
```
