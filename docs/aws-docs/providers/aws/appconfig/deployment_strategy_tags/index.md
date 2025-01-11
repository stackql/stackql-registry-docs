---
title: deployment_strategy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_strategy_tags
  - appconfig
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

Expands all tag keys and values for <code>deployment_strategies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_strategy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::DeploymentStrategy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.deployment_strategy_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_duration_in_minutes" /></td><td><code>number</code></td><td>Total amount of time for a deployment to last.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the deployment strategy.</td></tr>
<tr><td><CopyableCode code="final_bake_time_in_minutes" /></td><td><code>number</code></td><td>Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see Configuring permissions for rollback based on Amazon CloudWatch alarms in the AWS AppConfig User Guide.</td></tr>
<tr><td><CopyableCode code="growth_factor" /></td><td><code>number</code></td><td>The percentage of targets to receive a deployed configuration during each interval.</td></tr>
<tr><td><CopyableCode code="growth_type" /></td><td><code>string</code></td><td>The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:<br />Linear: For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for Step percentage. For example, a linear deployment that uses a Step percentage of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.<br />Exponential: For this type, AWS AppConfig processes the deployment exponentially using the following formula: G*(2^N). In this formula, G is the growth factor specified by the user and N is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:<br />2*(2^0)<br />2*(2^1)<br />2*(2^2)<br />Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the deployment strategy.</td></tr>
<tr><td><CopyableCode code="replicate_to" /></td><td><code>string</code></td><td>Save the deployment strategy to a Systems Manager (SSM) document.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The deployment strategy ID.</td></tr>
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
Expands tags for all <code>deployment_strategies</code> in a region.
```sql
SELECT
region,
deployment_duration_in_minutes,
description,
final_bake_time_in_minutes,
growth_factor,
growth_type,
name,
replicate_to,
id,
tag_key,
tag_value
FROM aws.appconfig.deployment_strategy_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>deployment_strategy_tags</code> resource, see <a href="/providers/aws/appconfig/deployment_strategies/#permissions"><code>deployment_strategies</code></a>

