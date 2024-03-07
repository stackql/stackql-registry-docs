---
title: link
hide_title: false
hide_table_of_contents: false
keywords:
  - link
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>link</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>link_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the link.</td></tr>
<tr><td><code>link_id</code></td><td><code>string</code></td><td>The ID of the link.</td></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>site_id</code></td><td><code>string</code></td><td>The ID of the site</td></tr>
<tr><td><code>bandwidth</code></td><td><code>object</code></td><td>The Bandwidth for the link.</td></tr>
<tr><td><code>provider</code></td><td><code>string</code></td><td>The provider of the link.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the link.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the link.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the link.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the link.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
link_arn,
link_id,
global_network_id,
site_id,
bandwidth,
provider,
description,
tags,
type,
created_at,
state
FROM awscc.networkmanager.link
WHERE region = 'us-east-1'
AND data__Identifier = '{GlobalNetworkId}';
AND data__Identifier = '{LinkId}';
```

## Permissions

To operate on the <code>link</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetLinks
```

### Update
```json
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:GetLinks,
networkmanager:UntagResource,
networkmanager:UpdateLink
```

### Delete
```json
networkmanager:GetLinks,
networkmanager:DeleteLink
```

