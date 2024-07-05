---
title: profile_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_association_tags
  - route53profiles
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

Expands all tag keys and values for <code>profile_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Profiles::ProfileAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53profiles.profile_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The resource that you associated the profile with.</td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td>The ID of the profile that you associated with the resource that is specified by ResourceId.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Primary Identifier for Profile Association</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of an association between a Profile and a VPC.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the profile association.</td></tr>
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
Expands tags for all <code>profile_associations</code> in a region.
```sql
SELECT
region,
resource_id,
profile_id,
id,
name,
arn,
tag_key,
tag_value
FROM aws.route53profiles.profile_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>profile_association_tags</code> resource, see <a href="/providers/aws/route53profiles/profile_associations/#permissions"><code>profile_associations</code></a>


