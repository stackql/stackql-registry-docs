---
title: playback_key_pair_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_key_pair_tags
  - ivs
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

Expands all tag keys and values for <code>playback_key_pairs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_key_pair_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::PlaybackKeyPair</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.playback_key_pair_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>An arbitrary string (a nickname) assigned to a playback key pair that helps the customer identify that resource. The value does not need to be unique.</td></tr>
<tr><td><CopyableCode code="public_key_material" /></td><td><code>string</code></td><td>The public portion of a customer-generated key pair.</td></tr>
<tr><td><CopyableCode code="fingerprint" /></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
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
Expands tags for all <code>playback_key_pairs</code> in a region.
```sql
SELECT
region,
name,
public_key_material,
fingerprint,
arn,
tag_key,
tag_value
FROM aws.ivs.playback_key_pair_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>playback_key_pair_tags</code> resource, see <a href="/providers/aws/ivs/playback_key_pairs/#permissions"><code>playback_key_pairs</code></a>


