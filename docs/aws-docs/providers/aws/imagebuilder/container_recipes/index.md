---
title: container_recipes
hide_title: false
hide_table_of_contents: false
keywords:
  - container_recipes
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>container_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>container_recipes</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.container_recipes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the container recipe.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the container recipe.</td></tr>
<tr><td><code>Version</code></td><td><code>string</code></td><td>The semantic version of the container recipe (&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;).</td></tr>
<tr><td><code>Components</code></td><td><code>array</code></td><td>Components for build and test that are included in the container recipe.</td></tr>
<tr><td><code>InstanceConfiguration</code></td><td><code>object</code></td><td>A group of options that can be used to configure an instance for building and testing container images.</td></tr>
<tr><td><code>DockerfileTemplateData</code></td><td><code>string</code></td><td>Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.</td></tr>
<tr><td><code>DockerfileTemplateUri</code></td><td><code>string</code></td><td>The S3 URI for the Dockerfile that will be used to build your container image.</td></tr>
<tr><td><code>PlatformOverride</code></td><td><code>string</code></td><td>Specifies the operating system platform when you use a custom source image.</td></tr>
<tr><td><code>ContainerType</code></td><td><code>string</code></td><td>Specifies the type of container, such as Docker.</td></tr>
<tr><td><code>ImageOsVersionOverride</code></td><td><code>string</code></td><td>Specifies the operating system version for the source image.</td></tr>
<tr><td><code>TargetRepository</code></td><td><code>object</code></td><td>The destination repository for the container image.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>Identifies which KMS key is used to encrypt the container image.</td></tr>
<tr><td><code>ParentImage</code></td><td><code>string</code></td><td>The source image for the container recipe.</td></tr>
<tr><td><code>WorkingDirectory</code></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>Tags that are attached to the container recipe.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.imagebuilder.container_recipes<br/>WHERE region = 'us-east-1'
</pre>
