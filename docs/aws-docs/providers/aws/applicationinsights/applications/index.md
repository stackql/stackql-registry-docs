---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - applicationinsights
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.applicationinsights.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceGroupName</code></td><td><code>string</code></td><td>The name of the resource group.</td></tr>
<tr><td><code>ApplicationARN</code></td><td><code>string</code></td><td>The ARN of the ApplicationInsights application.</td></tr>
<tr><td><code>CWEMonitorEnabled</code></td><td><code>boolean</code></td><td>Indicates whether Application Insights can listen to CloudWatch events for the application resources.</td></tr>
<tr><td><code>OpsCenterEnabled</code></td><td><code>boolean</code></td><td>When set to true, creates opsItems for any problems detected on an application.</td></tr>
<tr><td><code>OpsItemSNSTopicArn</code></td><td><code>string</code></td><td>The SNS topic provided to Application Insights that is associated to the created opsItem.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags of Application Insights application.</td></tr>
<tr><td><code>CustomComponents</code></td><td><code>array</code></td><td>The custom grouped components.</td></tr>
<tr><td><code>LogPatternSets</code></td><td><code>array</code></td><td>The log pattern sets.</td></tr>
<tr><td><code>AutoConfigurationEnabled</code></td><td><code>boolean</code></td><td>If set to true, application will be configured with recommended monitoring configuration.</td></tr>
<tr><td><code>ComponentMonitoringSettings</code></td><td><code>array</code></td><td>The monitoring settings of the components.</td></tr>
<tr><td><code>GroupingType</code></td><td><code>string</code></td><td>The grouping type of the application</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.applicationinsights.applications
WHERE region = 'us-east-1'
</pre>
