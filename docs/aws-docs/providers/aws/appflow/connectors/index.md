---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - appflow
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connectors</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appflow.connectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ConnectorLabel</code></td><td><code>string</code></td><td> The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><code>ConnectorArn</code></td><td><code>string</code></td><td> The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><code>ConnectorProvisioningType</code></td><td><code>string</code></td><td>The provisioning type of the connector. Currently the only supported value is LAMBDA. </td></tr>
<tr><td><code>ConnectorProvisioningConfig</code></td><td><code>object</code></td><td>Contains information about the configuration of the connector being registered.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description about the connector that's being registered.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appflow.connectors<br/>WHERE region = 'us-east-1'
</pre>
