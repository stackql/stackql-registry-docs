---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Endpoint. |
| `description` | `string` | The description of the Endpoint. |
| `createTime` | `string` | Output only. Timestamp when this Endpoint was created. |
| `trafficSplit` | `object` | A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment. |
| `network` | `string` | Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. Only one of the fields, network or enable_private_service_connect, can be set. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/&#123;project&#125;/global/networks/&#123;network&#125;`. Where `&#123;project&#125;` is a project number, as in `12345`, and `&#123;network&#125;` is network name. |
| `labels` | `object` | The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `modelDeploymentMonitoringJob` | `string` | Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/modelDeploymentMonitoringJobs/&#123;model_deployment_monitoring_job&#125;` |
| `predictRequestResponseLoggingConfig` | `object` | Configuration for logging request-response to a BigQuery table. |
| `enablePrivateServiceConnect` | `boolean` | Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set. |
| `displayName` | `string` | Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `updateTime` | `string` | Output only. Timestamp when this Endpoint was last updated. |
| `deployedModels` | `array` | Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointsId, locationsId, projectsId` | Gets an Endpoint. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Endpoints in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates an Endpoint. |
| `delete` | `DELETE` | `endpointsId, locationsId, projectsId` | Deletes an Endpoint. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Endpoints in a Location. |
| `deploy_model` | `EXEC` | `endpointsId, locationsId, projectsId` | Deploys a Model into this Endpoint, creating a DeployedModel within it. |
| `explain` | `EXEC` | `endpointsId, locationsId, projectsId` | Perform an online explanation. If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated. |
| `mutate_deployed_model` | `EXEC` | `endpointsId, locationsId, projectsId` | Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only). |
| `patch` | `EXEC` | `endpointsId, locationsId, projectsId` | Updates an Endpoint. |
| `predict` | `EXEC` | `endpointsId, locationsId, projectsId` | Perform an online prediction. |
| `raw_predict` | `EXEC` | `endpointsId, locationsId, projectsId` | Perform an online prediction with an arbitrary HTTP payload. The response includes the following HTTP headers: * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. |
| `server_streaming_predict` | `EXEC` | `endpointsId, locationsId, projectsId` | Perform a server-side streaming online prediction request for Vertex LLM streaming. |
| `undeploy_model` | `EXEC` | `endpointsId, locationsId, projectsId` | Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using. |
