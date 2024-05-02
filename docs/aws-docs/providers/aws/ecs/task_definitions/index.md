---
title: task_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definitions
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
Used to retrieve a list of <code>task_definitions</code> in a region or create a <code>task_definitions</code> resource, use <code>task_definition</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a new task definition from the supplied ``family`` and ``containerDefinitions``. Optionally, you can add data volumes to your containers with the ``volumes`` parameter. For more information about task definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; You can specify a role for your task with the ``taskRoleArn`` parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see &#91;IAM Roles for Tasks&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; You can specify a Docker networking mode for the containers in your task definition with the ``networkMode`` parameter. The available network modes correspond to those described in &#91;Network settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;reference&#x2F;run&#x2F;#&#x2F;network-settings) in the Docker run reference. If you specify the ``awsvpc`` network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt;  In the following example or examples, the Authorization header contents (``AUTHPARAMS``) must be replaced with an AWS Signature Version 4 signature. For more information, see &#91;Signature Version 4 Signing Process&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;signature-version-4.html) in the *General Reference*.&lt;br&#x2F;&gt; You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;cli&#x2F;) or one of the &#91;SDKs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;tools&#x2F;) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecs.task_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>task_definition_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
task_definition_arn
FROM aws.ecs.task_definitions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>task_definitions</code> resource, the following permissions are required:

### Create
```json
ecs:RegisterTaskDefinition,
ecs:DescribeTaskDefinition,
ecs:TagResource,
iam:GetRole,
iam:PassRole
```

### List
```json
ecs:ListTaskDefinitions,
ecs:DescribeTaskDefinition
```

