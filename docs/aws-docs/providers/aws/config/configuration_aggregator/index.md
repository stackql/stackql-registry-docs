---
title: configuration_aggregator
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_aggregator
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration_aggregator</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_aggregator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_aggregator</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.configuration_aggregator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccountAggregationSources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ConfigurationAggregatorName</code></td><td><code>string</code></td><td>The name of the aggregator.</td></tr>
<tr><td><code>ConfigurationAggregatorArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the aggregator.</td></tr>
<tr><td><code>OrganizationAggregationSource</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags for the configuration aggregator.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.config.configuration_aggregator<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ConfigurationAggregatorName&gt;'
</pre>
