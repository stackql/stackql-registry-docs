---
title: spot_fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_fleet
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
Gets an individual <code>spot_fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spot_fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>spot_fleet</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.spot_fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>spot_fleet_request_config_data</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
spot_fleet_request_config_data
FROM awscc.ec2.spot_fleet
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>spot_fleet</code> resource, the following permissions are required:

### Delete
```json
ec2:DescribeSpotFleetRequests,
ec2:CancelSpotFleetRequests
```

### Read
```json
ec2:DescribeSpotFleetRequests
```

### Update
```json
ec2:ModifySpotFleetRequest,
ec2:DescribeSpotFleetRequests
```

