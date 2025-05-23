---
title: verified_access_instance_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_instance_tags
  - ec2
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

Expands all tag keys and values for <code>verified_access_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_instance_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_instance_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="verified_access_instance_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><CopyableCode code="verified_access_trust_providers" /></td><td><code>array</code></td><td>AWS Verified Access trust providers.</td></tr>
<tr><td><CopyableCode code="verified_access_trust_provider_ids" /></td><td><code>array</code></td><td>The IDs of the AWS Verified Access trust providers.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Time this Verified Access Instance was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>Time this Verified Access Instance was last updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the AWS Verified Access instance.</td></tr>
<tr><td><CopyableCode code="logging_configurations" /></td><td><code>object</code></td><td>The configuration options for AWS Verified Access instances.</td></tr>
<tr><td><CopyableCode code="fips_enabled" /></td><td><code>boolean</code></td><td>Indicates whether FIPS is enabled</td></tr>
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
Expands tags for all <code>verified_access_instances</code> in a region.
```sql
SELECT
region,
verified_access_instance_id,
verified_access_trust_providers,
verified_access_trust_provider_ids,
creation_time,
last_updated_time,
description,
logging_configurations,
fips_enabled,
tag_key,
tag_value
FROM aws.ec2.verified_access_instance_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>verified_access_instance_tags</code> resource, see <a href="/providers/aws/ec2/verified_access_instances/#permissions"><code>verified_access_instances</code></a>

