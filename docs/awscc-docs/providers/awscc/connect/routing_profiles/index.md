---
title: routing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_profiles
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>routing_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>routing_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.routing_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>routing_profile_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing profile.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
routing_profile_arn
FROM awscc.connect.routing_profiles
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>routing_profiles</code> resource, the following permissions are required:

### Create
```json
connect:CreateRoutingProfile,
connect:TagResource
```

### List
```json
connect:ListRoutingProfiles,
connect:ListRoutingProfileQueues
```

