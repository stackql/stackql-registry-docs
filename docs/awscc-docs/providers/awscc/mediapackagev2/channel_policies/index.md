---
title: channel_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_policies
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
Retrieves a list of <code>channel_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>channel_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackagev2.channel_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>channel_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
channel_group_name,
channel_name
FROM awscc.mediapackagev2.channel_policies
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>channel_policies</code> resource, the following permissions are required:

### Create
```json
mediapackagev2:GetChannelPolicy,
mediapackagev2:PutChannelPolicy
```

