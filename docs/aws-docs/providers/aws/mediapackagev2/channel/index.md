---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
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
Gets an individual <code>channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents an entry point into AWS Elemental MediaPackage for an ABR video content stream sent from an upstream encoder such as AWS Elemental MediaLive. The channel continuously analyzes the content that it receives and prepares it to be distributed to consumers via one or more origin endpoints.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediapackagev2.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>channel_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time the channel was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>&lt;p&gt;Enter any descriptive text that helps you to identify the channel.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>ingest_endpoints</code></td><td><code>array</code></td><td>&lt;p&gt;The list of ingest endpoints.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time the channel was modified.&lt;&#x2F;p&gt;</td></tr>
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
channel_name,
created_at,
description,
ingest_endpoints,
modified_at,
tags
FROM aws.mediapackagev2.channel
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>channel</code> resource, the following permissions are required:

### Read
```json
mediapackagev2:GetChannel
```

### Update
```json
mediapackagev2:TagResource,
mediapackagev2:UntagResource,
mediapackagev2:ListTagsForResource,
mediapackagev2:UpdateChannel
```

### Delete
```json
mediapackagev2:GetChannel,
mediapackagev2:DeleteChannel
```

