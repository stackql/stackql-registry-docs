---
title: application_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instance
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

Gets or operates on an individual <code>application_instance</code> resource, use <code>application_instances</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ApplicationInstance CloudFormation Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.application_instance" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="default_runtime_context_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_runtime_context_device" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_instance_id_to_replace" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="health_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_overrides_payload" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_instance_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_payload" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.panorama.application_instance
WHERE data__Identifier = '<ApplicationInstanceId>';
```

## Permissions

To operate on the <code>application_instance</code> resource, the following permissions are required:

### Read
```json
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
panorama:ListTagsForResource,
s3:ListObjects,
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

