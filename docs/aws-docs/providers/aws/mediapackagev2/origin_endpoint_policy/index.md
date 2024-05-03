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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>origin_endpoint_policy</code> resource, use <code>origin_endpoint_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents a resource policy that allows or denies access to an origin endpoint.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoint_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="origin_endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
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
channel_group_name,
channel_name,
origin_endpoint_name,
policy
FROM aws.mediapackagev2.origin_endpoint_policy
WHERE data__Identifier = '<ChannelGroupName>|<ChannelName>|<OriginEndpointName>';
```

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
