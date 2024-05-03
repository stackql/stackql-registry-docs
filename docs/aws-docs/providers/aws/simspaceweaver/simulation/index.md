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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>simulation</code> resource, use <code>simulations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::SimSpaceWeaver::Simulation resource creates an AWS Simulation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.simspaceweaver.simulation" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the simulation.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role ARN.</td></tr>
<tr><td><CopyableCode code="schema_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="describe_payload" /></td><td><code>string</code></td><td>Json object with all simulation details</td></tr>
<tr><td><CopyableCode code="maximum_duration" /></td><td><code>string</code></td><td>The maximum running time of the simulation.</td></tr>
<tr><td><CopyableCode code="snapshot_s3_location" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
role_arn,
schema_s3_location,
describe_payload,
maximum_duration,
snapshot_s3_location
FROM aws.simspaceweaver.simulation
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

