---
title: channel_namespace_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_namespace_tags
  - appsync
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

Expands all tag keys and values for <code>channel_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_namespace_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AppSync ChannelNamespace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.channel_namespace_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>AppSync Api Id that this Channel Namespace belongs to.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Namespace indentifier.</td></tr>
<tr><td><CopyableCode code="subscribe_auth_modes" /></td><td><code>array</code></td><td>List of AuthModes supported for Subscribe operations.</td></tr>
<tr><td><CopyableCode code="publish_auth_modes" /></td><td><code>array</code></td><td>List of AuthModes supported for Publish operations.</td></tr>
<tr><td><CopyableCode code="code_handlers" /></td><td><code>string</code></td><td>String of APPSYNC_JS code to be used by the handlers.</td></tr>
<tr><td><CopyableCode code="code_s3_location" /></td><td><code>string</code></td><td>The Amazon S3 endpoint where the code is located.</td></tr>
<tr><td><CopyableCode code="channel_namespace_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Channel Namespace.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>channel_namespaces</code> in a region.
```sql
SELECT
region,
api_id,
name,
subscribe_auth_modes,
publish_auth_modes,
code_handlers,
code_s3_location,
channel_namespace_arn,
tag_key,
tag_value
FROM aws.appsync.channel_namespace_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>channel_namespace_tags</code> resource, see <a href="/providers/aws/appsync/channel_namespaces/#permissions"><code>channel_namespaces</code></a>

