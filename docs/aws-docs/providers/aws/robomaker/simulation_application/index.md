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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>simulation_application</code> resource, use <code>simulation_applications</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation_application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema is for testing purpose only.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.simulation_application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the simulation application.</td></tr>
<tr><td><CopyableCode code="current_revision_id" /></td><td><code>string</code></td><td>The current revision id.</td></tr>
<tr><td><CopyableCode code="rendering_engine" /></td><td><code>object</code></td><td>The rendering engine for the simulation application.</td></tr>
<tr><td><CopyableCode code="robot_software_suite" /></td><td><code>object</code></td><td>The robot software suite used by the simulation application.</td></tr>
<tr><td><CopyableCode code="simulation_software_suite" /></td><td><code>object</code></td><td>The simulation software suite used by the simulation application.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>The sources of the simulation application.</td></tr>
<tr><td><CopyableCode code="environment" /></td><td><code>string</code></td><td>The URI of the Docker image for the robot application.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.robomaker.simulation_application
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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

