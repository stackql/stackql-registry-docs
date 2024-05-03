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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.deployments.builds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the Build |
| <CopyableCode code="config" /> | `object` | An object that contains the Build's configuration |
| <CopyableCode code="copiedFrom" /> | `string` |  |
| <CopyableCode code="createdAt" /> | `number` | The time at which the Build was created |
| <CopyableCode code="createdIn" /> | `string` | The region where the Build was first created |
| <CopyableCode code="deployedAt" /> | `number` | The time at which the Build was deployed |
| <CopyableCode code="deploymentId" /> | `string` | The unique identifier of the deployment |
| <CopyableCode code="entrypoint" /> | `string` | The entrypoint of the deployment |
| <CopyableCode code="fingerprint" /> | `string` | If the Build uses the `@vercel/static` Runtime, it contains a hashed string of all outputs |
| <CopyableCode code="output" /> | `array` | A list of outputs for the Build that can be either Serverless Functions or static files |
| <CopyableCode code="readyState" /> | `string` | The state of the deployment depending on the process of deploying, or if it is ready or in an error state |
| <CopyableCode code="readyStateAt" /> | `number` | The time at which the Build state was last modified |
| <CopyableCode code="scheduledAt" /> | `number` | The time at which the Build was scheduled to be built |
| <CopyableCode code="use" /> | `string` | The Runtime the Build used to generate the output |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_builds_for_deployment" /> | `SELECT` | <CopyableCode code="deploymentId" /> |
| <CopyableCode code="_get_builds_for_deployment" /> | `EXEC` | <CopyableCode code="deploymentId" /> |
