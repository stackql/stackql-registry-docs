---
title: data_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_integrations
  - appintegrations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>data_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_integrations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appintegrations.data_integrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The data integration description.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The unique identifer of the data integration.</td></tr>
<tr><td><code>DataIntegrationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the data integration.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the data integration.</td></tr>
<tr><td><code>KmsKey</code></td><td><code>string</code></td><td>The KMS key of the data integration.</td></tr>
<tr><td><code>ScheduleConfig</code></td><td><code>object</code></td><td>The name of the data and how often it should be pulled from the source.</td></tr>
<tr><td><code>SourceURI</code></td><td><code>string</code></td><td>The URI of the data source.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the data integration.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appintegrations.data_integrations<br/>WHERE region = 'us-east-1'
</pre>
