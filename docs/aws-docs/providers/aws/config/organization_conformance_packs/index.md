---
title: organization_conformance_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_conformance_packs
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
Retrieves a list of <code>organization_conformance_packs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_conformance_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organization_conformance_packs</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.organization_conformance_packs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OrganizationConformancePackName</code></td><td><code>string</code></td><td>The name of the organization conformance pack.</td></tr>
<tr><td><code>TemplateS3Uri</code></td><td><code>string</code></td><td>Location of file containing the template body.</td></tr>
<tr><td><code>TemplateBody</code></td><td><code>string</code></td><td>A string containing full conformance pack template body.</td></tr>
<tr><td><code>DeliveryS3Bucket</code></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><code>DeliveryS3KeyPrefix</code></td><td><code>string</code></td><td>The prefix for the delivery S3 bucket.</td></tr>
<tr><td><code>ConformancePackInputParameters</code></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>
<tr><td><code>ExcludedAccounts</code></td><td><code>array</code></td><td>A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.config.organization_conformance_packs<br/>WHERE region = 'us-east-1'
</pre>
