---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - appstream
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_parameters" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="working_directory" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_families" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="icon_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_block_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="platforms" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="attributes_to_delete" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, IconS3Location, LaunchPath, Platforms, InstanceFamilies, AppBlockArn, region" /></td>
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

Gets all properties from an <code>application</code>.
```sql
SELECT
region,
name,
display_name,
description,
launch_path,
launch_parameters,
working_directory,
instance_families,
icon_s3_location,
arn,
app_block_arn,
platforms,
tags,
attributes_to_delete,
created_time
FROM aws.appstream.applications
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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
INSERT INTO aws.appstream.applications (
 Name,
 LaunchPath,
 InstanceFamilies,
 IconS3Location,
 AppBlockArn,
 Platforms,
 region
)
SELECT 
'{{ Name }}',
 '{{ LaunchPath }}',
 '{{ InstanceFamilies }}',
 '{{ IconS3Location }}',
 '{{ AppBlockArn }}',
 '{{ Platforms }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appstream.applications (
 Name,
 DisplayName,
 Description,
 LaunchPath,
 LaunchParameters,
 WorkingDirectory,
 InstanceFamilies,
 IconS3Location,
 AppBlockArn,
 Platforms,
 Tags,
 AttributesToDelete,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DisplayName }}',
 '{{ Description }}',
 '{{ LaunchPath }}',
 '{{ LaunchParameters }}',
 '{{ WorkingDirectory }}',
 '{{ InstanceFamilies }}',
 '{{ IconS3Location }}',
 '{{ AppBlockArn }}',
 '{{ Platforms }}',
 '{{ Tags }}',
 '{{ AttributesToDelete }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: Description
        value: '{{ Description }}'
      - name: LaunchPath
        value: '{{ LaunchPath }}'
      - name: LaunchParameters
        value: '{{ LaunchParameters }}'
      - name: WorkingDirectory
        value: '{{ WorkingDirectory }}'
      - name: InstanceFamilies
        value:
          - '{{ InstanceFamilies[0] }}'
      - name: IconS3Location
        value:
          S3Bucket: '{{ S3Bucket }}'
          S3Key: '{{ S3Key }}'
      - name: AppBlockArn
        value: '{{ AppBlockArn }}'
      - name: Platforms
        value:
          - '{{ Platforms[0] }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: AttributesToDelete
        value:
          - '{{ AttributesToDelete[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appstream.applications
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
s3:GetObject,
appstream:CreateApplication,
appstream:TagResource
```

### Read
```json
appstream:DescribeApplications
```

### Update
```json
appstream:UpdateApplication,
s3:GetObject
```

### Delete
```json
appstream:DeleteApplication
```

