---
title: container_group_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - container_group_definition_tags
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

Expands all tag keys and values for <code>container_group_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_group_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::ContainerGroupDefinition resource creates an Amazon GameLift container group definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.container_group_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="container_group_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift container group resource and uniquely identifies it across all AWS Regions.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").</td></tr>
<tr><td><CopyableCode code="operating_system" /></td><td><code>string</code></td><td>The operating system of the container group</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label for the container group definition.</td></tr>
<tr><td><CopyableCode code="container_group_type" /></td><td><code>string</code></td><td>The scope of the container group</td></tr>
<tr><td><CopyableCode code="total_memory_limit_mebibytes" /></td><td><code>integer</code></td><td>The total memory limit of container groups following this definition in MiB</td></tr>
<tr><td><CopyableCode code="total_vcpu_limit" /></td><td><code>number</code></td><td>The total amount of virtual CPUs on the container group definition</td></tr>
<tr><td><CopyableCode code="game_server_container_definition" /></td><td><code>object</code></td><td>Specifies the information required to run game servers with this container group</td></tr>
<tr><td><CopyableCode code="support_container_definitions" /></td><td><code>array</code></td><td>A collection of support container definitions that define the containers in this group.</td></tr>
<tr><td><CopyableCode code="version_number" /></td><td><code>integer</code></td><td>The version of this ContainerGroupDefinition</td></tr>
<tr><td><CopyableCode code="source_version_number" /></td><td><code>integer</code></td><td>A specific ContainerGroupDefinition version to be updated</td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td>The description of this version</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A string indicating ContainerGroupDefinition status.</td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td>A string indicating the reason for ContainerGroupDefinition status.</td></tr>
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
Expands tags for all <code>container_group_definitions</code> in a region.
```sql
SELECT
region,
container_group_definition_arn,
creation_time,
operating_system,
name,
container_group_type,
total_memory_limit_mebibytes,
total_vcpu_limit,
game_server_container_definition,
support_container_definitions,
version_number,
source_version_number,
version_description,
status,
status_reason,
tag_key,
tag_value
FROM aws.gamelift.container_group_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>container_group_definition_tags</code> resource, see <a href="/providers/aws/gamelift/container_group_definitions/#permissions"><code>container_group_definitions</code></a>

