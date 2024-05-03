---
title: live_source
hide_title: false
hide_table_of_contents: false
keywords:
  - live_source
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

Gets or operates on an individual <code>live_source</code> resource, use <code>live_sources</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::LiveSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.live_source" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The ARN of the live source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="http_package_configurations" /></td><td><code>array</code></td><td>&lt;p&gt;A list of HTTP package configuration parameters for this live source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="live_source_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the live source.</td></tr>
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
live_source_name,
source_location_name,
tags
FROM aws.mediatailor.live_source
WHERE data__Identifier = '<LiveSourceName>|<SourceLocationName>';
```

## Permissions

To operate on the <code>live_source</code> resource, the following permissions are required:

### Read
```json
mediatailor:DescribeLiveSource
```

### Update
```json
mediatailor:UpdateLiveSource,
mediatailor:DescribeLiveSource,
mediatailor:TagResource,
mediatailor:UntagResource
```

### Delete
```json
mediatailor:DeleteLiveSource,
mediatailor:DescribeLiveSource
```

