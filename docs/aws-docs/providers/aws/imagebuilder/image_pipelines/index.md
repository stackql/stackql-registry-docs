---
title: image_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - image_pipelines
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
Retrieves a list of <code>image_pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image_pipelines</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.image_pipelines</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image pipeline.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the image pipeline.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the image pipeline.</td></tr>
<tr><td><code>ImageTestsConfiguration</code></td><td><code>object</code></td><td>The image tests configuration of the image pipeline.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the image pipeline.</td></tr>
<tr><td><code>Schedule</code></td><td><code>object</code></td><td>The schedule of the image pipeline.</td></tr>
<tr><td><code>ImageRecipeArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</td></tr>
<tr><td><code>ContainerRecipeArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</td></tr>
<tr><td><code>DistributionConfigurationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.</td></tr>
<tr><td><code>InfrastructureConfigurationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.</td></tr>
<tr><td><code>EnhancedImageMetadataEnabled</code></td><td><code>boolean</code></td><td>Collects additional information about the image being created, including the operating system (OS) version and package list.</td></tr>
<tr><td><code>ImageScanningConfiguration</code></td><td><code>object</code></td><td>Contains settings for vulnerability scans.</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>The tags of this image pipeline.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.imagebuilder.image_pipelines<br/>WHERE region = 'us-east-1'
</pre>
