---
title: origin_endpoint_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoint_policy
  - mediapackagev2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>origin_endpoint_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_endpoint_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackagev2.origin_endpoint_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>channel_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>origin_endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>origin_endpoint_policy</code> resource, the following permissions are required:

### Read
```json
mediapackagev2:GetOriginEndpointPolicy
```

### Update
```json
mediapackagev2:GetOriginEndpointPolicy,
mediapackagev2:PutOriginEndpointPolicy
```

### Delete
```json
mediapackagev2:GetOriginEndpointPolicy,
mediapackagev2:DeleteOriginEndpointPolicy
```


## Example
```sql
SELECT
region,
channel_group_name,
channel_name,
origin_endpoint_name,
policy
FROM awscc.mediapackagev2.origin_endpoint_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ChannelGroupName&gt;'
AND data__Identifier = '&lt;ChannelName&gt;'
AND data__Identifier = '&lt;OriginEndpointName&gt;'
```
