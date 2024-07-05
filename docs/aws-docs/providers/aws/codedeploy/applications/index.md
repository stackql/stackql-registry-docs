---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - codedeploy
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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodeDeploy::Application resource creates an AWS CodeDeploy application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codedeploy.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>A name for the application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.</td></tr>
<tr><td><CopyableCode code="compute_platform" /></td><td><code>string</code></td><td>The compute platform that CodeDeploy deploys the application to.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>applications</code> in a region.
```sql
SELECT
region,
application_name,
compute_platform,
tags
FROM aws.codedeploy.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
application_name,
compute_platform,
tags
FROM aws.codedeploy.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codedeploy.applications (
 ApplicationName,
 ComputePlatform,
 Tags,
 region
)
SELECT 
'{{ ApplicationName }}',
 '{{ ComputePlatform }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codedeploy.applications (
 ApplicationName,
 ComputePlatform,
 Tags,
 region
)
SELECT 
 '{{ ApplicationName }}',
 '{{ ComputePlatform }}',
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
  - name: application
    props:
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: ComputePlatform
        value: '{{ ComputePlatform }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.codedeploy.applications
WHERE data__Identifier = '<ApplicationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
codedeploy:CreateApplication,
codedeploy:TagResource
```

### Read
```json
codedeploy:GetApplication,
codedeploy:ListTagsForResource
```

### Delete
```json
codedeploy:GetApplication,
codedeploy:DeleteApplication
```

### Update
```json
codedeploy:TagResource,
codedeploy:UntagResource
```

### List
```json
codedeploy:ListApplications
```

