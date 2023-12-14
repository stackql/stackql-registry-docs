---
title: builds
hide_title: false
hide_table_of_contents: false
keywords:
  - builds
  - deployments
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.deployments.builds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the Build |
| `config` | `object` | An object that contains the Build's configuration |
| `copiedFrom` | `string` |  |
| `createdAt` | `number` | The time at which the Build was created |
| `createdIn` | `string` | The region where the Build was first created |
| `deployedAt` | `number` | The time at which the Build was deployed |
| `deploymentId` | `string` | The unique identifier of the deployment |
| `entrypoint` | `string` | The entrypoint of the deployment |
| `fingerprint` | `string` | If the Build uses the `@vercel/static` Runtime, it contains a hashed string of all outputs |
| `output` | `array` | A list of outputs for the Build that can be either Serverless Functions or static files |
| `readyState` | `string` | The state of the deployment depending on the process of deploying, or if it is ready or in an error state |
| `readyStateAt` | `number` | The time at which the Build state was last modified |
| `scheduledAt` | `number` | The time at which the Build was scheduled to be built |
| `use` | `string` | The Runtime the Build used to generate the output |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_builds_for_deployment` | `SELECT` | `deploymentId` |
| `_get_builds_for_deployment` | `EXEC` | `deploymentId` |
