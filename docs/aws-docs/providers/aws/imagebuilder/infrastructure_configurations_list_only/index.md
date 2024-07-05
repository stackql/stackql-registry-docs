---
title: infrastructure_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_configurations_list_only
  - imagebuilder
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

Lists <code>infrastructure_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/infrastructure_configurations/"><code>infrastructure_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::InfrastructureConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.infrastructure_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="instance_types" /></td><td><code>array</code></td><td>The instance types of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The security group IDs of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="logging" /></td><td><code>object</code></td><td>The logging configuration of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The subnet ID of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="key_pair" /></td><td><code>string</code></td><td>The EC2 key pair of the infrastructure configuration..</td></tr>
<tr><td><CopyableCode code="terminate_instance_on_failure" /></td><td><code>boolean</code></td><td>The terminate instance on failure configuration of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="instance_profile_name" /></td><td><code>string</code></td><td>The instance profile of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="instance_metadata_options" /></td><td><code>object</code></td><td>The instance metadata option settings for the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="sns_topic_arn" /></td><td><code>string</code></td><td>The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>object</code></td><td>The tags attached to the resource created by Image Builder.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
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
Lists all <code>infrastructure_configurations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.imagebuilder.infrastructure_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>infrastructure_configurations_list_only</code> resource, see <a href="/providers/aws/imagebuilder/infrastructure_configurations/#permissions"><code>infrastructure_configurations</code></a>


