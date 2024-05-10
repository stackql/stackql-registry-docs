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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
FROM aws.appstream.applications
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
 "Name": "{{ Name }}",
 "LaunchPath": "{{ LaunchPath }}",
 "InstanceFamilies": [
  "{{ InstanceFamilies[0] }}"
 ],
 "IconS3Location": {
  "S3Bucket": "{{ S3Bucket }}",
  "S3Key": "{{ S3Key }}"
 },
 "AppBlockArn": "{{ AppBlockArn }}",
 "Platforms": [
  "{{ Platforms[0] }}"
 ]
}
>>>
--required properties only
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
{{ .Name }},
 {{ .LaunchPath }},
 {{ .InstanceFamilies }},
 {{ .IconS3Location }},
 {{ .AppBlockArn }},
 {{ .Platforms }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "DisplayName": "{{ DisplayName }}",
 "Description": "{{ Description }}",
 "LaunchPath": "{{ LaunchPath }}",
 "LaunchParameters": "{{ LaunchParameters }}",
 "WorkingDirectory": "{{ WorkingDirectory }}",
 "InstanceFamilies": [
  "{{ InstanceFamilies[0] }}"
 ],
 "IconS3Location": {
  "S3Bucket": "{{ S3Bucket }}",
  "S3Key": "{{ S3Key }}"
 },
 "AppBlockArn": "{{ AppBlockArn }}",
 "Platforms": [
  "{{ Platforms[0] }}"
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "AttributesToDelete": [
  "{{ AttributesToDelete[0] }}"
 ]
}
>>>
--all properties
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
 {{ .Name }},
 {{ .DisplayName }},
 {{ .Description }},
 {{ .LaunchPath }},
 {{ .LaunchParameters }},
 {{ .WorkingDirectory }},
 {{ .InstanceFamilies }},
 {{ .IconS3Location }},
 {{ .AppBlockArn }},
 {{ .Platforms }},
 {{ .Tags }},
 {{ .AttributesToDelete }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
appstream:DeleteApplication
```

