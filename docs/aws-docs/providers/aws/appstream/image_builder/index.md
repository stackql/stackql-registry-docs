---
title: image_builder
hide_title: false
hide_table_of_contents: false
keywords:
  - image_builder
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

Gets or operates on an individual <code>image_builder</code> resource, use <code>image_builders</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_builder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::ImageBuilder</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.image_builder" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_default_internet_access" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_join_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="appstream_agent_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="streaming_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="access_endpoints" /></td><td><code>array</code></td><td></td></tr>
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
description,
vpc_config,
enable_default_internet_access,
domain_join_info,
appstream_agent_version,
name,
image_name,
display_name,
iam_role_arn,
instance_type,
tags,
streaming_url,
image_arn,
access_endpoints
FROM aws.appstream.image_builder
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>image_builder</code> resource, the following permissions are required:

### Read
```json
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Delete
```json
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

