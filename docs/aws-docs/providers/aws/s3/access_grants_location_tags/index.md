---
title: access_grants_location_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_location_tags
  - s3
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

Expands all tag keys and values for <code>access_grants_locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_location_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrantsLocation resource is an Amazon S3 resource type hosted in an access grants instance which can be the target of S3 access grants.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants_location_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_grants_location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants location.</td></tr>
<tr><td><CopyableCode code="access_grants_location_id" /></td><td><code>string</code></td><td>The unique identifier for the specified Access Grants location.</td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the access grant location's associated IAM role.</td></tr>
<tr><td><CopyableCode code="location_scope" /></td><td><code>string</code></td><td>Descriptor for where the location actually points</td></tr>
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
Expands tags for all <code>access_grants_locations</code> in a region.
```sql
SELECT
region,
access_grants_location_arn,
access_grants_location_id,
iam_role_arn,
location_scope,
tag_key,
tag_value
FROM aws.s3.access_grants_location_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>access_grants_location_tags</code> resource, see <a href="/providers/aws/s3/access_grants_locations/#permissions"><code>access_grants_locations</code></a>

