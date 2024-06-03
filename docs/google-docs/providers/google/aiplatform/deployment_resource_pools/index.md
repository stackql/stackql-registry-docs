---
title: deployment_resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_resource_pools
  - aiplatform
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.deployment_resource_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the DeploymentResourcePool. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/deploymentResourcePools/&#123;deployment_resource_pool&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this DeploymentResourcePool was created. |
| <CopyableCode code="dedicatedResources" /> | `object` | A description of resources that are dedicated to a DeployedModel, and that need a higher degree of manual configuration. |
| <CopyableCode code="disableContainerLogging" /> | `boolean` | If the DeploymentResourcePool is deployed with custom-trained Models or AutoML Tabular Models, the container(s) of the DeploymentResourcePool will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing). User can disable container logging by setting this flag to true. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account that the DeploymentResourcePool's container(s) run as. Specify the email address of the service account. If this service account is not specified, the container(s) run as a service account that doesn't have access to the resource project. Users deploying the Models to this DeploymentResourcePool must have the `iam.serviceAccounts.actAs` permission on this service account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | Get a DeploymentResourcePool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List DeploymentResourcePools in a location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a DeploymentResourcePool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | Delete a DeploymentResourcePool. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List DeploymentResourcePools in a location. |
| <CopyableCode code="query_deployed_models" /> | `EXEC` | <CopyableCode code="deploymentResourcePoolsId, locationsId, projectsId" /> | List DeployedModels that have been deployed on this DeploymentResourcePool. |
