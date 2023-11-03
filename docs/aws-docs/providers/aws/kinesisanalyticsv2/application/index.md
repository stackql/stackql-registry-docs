---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - kinesisanalyticsv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.kinesisanalyticsv2.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ApplicationConfiguration</code></td><td><code>undefined</code></td><td>Use this parameter to configure the application.</td></tr><tr><td><code>ApplicationDescription</code></td><td><code>string</code></td><td>The description of the application.</td></tr><tr><td><code>ApplicationMode</code></td><td><code>string</code></td><td>To create a Kinesis Data Analytics Studio notebook, you must set the mode to `INTERACTIVE`. However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.</td></tr><tr><td><code>ApplicationName</code></td><td><code>string</code></td><td>The name of the application.</td></tr><tr><td><code>RuntimeEnvironment</code></td><td><code>string</code></td><td>The runtime environment for the application.</td></tr><tr><td><code>ServiceExecutionRole</code></td><td><code>undefined</code></td><td>Specifies the IAM role that the application uses to access external resources.</td></tr><tr><td><code>RunConfiguration</code></td><td><code>undefined</code></td><td>Specifies run configuration (start parameters) of a Kinesis Data Analytics application. Evaluated on update for RUNNING applications an only.</td></tr><tr><td><code>ApplicationMaintenanceConfiguration</code></td><td><code>undefined</code></td><td>Used to configure start of maintenance window.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.kinesisanalyticsv2.application
WHERE region = 'us-east-1' AND data__Identifier = '{ApplicationName}'
</pre>
