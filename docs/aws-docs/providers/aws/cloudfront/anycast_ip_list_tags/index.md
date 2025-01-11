---
title: anycast_ip_list_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - anycast_ip_list_tags
  - cloudfront
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

Expands all tag keys and values for <code>anycast_ip_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anycast_ip_list_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::CloudFront::AnycastIpList Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.anycast_ip_list_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="anycast_ip_list" /></td><td><code>object</code></td><td>Definition of AWS::CloudFront::AnycastIpList Resource Type</td></tr>
<tr><td><CopyableCode code="e_tag" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>anycast_ip_lists</code> in a region.
```sql
SELECT
region,
anycast_ip_list,
e_tag,
id,
ip_count,
name,
tag_key,
tag_value
FROM aws.cloudfront.anycast_ip_list_tags
;
```


## Permissions

For permissions required to operate on the <code>anycast_ip_list_tags</code> resource, see <a href="/providers/aws/cloudfront/anycast_ip_lists/#permissions"><code>anycast_ip_lists</code></a>

