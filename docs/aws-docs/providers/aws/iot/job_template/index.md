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
Gets an individual <code>job_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iot.job_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>JobArn</code></td><td><code>string</code></td><td>Optional for copying a JobTemplate from a pre-existing Job configuration.</td></tr><tr><td><code>JobTemplateId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the Job Template.</td></tr><tr><td><code>Document</code></td><td><code>string</code></td><td>The job document. Required if you don't specify a value for documentSource.</td></tr><tr><td><code>DocumentSource</code></td><td><code>string</code></td><td>An S3 link to the job document to use in the template. Required if you don't specify a value for document.</td></tr><tr><td><code>TimeoutConfig</code></td><td><code>object</code></td><td>Specifies the amount of time each device has to finish its execution of the job.</td></tr><tr><td><code>JobExecutionsRolloutConfig</code></td><td><code>object</code></td><td>Allows you to create a staged rollout of a job.</td></tr><tr><td><code>AbortConfig</code></td><td><code>object</code></td><td>The criteria that determine when and how a job abort takes place.</td></tr><tr><td><code>PresignedUrlConfig</code></td><td><code>object</code></td><td>Configuration for pre-signed S3 URLs.</td></tr><tr><td><code>JobExecutionsRetryConfig</code></td><td><code>object</code></td><td></td></tr><tr><td><code>MaintenanceWindows</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Metadata that can be used to manage the JobTemplate.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.job_template
WHERE region = 'us-east-1' AND data__Identifier = '<JobTemplateId>'
</pre>
