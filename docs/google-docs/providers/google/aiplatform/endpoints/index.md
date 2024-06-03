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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the Endpoint. |
| <CopyableCode code="description" /> | `string` | The description of the Endpoint. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Endpoint was created. |
| <CopyableCode code="deployedModels" /> | `array` | Output only. The models deployed in this Endpoint. To add or remove DeployedModels use EndpointService.DeployModel and EndpointService.UndeployModel respectively. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the Endpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="enablePrivateServiceConnect" /> | `boolean` | Deprecated: If true, expose the Endpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="modelDeploymentMonitoringJob" /> | `string` | Output only. Resource name of the Model Monitoring job associated with this Endpoint if monitoring is enabled by JobService.CreateModelDeploymentMonitoringJob. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/modelDeploymentMonitoringJobs/&#123;model_deployment_monitoring_job&#125;` |
| <CopyableCode code="network" /> | `string` | Optional. The full name of the Google Compute Engine [network](https://cloud.google.com//compute/docs/networks-and-firewalls#networks) to which the Endpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. Only one of the fields, network or enable_private_service_connect, can be set. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): `projects/&#123;project&#125;/global/networks/&#123;network&#125;`. Where `&#123;project&#125;` is a project number, as in `12345`, and `&#123;network&#125;` is network name. |
| <CopyableCode code="predictRequestResponseLoggingConfig" /> | `object` | Configuration for logging request-response to a BigQuery table. |
| <CopyableCode code="privateServiceConnectConfig" /> | `object` | Represents configuration for private service connect. |
| <CopyableCode code="trafficSplit" /> | `object` | A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Endpoint was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Gets an Endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Endpoints in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Deletes an Endpoint. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Updates an Endpoint. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Endpoints in a Location. |
| <CopyableCode code="compute_tokens" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Return a list of tokens based on the input text. |
| <CopyableCode code="count_tokens" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform a token counting. |
| <CopyableCode code="deploy_model" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Deploys a Model into this Endpoint, creating a DeployedModel within it. |
| <CopyableCode code="direct_predict" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks. |
| <CopyableCode code="direct_raw_predict" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform an unary online prediction request to a gRPC model server for custom containers. |
| <CopyableCode code="explain" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform an online explanation. If deployed_model_id is specified, the corresponding DeployModel must have explanation_spec populated. If deployed_model_id is not specified, all DeployedModels must have explanation_spec populated. |
| <CopyableCode code="generate_content" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Generate content with multimodal inputs. |
| <CopyableCode code="mutate_deployed_model" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only). |
| <CopyableCode code="predict" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform an online prediction. |
| <CopyableCode code="raw_predict" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform an online prediction with an arbitrary HTTP payload. The response includes the following HTTP headers: * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction. * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction. |
| <CopyableCode code="server_streaming_predict" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform a server-side streaming online prediction request for Vertex LLM streaming. |
| <CopyableCode code="stream_generate_content" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Generate content with multimodal inputs with streaming support. |
| <CopyableCode code="stream_raw_predict" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Perform a streaming online prediction with an arbitrary HTTP payload. |
| <CopyableCode code="undeploy_model" /> | `EXEC` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using. |
