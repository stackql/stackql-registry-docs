---
title: task_definitions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definitions_list_only
  - ecs
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

Lists <code>task_definitions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/task_definitions/"><code>task_definitions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a new task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information about task definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.<br />You can specify a role for your task with the <code>taskRoleArn</code> parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see &#91;IAM Roles for Tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.<br />You can specify a Docker networking mode for the containers in your task definition with the <code>networkMode</code> parameter. If you specify the <code>awsvpc</code> network mode, the task is allocated an elastic network interface, and you must specify a &#91;NetworkConfiguration&#93;(https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html) when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.<br />In the following example or examples, the Authorization header contents (<code>AUTHPARAMS</code>) must be replaced with an AWS Signature Version 4 signature. For more information, see &#91;Signature Version 4 Signing Process&#93;(https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *General Reference*.<br />You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the &#91;&#93;(https://docs.aws.amazon.com/cli/) or one of the &#91;SDKs&#93;(https://docs.aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_definitions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="task_definition_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>task_definitions</code> in a region.
```sql
SELECT
region,
task_definition_arn
FROM aws.ecs.task_definitions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>task_definitions_list_only</code> resource, see <a href="/providers/aws/ecs/task_definitions/#permissions"><code>task_definitions</code></a>

