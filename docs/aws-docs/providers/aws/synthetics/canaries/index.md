---
title: canaries
hide_title: false
hide_table_of_contents: false
keywords:
  - canaries
  - synthetics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>canaries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.synthetics.canaries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the canary.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Id of the canary</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>State of the canary</td></tr>
<tr><td><code>Code</code></td><td><code>undefined</code></td><td>Provide the canary script source</td></tr>
<tr><td><code>ArtifactS3Location</code></td><td><code>string</code></td><td>Provide the s3 bucket output location for test results</td></tr>
<tr><td><code>ArtifactConfig</code></td><td><code>undefined</code></td><td>Provide artifact configuration</td></tr>
<tr><td><code>Schedule</code></td><td><code>undefined</code></td><td>Frequency to run your canaries</td></tr>
<tr><td><code>ExecutionRoleArn</code></td><td><code>string</code></td><td>Lambda Execution role used to run your canaries</td></tr>
<tr><td><code>RuntimeVersion</code></td><td><code>string</code></td><td>Runtime version of Synthetics Library</td></tr>
<tr><td><code>SuccessRetentionPeriod</code></td><td><code>integer</code></td><td>Retention period of successful canary runs represented in number of days</td></tr>
<tr><td><code>FailureRetentionPeriod</code></td><td><code>integer</code></td><td>Retention period of failed canary runs represented in number of days</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>VPCConfig</code></td><td><code>undefined</code></td><td>Provide VPC Configuration if enabled.</td></tr>
<tr><td><code>RunConfig</code></td><td><code>undefined</code></td><td>Provide canary run configuration</td></tr>
<tr><td><code>StartCanaryAfterCreation</code></td><td><code>boolean</code></td><td>Runs canary if set to True. Default is False</td></tr>
<tr><td><code>VisualReference</code></td><td><code>undefined</code></td><td>Visual reference configuration for visual testing</td></tr>
<tr><td><code>DeleteLambdaResourcesOnCanaryDeletion</code></td><td><code>boolean</code></td><td>Deletes associated lambda resources created by Synthetics if set to True. Default is False</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.synthetics.canaries
WHERE region = 'us-east-1'
</pre>
