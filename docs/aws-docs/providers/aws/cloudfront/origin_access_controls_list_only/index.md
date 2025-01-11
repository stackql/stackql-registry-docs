---
title: origin_access_controls_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_access_controls_list_only
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

Lists <code>origin_access_controls</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/origin_access_controls/"><code>origin_access_controls</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_access_controls_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.<br />This makes it possible to block public access to the origin, allowing viewers (users) to access the origin's content only through CloudFront.<br />For more information about using a CloudFront origin access control, see &#91;Restricting access to an origin&#93;(https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html) in the *Amazon CloudFront Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.origin_access_controls_list_only" /></td></tr>
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
Lists all <code>origin_access_controls</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.origin_access_controls_list_only
;
```


## Permissions

For permissions required to operate on the <code>origin_access_controls_list_only</code> resource, see <a href="/providers/aws/cloudfront/origin_access_controls/#permissions"><code>origin_access_controls</code></a>

