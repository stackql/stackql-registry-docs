---
title: container_group_definitions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - container_group_definitions_list_only
  - gamelift
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

Lists <code>container_group_definitions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/container_group_definitions/"><code>container_group_definitions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_group_definitions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::ContainerGroupDefinition resource creates an Amazon GameLift container group definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.container_group_definitions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="container_group_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift container group resource and uniquely identifies it across all AWS Regions.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label for the container group definition.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").</td></tr>
<tr><td><CopyableCode code="scheduling_strategy" /></td><td><code>string</code></td><td>Specifies whether the container group includes replica or daemon containers.</td></tr>
<tr><td><CopyableCode code="total_memory_limit" /></td><td><code>integer</code></td><td>The maximum amount of memory (in MiB) to allocate for this container group.</td></tr>
<tr><td><CopyableCode code="total_cpu_limit" /></td><td><code>integer</code></td><td>The maximum number of CPU units reserved for this container group. The value is expressed as an integer amount of CPU units. (1 vCPU is equal to 1024 CPU units.)</td></tr>
<tr><td><CopyableCode code="container_definitions" /></td><td><code>array</code></td><td>A collection of container definitions that define the containers in this group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="operating_system" /></td><td><code>string</code></td><td>The operating system of the container group</td></tr>
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
Lists all <code>container_group_definitions</code> in a region.
```sql
SELECT
region,
name
FROM aws.gamelift.container_group_definitions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>container_group_definitions_list_only</code> resource, see <a href="/providers/aws/gamelift/container_group_definitions/#permissions"><code>container_group_definitions</code></a>


