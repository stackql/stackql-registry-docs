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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>channel</code> resource, use <code>channels</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents an entry point into AWS Elemental MediaPackage for an ABR video content stream sent from an upstream encoder such as AWS Elemental MediaLive. The channel continuously analyzes the content that it receives and prepares it to be distributed to consumers via one or more origin endpoints.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.channel" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>&lt;p&gt;The date and time the channel was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>&lt;p&gt;Enter any descriptive text that helps you to identify the channel.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="ingest_endpoints" /></td><td><code>array</code></td><td>&lt;p&gt;The list of ingest endpoints.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td>&lt;p&gt;The date and time the channel was modified.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
channel_group_name,
channel_name,
created_at,
description,
ingest_endpoints,
modified_at,
tags
FROM aws.mediapackagev2.channel
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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

