---
title: capacity_reservation_fleets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_fleets_list_only
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

Lists <code>capacity_reservation_fleets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/capacity_reservation_fleets/"><code>capacity_reservation_fleets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::CapacityReservationFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.capacity_reservation_fleets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allocation_strategy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="total_target_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="end_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_match_criteria" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity_reservation_fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tenancy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_end_date" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="no_remove_end_date" /></td><td><code>boolean</code></td><td></td></tr>
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
Lists all <code>capacity_reservation_fleets</code> in a region.
```sql
SELECT
region,
capacity_reservation_fleet_id
FROM aws.ec2.capacity_reservation_fleets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>capacity_reservation_fleets_list_only</code> resource, see <a href="/providers/aws/ec2/capacity_reservation_fleets/#permissions"><code>capacity_reservation_fleets</code></a>


