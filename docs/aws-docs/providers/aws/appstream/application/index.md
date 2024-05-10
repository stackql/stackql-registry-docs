---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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


Gets or updates an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.appstream.application
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
appstream:DescribeApplications
```

### Update
```json
appstream:UpdateApplication,
s3:GetObject
```

