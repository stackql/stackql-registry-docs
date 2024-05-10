---
title: application_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instances
  - panorama
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


Used to retrieve a list of <code>application_instances</code> in a region or to create or delete a <code>application_instances</code> resource, use <code>application_instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ApplicationInstance CloudFormation Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.application_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_instance_id" /></td><td><code>undefined</code></td><td></td></tr>
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
application_instance_id
FROM aws.panorama.application_instances
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
 "DefaultRuntimeContextDevice": "{{ DefaultRuntimeContextDevice }}",
 "ManifestPayload": {
  "PayloadData": "{{ PayloadData }}"
 }
}
>>>
--required properties only
INSERT INTO aws.panorama.application_instances (
 DefaultRuntimeContextDevice,
 ManifestPayload,
 region
)
SELECT 
{{ .DefaultRuntimeContextDevice }},
 {{ .ManifestPayload }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DefaultRuntimeContextDevice": "{{ DefaultRuntimeContextDevice }}",
 "Description": "{{ Description }}",
 "ApplicationInstanceIdToReplace": "{{ ApplicationInstanceIdToReplace }}",
 "ManifestOverridesPayload": {
  "PayloadData": "{{ PayloadData }}"
 },
 "RuntimeRoleArn": "{{ RuntimeRoleArn }}",
 "Name": "{{ Name }}",
 "ManifestPayload": {
  "PayloadData": "{{ PayloadData }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.panorama.application_instances (
 DefaultRuntimeContextDevice,
 Description,
 ApplicationInstanceIdToReplace,
 ManifestOverridesPayload,
 RuntimeRoleArn,
 Name,
 ManifestPayload,
 Tags,
 region
)
SELECT 
 {{ .DefaultRuntimeContextDevice }},
 {{ .Description }},
 {{ .ApplicationInstanceIdToReplace }},
 {{ .ManifestOverridesPayload }},
 {{ .RuntimeRoleArn }},
 {{ .Name }},
 {{ .ManifestPayload }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.panorama.application_instances
WHERE data__Identifier = '<ApplicationInstanceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>application_instances</code> resource, the following permissions are required:

### Create
```json
panorama:CreateApplicationInstance,
panorama:ListTagsForResource,
panorama:TagResource,
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
iam:PassRole,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### List
```json
panorama:ListApplicationInstances,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
panorama:RemoveApplicationInstance,
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
s3:DeleteObject,
s3:DeleteObjectVersion,
s3:DeleteObjectVersionTagging,
s3:ListObjects,
s3:GetObject,
s3:GetObjectVersion
```

