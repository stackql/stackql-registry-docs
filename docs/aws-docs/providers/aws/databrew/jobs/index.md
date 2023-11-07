---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - databrew
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>jobs</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.jobs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DatasetName</code></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><code>EncryptionKeyArn</code></td><td><code>string</code></td><td>Encryption Key Arn</td></tr>
<tr><td><code>EncryptionMode</code></td><td><code>string</code></td><td>Encryption mode</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Job name</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>Job type</td></tr>
<tr><td><code>LogSubscription</code></td><td><code>string</code></td><td>Log subscription</td></tr>
<tr><td><code>MaxCapacity</code></td><td><code>integer</code></td><td>Max capacity</td></tr>
<tr><td><code>MaxRetries</code></td><td><code>integer</code></td><td>Max retries</td></tr>
<tr><td><code>Outputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DataCatalogOutputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DatabaseOutputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>OutputLocation</code></td><td><code>undefined</code></td><td>Output location</td></tr>
<tr><td><code>ProjectName</code></td><td><code>string</code></td><td>Project name</td></tr>
<tr><td><code>Recipe</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Timeout</code></td><td><code>integer</code></td><td>Timeout</td></tr>
<tr><td><code>JobSample</code></td><td><code>undefined</code></td><td>Job Sample</td></tr>
<tr><td><code>ProfileConfiguration</code></td><td><code>undefined</code></td><td>Profile Job configuration</td></tr>
<tr><td><code>ValidationConfigurations</code></td><td><code>array</code></td><td>Data quality rules configuration</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.databrew.jobs<br/>WHERE region = 'us-east-1'
</pre>
