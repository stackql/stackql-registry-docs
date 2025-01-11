---
title: access_grant_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grant_tags
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

Expands all tag keys and values for <code>access_grants</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grant_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrant resource is an Amazon S3 resource type representing permissions to a specific S3 bucket or prefix hosted in an S3 Access Grants instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grant_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_grant_id" /></td><td><code>string</code></td><td>The ID assigned to this access grant.</td></tr>
<tr><td><CopyableCode code="access_grants_location_id" /></td><td><code>string</code></td><td>The custom S3 location to be accessed by the grantee</td></tr>
<tr><td><CopyableCode code="permission" /></td><td><code>string</code></td><td>The level of access to be afforded to the grantee</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application grantees will use to access the location</td></tr>
<tr><td><CopyableCode code="s3_prefix_type" /></td><td><code>string</code></td><td>The type of S3SubPrefix.</td></tr>
<tr><td><CopyableCode code="grant_scope" /></td><td><code>string</code></td><td>The S3 path of the data to which you are granting access. It is a combination of the S3 path of the registered location and the subprefix.</td></tr>
<tr><td><CopyableCode code="access_grant_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified access grant.</td></tr>
<tr><td><CopyableCode code="grantee" /></td><td><code>object</code></td><td>The principal who will be granted permission to access S3.</td></tr>
<tr><td><CopyableCode code="access_grants_location_configuration" /></td><td><code>object</code></td><td>The configuration options of the grant location, which is the S3 path to the data to which you are granting access.</td></tr>
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
Expands tags for all <code>access_grants</code> in a region.
```sql
SELECT
region,
access_grant_id,
access_grants_location_id,
permission,
application_arn,
s3_prefix_type,
grant_scope,
access_grant_arn,
grantee,
access_grants_location_configuration,
tag_key,
tag_value
FROM aws.s3.access_grant_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>access_grant_tags</code> resource, see <a href="/providers/aws/s3/access_grants/#permissions"><code>access_grants</code></a>

