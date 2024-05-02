---
title: job_template
hide_title: false
hide_table_of_contents: false
keywords:
  - job_template
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>job_template</code> resource, use <code>job_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.job_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>job_arn</code></td><td><code>string</code></td><td>Optional for copying a JobTemplate from a pre-existing Job configuration.</td></tr>
<tr><td><code>job_template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the Job Template.</td></tr>
<tr><td><code>document</code></td><td><code>string</code></td><td>The job document. Required if you don't specify a value for documentSource.</td></tr>
<tr><td><code>document_source</code></td><td><code>string</code></td><td>An S3 link to the job document to use in the template. Required if you don't specify a value for document.</td></tr>
<tr><td><code>timeout_config</code></td><td><code>object</code></td><td>Specifies the amount of time each device has to finish its execution of the job.</td></tr>
<tr><td><code>job_executions_rollout_config</code></td><td><code>object</code></td><td>Allows you to create a staged rollout of a job.</td></tr>
<tr><td><code>abort_config</code></td><td><code>object</code></td><td>The criteria that determine when and how a job abort takes place.</td></tr>
<tr><td><code>presigned_url_config</code></td><td><code>object</code></td><td>Configuration for pre-signed S3 URLs.</td></tr>
<tr><td><code>job_executions_retry_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>maintenance_windows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>destination_package_versions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata that can be used to manage the JobTemplate.</td></tr>
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
arn,
job_arn,
job_template_id,
description,
document,
document_source,
timeout_config,
job_executions_rollout_config,
abort_config,
presigned_url_config,
job_executions_retry_config,
maintenance_windows,
destination_package_versions,
tags
FROM aws.iot.job_template
WHERE data__Identifier = '<JobTemplateId>';
```

## Permissions

To operate on the <code>job_template</code> resource, the following permissions are required:

### Read
```json
iot:DescribeJobTemplate
```

### Delete
```json
iot:DeleteJobTemplate
```

