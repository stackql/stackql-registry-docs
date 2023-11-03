---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>containers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.containers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ServiceName</code></td><td><code>string</code></td><td>The name for the container service.</td></tr><tr><td><code>Power</code></td><td><code>string</code></td><td>The power specification for the container service.</td></tr><tr><td><code>ContainerArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Scale</code></td><td><code>integer</code></td><td>The scale specification for the container service.</td></tr><tr><td><code>PublicDomainNames</code></td><td><code>array</code></td><td>The public domain names to use with the container service, such as example.com and www.example.com.</td></tr><tr><td><code>ContainerServiceDeployment</code></td><td><code>undefined</code></td><td>Describes a container deployment configuration of an Amazon Lightsail container service.</td></tr><tr><td><code>IsDisabled</code></td><td><code>boolean</code></td><td>A Boolean value to indicate whether the container service is disabled.</td></tr><tr><td><code>Url</code></td><td><code>string</code></td><td>The publicly accessible URL of the container service.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lightsail.containers
WHERE region = 'us-east-1'
</pre>
