---
title: bucket_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_tags
  - lightsail
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

Expands all tag keys and values for <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Bucket</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.bucket_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>The name for the bucket.</td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The ID of the bundle to use for the bucket.</td></tr>
<tr><td><CopyableCode code="bucket_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="object_versioning" /></td><td><code>boolean</code></td><td>Specifies whether to enable or disable versioning of objects in the bucket.</td></tr>
<tr><td><CopyableCode code="access_rules" /></td><td><code>object</code></td><td>An object that sets the public accessibility of objects in the specified bucket.</td></tr>
<tr><td><CopyableCode code="resources_receiving_access" /></td><td><code>array</code></td><td>The names of the Lightsail resources for which to set bucket access.</td></tr>
<tr><td><CopyableCode code="read_only_access_accounts" /></td><td><code>array</code></td><td>An array of strings to specify the AWS account IDs that can access the bucket.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The URL of the bucket.</td></tr>
<tr><td><CopyableCode code="able_to_update_bundle" /></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.</td></tr>
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
Expands tags for all <code>buckets</code> in a region.
```sql
SELECT
region,
bucket_name,
bundle_id,
bucket_arn,
object_versioning,
access_rules,
resources_receiving_access,
read_only_access_accounts,
url,
able_to_update_bundle,
tag_key,
tag_value
FROM aws.lightsail.bucket_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>bucket_tags</code> resource, see <a href="/providers/aws/lightsail/buckets/#permissions"><code>buckets</code></a>


