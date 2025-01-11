---
title: source_location_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - source_location_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>source_locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_location_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::SourceLocation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.source_location_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_configuration" /></td><td><code>object</code></td><td><p>Access configuration parameters.</p></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the source location.</p></td></tr>
<tr><td><CopyableCode code="default_segment_delivery_configuration" /></td><td><code>object</code></td><td><p>The optional configuration for a server that serves segments. Use this if you want the segment delivery server to be different from the source location server. For example, you can configure your source location server to be an origination server, such as MediaPackage, and the segment delivery server to be a content delivery network (CDN), such as CloudFront. If you don't specify a segment delivery server, then the source location server is used.</p></td></tr>
<tr><td><CopyableCode code="http_configuration" /></td><td><code>object</code></td><td><p>The HTTP configuration for the source location.</p></td></tr>
<tr><td><CopyableCode code="segment_delivery_configurations" /></td><td><code>array</code></td><td><p>A list of the segment delivery configurations associated with this resource.</p></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>source_locations</code> in a region.
```sql
SELECT
region,
access_configuration,
arn,
default_segment_delivery_configuration,
http_configuration,
segment_delivery_configurations,
source_location_name,
tag_key,
tag_value
FROM aws.mediatailor.source_location_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>source_location_tags</code> resource, see <a href="/providers/aws/mediatailor/source_locations/#permissions"><code>source_locations</code></a>

