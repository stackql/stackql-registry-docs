---
title: cloud_formation_products
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_formation_products
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>cloud_formation_products</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_formation_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.cloud_formation_products</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Owner</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProductName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SupportEmail</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProductType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProvisioningArtifactNames</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReplaceProvisioningArtifacts</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>SupportDescription</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Distributor</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProvisioningArtifactIds</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AcceptLanguage</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SupportUrl</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SourceConnection</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ProvisioningArtifactParameters</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.servicecatalog.cloud_formation_products
WHERE region = 'us-east-1'
</pre>
