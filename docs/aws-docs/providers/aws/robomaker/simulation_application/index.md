---
title: simulation_application
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation_application
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>simulation_application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation_application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.robomaker.simulation_application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the simulation application.</td></tr><tr><td><code>CurrentRevisionId</code></td><td><code>string</code></td><td>The current revision id.</td></tr><tr><td><code>RenderingEngine</code></td><td><code>undefined</code></td><td>The rendering engine for the simulation application.</td></tr><tr><td><code>RobotSoftwareSuite</code></td><td><code>undefined</code></td><td>The robot software suite used by the simulation application.</td></tr><tr><td><code>SimulationSoftwareSuite</code></td><td><code>undefined</code></td><td>The simulation software suite used by the simulation application.</td></tr><tr><td><code>Sources</code></td><td><code>array</code></td><td>The sources of the simulation application.</td></tr><tr><td><code>Environment</code></td><td><code>string</code></td><td>The URI of the Docker image for the robot application.</td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.robomaker.simulation_application
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>'
</pre>
