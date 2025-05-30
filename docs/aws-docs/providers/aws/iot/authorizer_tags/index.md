---
title: authorizer_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer_tags
  - iot
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

Expands all tag keys and values for <code>authorizers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an authorizer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.authorizer_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="authorizer_function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signing_disabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="token_key_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="token_signing_public_keys" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_caching_for_http" /></td><td><code>boolean</code></td><td></td></tr>
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
Expands tags for all <code>authorizers</code> in a region.
```sql
SELECT
region,
authorizer_function_arn,
arn,
authorizer_name,
signing_disabled,
status,
token_key_name,
token_signing_public_keys,
enable_caching_for_http,
tag_key,
tag_value
FROM aws.iot.authorizer_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>authorizer_tags</code> resource, see <a href="/providers/aws/iot/authorizers/#permissions"><code>authorizers</code></a>

