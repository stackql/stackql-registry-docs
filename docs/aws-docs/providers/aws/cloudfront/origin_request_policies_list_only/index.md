---
title: origin_request_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_request_policies_list_only
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

Lists <code>origin_request_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/origin_request_policies/"><code>origin_request_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_request_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An origin request policy.<br />When it's attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:<br />+ The request body and the URL path (without the domain name) from the viewer request.<br />+ The headers that CloudFront automatically includes in every origin request, including <code>Host</code>, <code>User-Agent</code>, and <code>X-Amz-Cf-Id</code>.<br />+ All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.<br /><br />CloudFront sends a request when it can't find an object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use <code>CachePolicy</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.origin_request_policies_list_only" /></td></tr>
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
Lists all <code>origin_request_policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.origin_request_policies_list_only
;
```


## Permissions

For permissions required to operate on the <code>origin_request_policies_list_only</code> resource, see <a href="/providers/aws/cloudfront/origin_request_policies/#permissions"><code>origin_request_policies</code></a>

