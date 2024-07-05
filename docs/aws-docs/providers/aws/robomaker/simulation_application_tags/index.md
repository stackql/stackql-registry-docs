---
title: simulation_application_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation_application_tags
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

Expands all tag keys and values for <code>simulation_applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation_application_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema is for testing purpose only.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.simulation_application_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the simulation application.</td></tr>
<tr><td><CopyableCode code="current_revision_id" /></td><td><code>string</code></td><td>The current revision id.</td></tr>
<tr><td><CopyableCode code="rendering_engine" /></td><td><code>object</code></td><td>The rendering engine for the simulation application.</td></tr>
<tr><td><CopyableCode code="robot_software_suite" /></td><td><code>object</code></td><td>The robot software suite used by the simulation application.</td></tr>
<tr><td><CopyableCode code="simulation_software_suite" /></td><td><code>object</code></td><td>The simulation software suite used by the simulation application.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>The sources of the simulation application.</td></tr>
<tr><td><CopyableCode code="environment" /></td><td><code>string</code></td><td>The URI of the Docker image for the robot application.</td></tr>
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
Expands tags for all <code>simulation_applications</code> in a region.
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
tag_key,
tag_value
FROM aws.robomaker.simulation_application_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>simulation_application_tags</code> resource, see <a href="/providers/aws/robomaker/simulation_applications/#permissions"><code>simulation_applications</code></a>


