---
title: branches
hide_title: false
hide_table_of_contents: false
keywords:
  - branches
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>branches</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.amplify.branches</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AppId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BasicAuthConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BranchName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BuildSpec</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EnableAutoBuild</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>EnablePerformanceMode</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>EnablePullRequestPreview</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>EnvironmentVariables</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Framework</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PullRequestEnvironmentName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Stage</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.amplify.branches
WHERE region = 'us-east-1'
</pre>
