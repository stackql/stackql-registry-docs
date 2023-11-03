---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.projects</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>ProjectArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ProjectId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ProjectName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ProjectDescription</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The time at which the project was created.</td></tr><tr><td><code>ServiceCatalogProvisioningDetails</code></td><td><code>object</code></td><td>Input ServiceCatalog Provisioning Details</td></tr><tr><td><code>ServiceCatalogProvisionedProductDetails</code></td><td><code>object</code></td><td>Provisioned ServiceCatalog  Details</td></tr><tr><td><code>ProjectStatus</code></td><td><code>string</code></td><td>The status of a project.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.sagemaker.projects
WHERE region = 'us-east-1'
```
