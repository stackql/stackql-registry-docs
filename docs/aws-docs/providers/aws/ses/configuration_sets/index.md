---
title: configuration_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_sets
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>configuration_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_sets</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.configuration_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
<tr><td><code>TrackingOptions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DeliveryOptions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ReputationOptions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SendingOptions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SuppressionOptions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VdmOptions</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ses.configuration_sets<br/>WHERE region = 'us-east-1'
</pre>
