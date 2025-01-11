---
title: fleet_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_tags
  - codebuild
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

Expands all tag keys and values for <code>fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeBuild::Fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codebuild.fleet_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="base_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="overflow_behavior" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_service_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_proxy_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scaling_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>fleets</code> in a region.
```sql
SELECT
region,
name,
base_capacity,
environment_type,
compute_type,
overflow_behavior,
fleet_service_role,
fleet_vpc_config,
fleet_proxy_configuration,
arn,
image_id,
scaling_configuration,
compute_configuration,
tag_key,
tag_value
FROM aws.codebuild.fleet_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>fleet_tags</code> resource, see <a href="/providers/aws/codebuild/fleets/#permissions"><code>fleets</code></a>

