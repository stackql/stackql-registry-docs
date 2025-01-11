---
title: cloud_front_origin_access_identities_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_front_origin_access_identities_list_only
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

Lists <code>cloud_front_origin_access_identities</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cloud_front_origin_access_identities/"><code>cloud_front_origin_access_identities</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_front_origin_access_identities_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The request to create a new origin access identity (OAI). An origin access identity is a special CloudFront user that you can associate with Amazon S3 origins, so that you can secure all or just some of your Amazon S3 content. For more information, see &#91;Restricting Access to Amazon S3 Content by Using an Origin Access Identity&#93;(https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.cloud_front_origin_access_identities_list_only" /></td></tr>
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
Lists all <code>cloud_front_origin_access_identities</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.cloud_front_origin_access_identities_list_only
;
```


## Permissions

For permissions required to operate on the <code>cloud_front_origin_access_identities_list_only</code> resource, see <a href="/providers/aws/cloudfront/cloud_front_origin_access_identities/#permissions"><code>cloud_front_origin_access_identities</code></a>

