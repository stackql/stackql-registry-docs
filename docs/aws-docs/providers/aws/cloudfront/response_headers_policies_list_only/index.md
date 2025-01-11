---
title: response_headers_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - response_headers_policies_list_only
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

Lists <code>response_headers_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/response_headers_policies/"><code>response_headers_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_headers_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A response headers policy.<br />A response headers policy contains information about a set of HTTP response headers.<br />After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it's attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.<br />For more information, see &#91;Adding or removing HTTP headers in CloudFront responses&#93;(https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html) in the *Amazon CloudFront Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.response_headers_policies_list_only" /></td></tr>
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
Lists all <code>response_headers_policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.response_headers_policies_list_only
;
```


## Permissions

For permissions required to operate on the <code>response_headers_policies_list_only</code> resource, see <a href="/providers/aws/cloudfront/response_headers_policies/#permissions"><code>response_headers_policies</code></a>

