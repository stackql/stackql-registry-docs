---
title: channel_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_policy
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
Gets an individual <code>channel_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::ChannelPolicy Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediatailor.channel_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>&lt;p&gt;The IAM policy for the channel. IAM policies are used to control access to your channel.&lt;&#x2F;p&gt;</td></tr>
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
channel_name,
policy
FROM aws.mediatailor.channel_policy
WHERE data__Identifier = '<ChannelName>';
```

## Permissions

To operate on the <code>channel_policy</code> resource, the following permissions are required:

### Read
```json
mediatailor:GetChannelPolicy
```

### Update
```json
mediatailor:PutChannelPolicy,
mediatailor:GetChannelPolicy
```

### Delete
```json
mediatailor:DeleteChannelPolicy,
mediatailor:GetChannelPolicy
```

