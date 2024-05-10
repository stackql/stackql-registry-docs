---
title: packaging_group
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_group
  - mediapackage
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


Gets or updates an individual <code>packaging_group</code> resource, use <code>packaging_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::PackagingGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.packaging_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the PackagingGroup.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the PackagingGroup.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The fully qualified domain name for Assets in the PackagingGroup.</td></tr>
<tr><td><CopyableCode code="authorization" /></td><td><code>object</code></td><td>CDN Authorization</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="egress_access_logs" /></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
arn,
domain_name,
authorization,
tags,
egress_access_logs
FROM aws.mediapackage.packaging_group
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>packaging_group</code> resource, the following permissions are required:

### Read
```json
mediapackage-vod:DescribePackagingGroup
```

### Update
```json
mediapackage-vod:DescribePackagingGroup,
mediapackage-vod:UpdatePackagingGroup,
mediapackage-vod:ConfigureLogs,
mediapackage-vod:TagResource,
iam:PassRole,
iam:CreateServiceLinkedRole
```

