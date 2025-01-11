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

Creates, updates, deletes or gets an <code>application_instance</code> resource or lists <code>application_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an application instance and deploys it to a device.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.application_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_runtime_context_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_runtime_context_device" /></td><td><code>string</code></td><td>The device's ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the application instance.</td></tr>
<tr><td><CopyableCode code="application_instance_id_to_replace" /></td><td><code>string</code></td><td>The ID of an application instance to replace with the new instance.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="health_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_overrides_payload" /></td><td><code>object</code></td><td>Setting overrides for the application manifest.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td>The ARN of a runtime role for the application instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the application instance.</td></tr>
<tr><td><CopyableCode code="application_instance_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_payload" /></td><td><code>object</code></td><td>The application's manifest document.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for the application instance.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html"><code>AWS::Panorama::ApplicationInstance</code></a>.

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
    <td><CopyableCode code="ManifestPayload, DefaultRuntimeContextDevice, region" /></td>
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
Gets all <code>application_instances</code> in a region.
```sql
SELECT
region,
default_runtime_context_device_name,
status,
default_runtime_context_device,
description,
application_instance_id_to_replace,
created_time,
health_status,
manifest_overrides_payload,
last_updated_time,
runtime_role_arn,
name,
application_instance_id,
status_description,
manifest_payload,
arn,
tags
FROM aws.panorama.application_instances
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application_instance</code>.
```sql
SELECT
region,
default_runtime_context_device_name,
status,
default_runtime_context_device,
description,
application_instance_id_to_replace,
created_time,
health_status,
manifest_overrides_payload,
last_updated_time,
runtime_role_arn,
name,
application_instance_id,
status_description,
manifest_payload,
arn,
tags
FROM aws.panorama.application_instances
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationInstanceId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_instance</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.panorama.application_instances (
 DefaultRuntimeContextDevice,
 ManifestPayload,
 region
)
SELECT 
'{{ DefaultRuntimeContextDevice }}',
 '{{ ManifestPayload }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ DefaultRuntimeContextDevice }}',
 '{{ Description }}',
 '{{ ApplicationInstanceIdToReplace }}',
 '{{ ManifestOverridesPayload }}',
 '{{ RuntimeRoleArn }}',
 '{{ Name }}',
 '{{ ManifestPayload }}',
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
  - name: application_instance
    props:
      - name: DefaultRuntimeContextDevice
        value: '{{ DefaultRuntimeContextDevice }}'
      - name: Description
        value: '{{ Description }}'
      - name: ApplicationInstanceIdToReplace
        value: '{{ ApplicationInstanceIdToReplace }}'
      - name: ManifestOverridesPayload
        value:
          PayloadData: '{{ PayloadData }}'
      - name: RuntimeRoleArn
        value: '{{ RuntimeRoleArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: ManifestPayload
        value:
          PayloadData: '{{ PayloadData }}'
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
DELETE FROM aws.panorama.application_instances
WHERE data__Identifier = '<ApplicationInstanceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>application_instances</code> resource, the following permissions are required:

### Read
```json
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
panorama:ListTagsForResource,
s3:ListObjects,
s3:GetObject,
s3:GetObjectVersion
```

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

### Update
```json
panorama:ListTagsForResource,
panorama:TagResource,
panorama:UntagResource,
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
s3:ListObjects,
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
