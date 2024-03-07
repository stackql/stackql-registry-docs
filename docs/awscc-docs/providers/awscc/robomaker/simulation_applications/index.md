---
title: simulation_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation_applications
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>simulation_applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>simulation_applications</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.robomaker.simulation_applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>simulation_applications</code> resource, the following permissions are required:

### Create
```json
robomaker:CreateSimulationApplication,
robomaker:TagResource,
robomaker:UntagResource,
ecr:BatchGetImage,
ecr:GetAuthorizationToken,
ecr:BatchCheckLayerAvailability,
ecr-public:GetAuthorizationToken,
sts:GetServiceBearerToken
```

### List
```json
robomaker:ListSimulationApplications
```


## Example
```sql
SELECT
region,
arn
FROM awscc.robomaker.simulation_applications
WHERE region = 'us-east-1'
```
