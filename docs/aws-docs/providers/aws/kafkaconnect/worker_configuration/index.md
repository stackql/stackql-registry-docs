---
title: worker_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - worker_configuration
  - kafkaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>worker_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>worker_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The configuration of the workers, which are the processes that run the connector logic.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kafkaconnect.worker_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the worker configuration.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A summary description of the worker configuration.</td></tr>
<tr><td><code>worker_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom configuration.</td></tr>
<tr><td><code>properties_file_content</code></td><td><code>string</code></td><td>Base64 encoded contents of connect-distributed.properties file.</td></tr>
<tr><td><code>revision</code></td><td><code>integer</code></td><td>The description of a revision of the worker configuration.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
description,
worker_configuration_arn,
properties_file_content,
revision,
tags
FROM aws.kafkaconnect.worker_configuration
WHERE data__Identifier = '<WorkerConfigurationArn>';
```

## Permissions

To operate on the <code>worker_configuration</code> resource, the following permissions are required:

### Read
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:ListTagsForResource
```

### Update
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:ListTagsForResource,
kafkaconnect:TagResource,
kafkaconnect:UntagResource
```

### Delete
```json
kafkaconnect:DescribeWorkerConfiguration,
kafkaconnect:DeleteWorkerConfiguration
```

