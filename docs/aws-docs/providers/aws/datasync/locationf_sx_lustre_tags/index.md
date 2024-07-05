---
title: locationf_sx_lustre_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_lustre_tags
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

Expands all tag keys and values for <code>locationf_sx_lustres</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_lustre_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxLustre.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.locationf_sx_lustre_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="fsx_filesystem_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx for Lustre file system.</td></tr>
<tr><td><CopyableCode code="security_group_arns" /></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx for Lustre file system.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx for Lustre file system location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the FSx for Lustre location that was described.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>locationf_sx_lustres</code> in a region.
```sql
SELECT
region,
fsx_filesystem_arn,
security_group_arns,
subdirectory,
location_arn,
location_uri,
tag_key,
tag_value
FROM aws.datasync.locationf_sx_lustre_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>locationf_sx_lustre_tags</code> resource, see <a href="/providers/aws/datasync/locationf_sx_lustres/#permissions"><code>locationf_sx_lustres</code></a>


