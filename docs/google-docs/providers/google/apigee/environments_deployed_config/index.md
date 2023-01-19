---
title: environments_deployed_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_deployed_config
  - apigee
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
<tr><td><b>Name</b></td><td><code>environments_deployed_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.environments_deployed_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the environment configuration in the following format: `organizations/&#123;org&#125;/environments/&#123;env&#125;/configs/&#123;config&#125;` |
| `dataCollectors` | `array` | List of data collectors used by the deployments in the environment. |
| `pubsubTopic` | `string` | Name of the PubSub topic for the environment. |
| `resourceReferences` | `array` | List of resource references in the environment. |
| `traceConfig` | `object` | NEXT ID: 8 RuntimeTraceConfig defines the configurations for distributed trace in an environment. |
| `featureFlags` | `object` | Feature flags inherited from the organization and environment. |
| `sequenceNumber` | `string` | DEPRECATED: Use revision_id. |
| `deployments` | `array` | List of deployments in the environment. |
| `gatewayConfigLocation` | `string` | The location for the gateway config blob as a URI, e.g. a Cloud Storage URI. This is only used by Envoy-based gateways. |
| `revisionId` | `string` | Revision ID of the environment configuration. The higher the value, the more recently the configuration was deployed. |
| `provider` | `string` | Used by the Control plane to add context information to help detect the source of the document during diagnostics and debugging. |
| `forwardProxyUri` | `string` | The forward proxy's url to be used by the runtime. When set, runtime will send requests to the target via the given forward proxy. This is only used by programmable gateways. |
| `deploymentGroups` | `array` | List of deployment groups in the environment. |
| `targets` | `array` | List of target servers in the environment. Disabled target servers are not displayed. |
| `flowhooks` | `array` | List of flow hooks in the environment. |
| `arcConfigLocation` | `string` | The location for the config blob of API Runtime Control, aka Envoy Adapter, for op-based authentication as a URI, e.g. a Cloud Storage URI. This is only used by Envoy-based gateways. |
| `createTime` | `string` | Time that the environment configuration was created. |
| `uid` | `string` | Unique ID for the environment configuration. The ID will only change if the environment is deleted and recreated. |
| `envScopedRevisionId` | `string` | Revision ID for environment-scoped resources (e.g. target servers, keystores) in this config. This ID will increment any time a resource not scoped to a deployment group changes. |
| `resources` | `array` | List of resource versions in the environment. |
| `debugMask` | `object` |  |
| `keystores` | `array` | List of keystores in the environment. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_getDeployedConfig` | `SELECT` | `environmentsId, organizationsId` |
