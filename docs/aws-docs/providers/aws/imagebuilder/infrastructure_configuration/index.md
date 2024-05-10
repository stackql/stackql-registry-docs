---
title: infrastructure_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_configuration
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


Gets or updates an individual <code>infrastructure_configuration</code> resource, use <code>infrastructure_configurations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::InfrastructureConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.infrastructure_configuration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
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
description,
instance_types,
security_group_ids,
logging,
subnet_id,
key_pair,
terminate_instance_on_failure,
instance_profile_name,
instance_metadata_options,
sns_topic_arn,
resource_tags,
tags
FROM aws.imagebuilder.infrastructure_configuration
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>infrastructure_configuration</code> resource, the following permissions are required:

### Update
```json
iam:PassRole,
sns:Publish,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:UpdateInfrastructureConfiguration
```

### Read
```json
imagebuilder:GetInfrastructureConfiguration
```

