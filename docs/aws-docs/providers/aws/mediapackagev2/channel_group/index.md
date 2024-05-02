---
title: channel_group
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_group
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
Gets an individual <code>channel_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents a channel group that facilitates the grouping of multiple channels.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackagev2.channel_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>channel_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time the channel group was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>&lt;p&gt;Enter any descriptive text that helps you to identify the channel group.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>egress_domain</code></td><td><code>string</code></td><td>&lt;p&gt;The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time the channel group was modified.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
channel_group_name,
created_at,
description,
egress_domain,
modified_at,
tags
FROM aws.mediapackagev2.channel_group
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>channel_group</code> resource, the following permissions are required:

### Read
```json
mediapackagev2:GetChannelGroup
```

### Update
```json
mediapackagev2:TagResource,
mediapackagev2:UntagResource,
mediapackagev2:ListTagsForResource,
mediapackagev2:UpdateChannelGroup
```

### Delete
```json
mediapackagev2:GetChannelGroup,
mediapackagev2:DeleteChannelGroup
```

