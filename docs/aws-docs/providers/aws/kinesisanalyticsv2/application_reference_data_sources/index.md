---
title: application_reference_data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - application_reference_data_sources
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
Retrieves a list of <code>application_reference_data_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_reference_data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application_reference_data_sources</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesisanalyticsv2.application_reference_data_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApplicationName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ReferenceDataSource</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.kinesisanalyticsv2.application_reference_data_sources<br/>WHERE region = 'us-east-1'
</pre>
