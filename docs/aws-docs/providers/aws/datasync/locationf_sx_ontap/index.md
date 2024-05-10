---
title: locationf_sx_ontap
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_ontap
  - datasync
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


Gets or updates an individual <code>locationf_sx_ontap</code> resource, use <code>locationf_sx_ontaps</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_ontap</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxONTAP.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.locationf_sx_ontap" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="storage_virtual_machine_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx ONTAP SVM.</td></tr>
<tr><td><CopyableCode code="fsx_filesystem_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx ONAP file system.</td></tr>
<tr><td><CopyableCode code="security_group_arns" /></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx ONTAP file system.</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the FSx ONTAP file system that was described.</td></tr>
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
storage_virtual_machine_arn,
fsx_filesystem_arn,
security_group_arns,
protocol,
subdirectory,
tags,
location_arn,
location_uri
FROM aws.datasync.locationf_sx_ontap
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```


## Permissions

To operate on the <code>locationf_sx_ontap</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationFsxOntap,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationFsxOntap,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

