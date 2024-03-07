---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
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
Gets an individual <code>channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>channel</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackage.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the Channel.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the Channel.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A short text description of the Channel.</td></tr>
<tr><td><code>hls_ingest</code></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) ingest resource configuration.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>egress_access_logs</code></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
<tr><td><code>ingress_access_logs</code></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>channel</code> resource, the following permissions are required:

### Read
<pre>
mediapackage:DescribeChannel</pre>

### Update
<pre>
mediapackage:UpdateChannel,
mediapackage:ConfigureLogs,
iam:CreateServiceLinkedRole</pre>

### Delete
<pre>
mediapackage:DeleteChannel</pre>


## Example
```sql
SELECT
region,
arn,
id,
description,
hls_ingest,
tags,
egress_access_logs,
ingress_access_logs
FROM awscc.mediapackage.channel
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
