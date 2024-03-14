---
title: simulation
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation
  - simspaceweaver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>simulation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>simulation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.simspaceweaver.simulation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the simulation.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Role ARN.</td></tr>
<tr><td><code>schema_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>describe_payload</code></td><td><code>string</code></td><td>Json object with all simulation details</td></tr>
<tr><td><code>maximum_duration</code></td><td><code>string</code></td><td>The maximum running time of the simulation.</td></tr>
<tr><td><code>snapshot_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
role_arn,
schema_s3_location,
describe_payload,
maximum_duration,
snapshot_s3_location
FROM awscc.simspaceweaver.simulation
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>simulation</code> resource, the following permissions are required:

### Read
```json
simspaceweaver:DescribeSimulation
```

### Update
```json
simspaceweaver:StartSimulation,
simspaceweaver:StopSimulation,
simspaceweaver:DeleteSimulation,
simspaceweaver:DescribeSimulation
```

### Delete
```json
simspaceweaver:StopSimulation,
simspaceweaver:DeleteSimulation,
simspaceweaver:DescribeSimulation
```

