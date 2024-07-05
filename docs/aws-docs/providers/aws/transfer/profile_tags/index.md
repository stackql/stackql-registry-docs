---
title: profile_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_tags
  - transfer
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

Expands all tag keys and values for <code>profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Profile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.profile_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="as2_id" /></td><td><code>string</code></td><td>AS2 identifier agreed with a trading partner.</td></tr>
<tr><td><CopyableCode code="profile_type" /></td><td><code>string</code></td><td>Enum specifying whether the profile is local or associated with a trading partner.</td></tr>
<tr><td><CopyableCode code="certificate_ids" /></td><td><code>array</code></td><td>List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the profile.</td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td>A unique identifier for the profile</td></tr>
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
Expands tags for all <code>profiles</code> in a region.
```sql
SELECT
region,
as2_id,
profile_type,
certificate_ids,
arn,
profile_id,
tag_key,
tag_value
FROM aws.transfer.profile_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>profile_tags</code> resource, see <a href="/providers/aws/transfer/profiles/#permissions"><code>profiles</code></a>


