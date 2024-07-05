---
title: ec2fleets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - ec2fleets_list_only
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

Lists <code>ec2fleets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/ec2fleets/"><code>ec2fleets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ec2fleets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::EC2Fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ec2fleets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_capacity_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="on_demand_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="excess_capacity_termination_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="spot_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="valid_from" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="replace_unhealthy_instances" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_template_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="terminate_instances_with_expiration" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="valid_until" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="context" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>ec2fleets</code> in a region.
```sql
SELECT
region,
fleet_id
FROM aws.ec2.ec2fleets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ec2fleets_list_only</code> resource, see <a href="/providers/aws/ec2/ec2fleets/#permissions"><code>ec2fleets</code></a>


