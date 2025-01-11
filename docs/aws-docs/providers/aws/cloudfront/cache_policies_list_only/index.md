---
title: cache_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_policies_list_only
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

Lists <code>cache_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cache_policies/"><code>cache_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cache_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A cache policy.<br />When it's attached to a cache behavior, the cache policy determines the following:<br />+ The values that CloudFront includes in the cache key. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.<br />+ The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.<br /><br />The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can't find a valid object in its cache that matches the request's cache key. If you want to send values to the origin but *not* include them in the cache key, use <code>OriginRequestPolicy</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.cache_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>cache_policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.cache_policies_list_only
;
```


## Permissions

For permissions required to operate on the <code>cache_policies_list_only</code> resource, see <a href="/providers/aws/cloudfront/cache_policies/#permissions"><code>cache_policies</code></a>

