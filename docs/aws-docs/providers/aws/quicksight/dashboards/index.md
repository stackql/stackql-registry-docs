---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>dashboards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.quicksight.dashboards</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DashboardId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DashboardPublishOptions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Definition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastPublishedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Parameters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SourceEntity</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ThemeArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Version</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VersionDescription</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.quicksight.dashboards
WHERE region = 'us-east-1'
</pre>
