---
title: simulation_application
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation_application
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
Gets an individual <code>simulation_application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation_application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>simulation_application</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.robomaker.simulation_application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the simulation application.</td></tr>
<tr><td><code>current_revision_id</code></td><td><code>string</code></td><td>The current revision id.</td></tr>
<tr><td><code>rendering_engine</code></td><td><code>object</code></td><td>The rendering engine for the simulation application.</td></tr>
<tr><td><code>robot_software_suite</code></td><td><code>object</code></td><td>The robot software suite used by the simulation application.</td></tr>
<tr><td><code>simulation_software_suite</code></td><td><code>object</code></td><td>The simulation software suite used by the simulation application.</td></tr>
<tr><td><code>sources</code></td><td><code>array</code></td><td>The sources of the simulation application.</td></tr>
<tr><td><code>environment</code></td><td><code>string</code></td><td>The URI of the Docker image for the robot application.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
current_revision_id,
rendering_engine,
robot_software_suite,
simulation_software_suite,
sources,
environment,
tags
FROM awscc.robomaker.simulation_application
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>simulation_application</code> resource, the following permissions are required:

### Read
```json
robomaker:DescribeSimulationApplication
```

### Update
```json
robomaker:TagResource,
robomaker:UntagResource,
robomaker:UpdateSimulationApplication,
ecr:BatchGetImage,
ecr:GetAuthorizationToken,
ecr:BatchCheckLayerAvailability,
ecr-public:GetAuthorizationToken
```

### Delete
```json
robomaker:DescribeSimulationApplication,
robomaker:DeleteSimulationApplication
```

