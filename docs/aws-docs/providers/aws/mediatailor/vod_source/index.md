---
title: vod_source
hide_title: false
hide_table_of_contents: false
keywords:
  - vod_source
  - mediatailor
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

Gets or operates on an individual <code>vod_source</code> resource, use <code>vod_sources</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vod_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::VodSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.vod_source" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The ARN of the VOD source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="http_package_configurations" /></td><td><code>array</code></td><td>&lt;p&gt;A list of HTTP package configuration parameters for this VOD source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the VOD source.</td></tr>
<tr><td><CopyableCode code="vod_source_name" /></td><td><code>string</code></td><td></td></tr>
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
arn,
http_package_configurations,
source_location_name,
tags,
vod_source_name
FROM aws.mediatailor.vod_source
WHERE data__Identifier = '<SourceLocationName>|<VodSourceName>';
```

## Permissions

To operate on the <code>vod_source</code> resource, the following permissions are required:

### Read
```json
mediatailor:DescribeVodSource
```

### Update
```json
mediatailor:DescribeVodSource,
mediatailor:TagResource,
mediatailor:UntagResource,
mediatailor:UpdateVodSource
```

### Delete
```json
mediatailor:DeleteVodSource,
mediatailor:DescribeVodSource
```

