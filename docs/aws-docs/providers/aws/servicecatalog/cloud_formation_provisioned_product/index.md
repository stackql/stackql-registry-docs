---
title: cloud_formation_provisioned_product
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_formation_provisioned_product
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
Gets an individual <code>cloud_formation_provisioned_product</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_formation_provisioned_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cloud_formation_provisioned_product</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.cloud_formation_provisioned_product</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AcceptLanguage</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NotificationArns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>PathId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PathName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProductId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProductName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProvisionedProductName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProvisioningArtifactId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProvisioningArtifactName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProvisioningParameters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ProvisioningPreferences</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ProvisionedProductId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RecordId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CloudformationStackArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Outputs</code></td><td><code>object</code></td><td>List of key-value pair outputs.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.servicecatalog.cloud_formation_provisioned_product
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ProvisionedProductId&gt;'
</pre>
