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
Gets an individual <code>live_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>live_source</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediatailor.live_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The ARN of the live source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>http_package_configurations</code></td><td><code>array</code></td><td>&lt;p&gt;A list of HTTP package configuration parameters for this live source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>live_source_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_location_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to assign to the live source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
http_package_configurations,
live_source_name,
source_location_name,
tags
FROM awscc.mediatailor.live_source
WHERE region = 'us-east-1'
AND data__Identifier = '{LiveSourceName}';
AND data__Identifier = '{SourceLocationName}';
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

